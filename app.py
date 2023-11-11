import streamlit as st
from langchain.llms import OpenAI
from gen_ai2 import openai_search
# st.set_page_config(page_title="🦜🔍 DSW Product Finder App")
st.set_page_config(page_title="Bandar")

st.title('🔍 DSW 2023 Product Finder App')
st.write("🚀 Made by Bandamology Team for the Data Science Weekend 2023 Data Challenge")

# openai_api_key = st.sidebar.text_input('OpenAI API Key')

# def generate_response(input_text):
#   llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#   st.info(llm(input_text))
  
def search_product(product_name):
  ## Sample Logic here
  if product_name != 'keong':
    product_list = ['Roundup', 'Glyphosate', 'Fujiwan']
    return product_list
  else:
    return None

st.sidebar.header("About")
st.sidebar.markdown((
      "[Bandar](https://bandar.streamlit.app) is a Product Finder application designed for submission to the Senior Professional Category of the 2023 Data Science Weekend Competition."
  ))
st.sidebar.header("Copyright notice")
st.sidebar.markdown("No part of this publication or its text may be made publicly available or, excepting personal use, reproduced, or distributed or translated into other languages without the prior written permission of Berlin Product People GmbH. If you would like permission to reproduce or otherwise publish any part or all of this publication or its text, including translations thereof, write to us at info@berlin-product-people.com addressed “Attention: Permissions Request.”")

with st.form('my_form'):
  text = st.text_input("Search product name", value="")
  submitted = st.form_submit_button('Submit')
  
  # Submit button is pressed
  if submitted:
    # products = search_product(text)
    products = openai_search(text)
    if products is not None:
      st.caption("Below are the possible product names")
      for product in products:
        with st.expander('Product SKU : ' + product):
          st.write("Product Type :")
    else:
      st.warning('Product name not found, is this the product that you are referring to?')

  # # Delete later
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('Please enter your OpenAI API key!', icon='⚠')
  # if submitted and openai_api_key.startswith('sk-'):
  #   generate_response(text)
  # # Put inside search product
  # if text == 'keong':
  #   st.info('Product name not found, is this the product that you are referring to?')
