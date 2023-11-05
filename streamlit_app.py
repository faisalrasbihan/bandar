import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="🦜🔗 DSW Product Finder App")
st.title('🔍 DSW 2023 Product Finder App')
st.caption("🚀 Product finder application made by Bandamology Team for the Data Science Weekend 2023 Data Hackathon")

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))
  
def search_product(product_name):
  ## Logic here
  product_list = ['Roundup', 'Glyphosate', 'Fujiwan']
  return product_list

with st.form('my_form'):
  text = st.text_input("Search product name", value="")
  submitted = st.form_submit_button('Submit')
  
  # Submit button is pressed
  if submitted:
    products = search_product(text)
    st.caption("Below are the possible product names")
    for product in products:
      with st.expander(product):
        st.write("Product Type :")

  # Delete later
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
  # Put inside search product
  if text == 'keong':
    st.info('Product name not found, is this the product that you are referring to?')
