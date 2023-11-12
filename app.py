import streamlit as st
from gen_ai2 import openai_search
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
st.sidebar.markdown("Open AI API Key dapat dilihat pada slide materi tim Bandarmology pada link berikut : [Get an OpenAI API key](https://docs.google.com/presentation/d/1nP1aToowg5b3datkuYCHMgaGIjWT-fvCfMsyRW2uMv8/edit?usp=sharing)")
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
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    # Search OpenAI for free-text input
    search_result = openai_search(openai_api_key, text)
    print(search_result['matches'])
    # Split output to string
    products = search_result['matches'].split(",")
    if products is not None:
      st.caption("Below are the possible product names")
      for product in products:
        with st.expander(product):
          st.write("Product Type :")
      
      st.info('Didnt find the product you are looking for? Suggest a new Product SKU Name')
      title = st.text_input('New Product SKU')
      suggestted = st.form_submit_button('Suggest New Product')
    else:
      st.warning('Product name not found, Please retype your product name')