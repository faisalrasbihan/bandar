import pandas as pd
import fuzz

def clean_column_names(df):
    cleaned_df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
    return cleaned_df

def matching_tokens(product_prompt_tokens, product_sku_tokens):
    matching_tokens = []
    for product_prompt_token in product_prompt_tokens:
        for product_sku_token in product_sku_tokens:
            if product_prompt_token == product_sku_token:
                if product_prompt_token not in matching_tokens:
                    matching_tokens.append(product_prompt_token)
            elif fuzz.ratio(product_prompt_token, product_sku_token) >= 80:
                # If the two tokens are not exactly the same, but the partial ratio is
                # greater than or equal to 99, then we consider them to be a match.
                if product_sku_token not in matching_tokens:
                    matching_tokens.append(product_sku_token)
    return matching_tokens

def product_catalog_processing(path):
    product_catalog_df = clean_column_names(pd.read_csv(path))
    product_catalog_df['product_sku'] = product_catalog_df['product_sku'].astype(str)

    # Replace + with space
    product_catalog_df['product_sku'] = product_catalog_df['product_sku'].str.replace('+', ' ').str.replace('@', ' ')
    product_catalog_df['combined_name'] = product_catalog_df.apply(lambda row: ' '.join(str(val) for val in row if not pd.isna(val)), axis=1)

    # Split 'combined_name' into tokens based on the space delimiter and save into a new column
    product_catalog_df['product_sku_tokens'] = product_catalog_df['combined_name'].str.split().apply(lambda tokens: list(set(token.lower() for token in tokens)))

    # Create a list 'token_corpus' containing all the tokens
    token_corpus = [token for tokens in product_catalog_df['product_sku_tokens'] for token in tokens]

    # Convert all tokens to lowercase and remove duplicates
    token_corpus = list(set([token for token in token_corpus]))
    return product_catalog_df, token_corpus

def product_prompt_processing(prompt, token_corpus):
    
    # Convert prompt string to dataframe
    product_prompt_df = pd.DataFrame({'product_prompt': [prompt]})

    # Replace + with space
    product_prompt_df['product_prompt_cleaned'] = product_prompt_df['product_prompt'].str.replace('+', ' ').str.replace('@', ' ')

    # Split 'product_sku' into tokens based on the space delimiter and save into a new column
    product_prompt_df['product_prompt_tokens_all'] = product_prompt_df['product_prompt_cleaned'].str.split().apply(lambda tokens: [token.lower() for token in tokens])

    product_prompt_df['product_prompt_tokens'] = product_prompt_df['product_prompt_tokens_all'].apply(lambda x: matching_tokens(x, token_corpus))

    return product_prompt_df

def combine_prompt_and_catalog(product_prompt_df, product_catalog_df):
    # Performing a cross join (cartesian product) without a key column
    base_df = product_prompt_df.assign(CrossJoinKey=1).merge(product_catalog_df.assign(CrossJoinKey=1), on='CrossJoinKey')

    # Drop the 'CrossJoinKey' column, which is no longer needed
    base_df = base_df.drop('CrossJoinKey', axis=1)
    base_df = base_df[['product_prompt', 'product_sku', 'brand', 'type', 'formula', 'product_prompt_tokens', 'product_sku_tokens']]

    return base_df

def fuzzy_classic_algorithm(base_df):

    base_df['matching_tokens'] = base_df.apply(lambda x: matching_tokens(x['product_prompt_tokens'], x['product_sku_tokens']), axis=1)

    # Count the number of lists in the `matching_tokens` column
    base_df['count_matching_tokens'] = base_df['matching_tokens'].apply(lambda x: len(x))
    base_df['count_product_prompt_tokens'] = base_df['product_prompt_tokens'].apply(lambda x: len(x))
    base_df['count_product_sku_tokens'] = base_df['product_sku_tokens'].apply(lambda x: len(x))


    # Scoring based on percentage matching
    base_df['percent_prompt_match'] = base_df['count_matching_tokens'] / base_df['count_product_prompt_tokens']
    base_df['percent_sku_match'] = base_df['count_matching_tokens'] / base_df['count_product_sku_tokens']
    base_df['percent_prompt_sku_match'] = (base_df['percent_prompt_match'] + base_df['percent_sku_match'])/2

    # Fill missing values in `base_df['percent_prompt_sku_match']` with 0
    base_df['percent_prompt_sku_match'] = base_df['percent_prompt_sku_match'].fillna(0)

    # Sort and rank within partitions
    base_df['rank'] = base_df.groupby('product_prompt')['percent_prompt_sku_match'].rank(method='first', ascending=False).astype(int)

    # Sort the DataFrame by 'product_prompt' and 'rank'
    base_df = base_df.sort_values(by=['product_prompt', 'rank'])

    # Filter rows with rank 1
    result_df = base_df[base_df['rank'].isin([1,2,3,4,5])]

    # Filter rows where percent_prompt_sku_match is more than 0.5
    filtered_result_df = result_df[result_df['percent_prompt_sku_match'] > 0.25]

    # Create a DataFrame with all unique 'product_prompt' values
    all_product_prompts = pd.DataFrame({'product_prompt': result_df['product_prompt'].unique()})

    # Merge the all_product_prompts DataFrame with the filtered_result_df
    final_result_df = pd.merge(all_product_prompts, filtered_result_df[['product_prompt', 'product_sku']], on='product_prompt', how='left')

    # Group by 'product_prompt' and aggregate 'product_sku' values into a list
    final_result_df = final_result_df.groupby('product_prompt')['product_sku'].agg(lambda x: [] if pd.isnull(x).all() else x.tolist()).reset_index()

    # Rename the 'product_sku' column to 'suggestion'
    final_result_df.rename(columns={'product_sku': 'suggestion'}, inplace=True)

    return final_result_df


def classic_algo(prompt):
   
    # Product Catalog
    product_catalog_df, token_corpus = product_catalog_processing('Product Catalog.csv')

    # Product Prompt
    product_prompt_df = product_prompt_processing(prompt, token_corpus)

    # Combine
    base_df = combine_prompt_and_catalog(product_prompt_df, product_catalog_df)

    # Fuzzy Classic Algorithm
    final_result_df = fuzzy_classic_algorithm(base_df)

    # Get Suggestion
    suggestion = final_result_df[final_result_df.product_prompt == prompt]['suggestion'].iloc[0]

    return suggestion



    
