import pandas as pd

def get_product_list():
    df1 = pd.read_csv('product_catalog.csv')
    df2 = pd.read_csv('product_catalog_enriched.csv')

    list1 = df1.iloc[:, 0].tolist()
    list2 = df2.iloc[:, 0].tolist()

    union_list = list(set(list1 + list2))

    combined_string = "\n".join(union_list)

    return combined_string
    print(combined_string)