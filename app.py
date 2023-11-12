import streamlit as st
from gen_ai2 import openai_search
import algo as ca

# st.set_page_config(page_title="🦜🔍 DSW Product Finder App")
st.set_page_config(page_title="Bandar")

st.title('🔍 DSW 2023 Product Finder App')
st.write("Made by Bandamology Team for the Data Science Weekend 2023 Data Challenge 🚀")
  
def search_product(product_name):
  ## Sample Logic here
  if product_name != 'keong':
    product_list = ['Roundup', 'Glyphosate', 'Fujiwan']
    return product_list
  else:
    return None

openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.sidebar.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
st.sidebar.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")
st.sidebar.header("About")
st.sidebar.markdown((
      "[Bandar](https://bandar.streamlit.app) is a Product Finder application designed for submission to the Senior Professional Category of the 2023 Data Science Weekend Competition."
  ))
st.sidebar.header("Copyright notice")
st.sidebar.markdown("No part of this publication or its text may be made publicly available or, excepting personal use, reproduced, or distributed or translated into other languages without the prior written permission of Berlin Product People GmbH. If you would like permission to reproduce or otherwise publish any part or all of this publication or its text, including translations thereof, write to us at faisalrasbihan@gmail.com addressed “Attention: Permissions Request.”")

with st.form('my_form'):
  text = st.text_input("Search product name", value="")
  submitted = st.form_submit_button('Submit')
  
  # Submit button is pressed
  if submitted:
    # Check if OpenAI key is filled

    classic_algo_result = ca.classic_algo(text)
    if not classic_algo_result:
      if not openai_api_key:
        # Open AI key is not found, user cant search using Gen AI method
        st.warning("Product not found, please add your OpenAI API key to continue searching using Generative AI.")
        st.stop()
      else:
        # Search OpenAI for free-text input
        search_result = openai_search(openai_api_key, text)
        print(search_result)
        products = search_result.split(",")
    else:
      products = classic_algo_result
    # Split output to string
    if products is not None:
      st.caption("Below are the possible product names")
      for product in products:
        with st.expander(product):
          st.write("Product Type : Fertilizer")
      st.divider()
      st.info('Didnt find the product you are looking for? Suggest a new Product SKU Name')
      title = st.text_input('New Product SKU')
      suggestted = st.form_submit_button('Suggest New Product')
    else:
      st.warning('Product name not found, Please retype your product name')