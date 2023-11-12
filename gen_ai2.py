from openai import OpenAI
import json
import os
from product_catalog import get_product_list

def openai_search(openai_api_key, product_name):
  
  os.environ["OPENAI_API_KEY"] = openai_api_key
  client = OpenAI() 
  
  product_list = get_product_list()
  
  user_prompt = '''Please give ALL possible matches for the product "{fname}" from this Product SKU list:

  {plist}

  ONLY return Product SKU Name that is available in Product SKU list.

  return FULL NAME of product SKU IF and only IF you found possible matches.

  ONLY return a comma-separated list, and nothing more.

  RETURN "NOT FOUND" if you don't find any match'''.format(fname = product_name, plist = product_list)
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "system", "content": "You are an assistent that generate JSON and only JSON without additional description or context, I will give you a product name and you need to find possible matches from the product list that I gave you in JSON Format. Do not include any explanations, only provide a RFC8259 compliant JSON response without newline following this format without deviation. "},
      {"role": "user", "content": user_prompt}
    ]
  )
  # print(completion.choices[0].message.content)
  res = json.loads(completion.choices[0].message.content)

  return res
  
# DELETE IN PRODUCTION
# result = openai_search("Mutiara")
# print(result['matches'].split(","))