import streamlit as st

with st.sidebar:
    st.write("**Streamlit app created by:**")

    st.write("Bandarmology Team")
    st.write("Faisal Rasbihan")
    st.write("Taufik Eko Hidayanto")
    st.write("Arda Putra Ryandika")
    st.write("**Questions and answers sourced from:**")
    st.caption(" 82 Product Owner Interview Questions to Avoid Hiring Imposters")
    st.caption("By Stefan Wolpers | Version 8.01 | 2022-01-17")
    st.caption("https://berlin-product-people.com/")
    st.caption(
        "Download link: https://age-of-product.com/42-scrum-product-owner-interview-questions/"
    )
    st.write("Copyright notice:")
    st.caption(
        "No part of this publication or its text may be made publicly available or, excepting personal use, reproduced, or distributed or translated into other languages without the prior written permission of Berlin Product People GmbH. If you would like permission to reproduce or otherwise publish any part or all of this publication or its text, including translations thereof, write to us at info@berlin-product-people.com addressed “Attention: Permissions Request.”"
    )
    st.caption("Materials in the app used with permission of Stefan Wolpers")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


st.title("💬 Bandar Product Name Finder")
text_search = st.text_input("Search in titles, questions and answers", value="")

text = st.text_area(
    # Instructions
    "Product name not found, is this the product that you meant?",
    # 'sample' variable that contains our keyphrases.
    height=200,

)