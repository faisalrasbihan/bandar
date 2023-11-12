from openai import OpenAI
import json
import os



def openai_search(openai_api_key, product_name):
  
  os.environ["OPENAI_API_KEY"] = openai_api_key
  client = OpenAI() 
  
  user_prompt = '''Please give ALL possible matches for the product "{fname}" from this Product SKU list:

  Urea Petro
  Urea PIM
  Urea Nitrea
  Urea Daun Buah
  Urea Pusri
  Nitralite
  ZA Petro
  ZA Plus Petro
  ZK Petro
  Petro-CAS
  SP-36 Petro
  Rock Phosphate PETRO
  Phosgreen
  SP-26 Petro
  Petro BioFertil
  Phonska Plus 15-15-15+9S+0.2Zn
  NPK Kebomas 12-12-17+2MgO+0.1Zn+0.2B+0.2Fe
  NPK Kebomas 12-6-22+3Mg
  NPK Kebomas 15-15-15
  PETROFERT  16-16-8+13S
  Petro Niphos 20-20+13S
  FERTIGRES  16-20+13S 
  NPK PIM 15-15-15
  Nitroku 16-16-16
  NITROSKA  15-9-20+1.5MgO+3S 
  NPK Kujang 15-15-15 
  NPK Kujang 30-6-8
  Polivit-PIM 0-0-12+48S+9MgO
  Solution N 28-10-10 + TE
  Pelangi Agro 20-10-10
  Pelangi Jos 16-16-16 Coating Mikroba
  Pelangi 16-16-16
  Pelangi 15-15-15
  NPK Pusri 15-15-15 
  Pelangi 20-10-18
  Pelangi 12-12-17-2
  NPK Pelangi 13-6-27-4
  Petro Nitrat 16-16-16
  Jeranti 18-10-14+2S+TE
  NPK Pusri 16-16-16
  NPK Pusri 13-6-27-4Mg+0.65B
  NPK Petro Ningrat 12-11-20
  Kapur Pertanian Kebomas
  MerokeZA
  MerokeROCK
  MerokeTSP
  MerokeKKB 0-0-40-0.8B
  Suburkali Butir 0-0-30+17S+10MgO
  MerokeSOP KALI 0-0-52+18S
  MerokeMOP
  KARATE PLUS BORONI 15.5-0-0+0.3S+26CaO
  Mutiara PARTNER 13-13-24
  Mutiara 16-16-16
  Mutiara PROFESSIONAL 9-25-25
  Mutiara SPRINTER 20-10-10
  MerokeCPN NK 15-15+TE
  MerokeMAP 12-61-0
  MerokeMKP 0-52-34
  Meroke Flex-G 8-9-39+3MgO
  SS (AMMOPHOS) 16-20-0+12S
  Mutiara GROWER 15-09-20+TE
  Mahkota ZA
  RP Peru
  RP Mesir
  Triple Super Phospate (TSP)
  Mahkota Kieserite
  Borat
  Mahkota MOP (KCL Canada)
  Mahkota NP 16-20-12S
  Mahkota 15-15-6-4
  Mahkota 12-6-22-3+TE
  Mahkota 12-12-17-2+TE
  Mahkota 13-6-27-4+0.5B
  Mahkota 13-8-27-4+0.65B
  Mahkota 15-15-15
  Mahkota 16-16-16
  Urecote
  ZA Pak Tani
  Fertiphos
  Phosgro
  Fertiphos Sawit
  Magnesium Sulfate
  Fertikali
  Saprodap  16-20+12S
  Pak Tani 15-15-15+TE
  Pak Tani Holland  15-15-15
  Pak Tani  16-16-16 Merah
  Pak Tani  16-16-16 Biru
  Pak Tani Sawit  15-15-6-4
  Pak Tani Sawit 12-12-17-2
  Pak Tani Sawit  13-6-27-4+0.65B
  Pak Tani Sawit  13-8-27-4+0.5B
  Pak Tani Sawit  7-6-35+B+Cu+Zn
  Magnum 15-10-22-2Mg-3.8S
  Pak Tani Padi  21-14-7+2MgO+2S+TE
  Pak Tani Fertila 13-6-27-4Mg+0.65B+TE
  Pak Tani Fertila  18-6-14+5S
  Pak Tani Fertilla 18-8-10+3MgO+TE
  Pak Tani Fertila  21-14-7+4MgO+TE
  Pak Tani Fertila 20-10-12+TE
  Pak Tani Fertila  28-6-13+3MgO+TE
  Pak Tani Fertila 8-15-19
  Pak Tani Singkong  15-15-15
  Pak Tani 12-12-17-2
  Pak Tani Sawit  12-6-22-3+TE
  Pak Tani  9-15-6
  Pak Tani Fertila Qrop   12-6-24
  MKP PAK TANI 0-52-32
  CPN PAK TANI 15-0-15
  ULTRADAP 12-60-0
  NEO KRISTALON 12-12-36
  NEO KRISTALON 18-18-18-0.8Mg-2S+0.02Mn+0.036Zn+0.02B
  FERTILA 6-18-28-0.6Mg-5S+0.1B+0.01Zn+0.01Cu
  FERTILA 12-6-24-0.75Mg-1.5CaO-5.6s
  FERTILA 0-16-17
  PN PAK TANI 13-0-46+0.55Cl
  YaraVera
  Ammonium Sulfate
  YaraVita TRI-PHOLATE 0-0-0-70Mn+50Zn+25Fe+20B+20Cu+1Mo
  YaraLiva TROPICOTE 15.5-0-0+19Ca
  YaraTera CALCINIT 15-0-0+26CaO
  YaraTera KRISTA K 13.7-0-46.3
  YaraTera KRISTA MAP 12-61-0
  YaraMila PALMAE 13-11-21+2MgO+0.2B
  YaraLiva NITRABOR 15.5-0-0+25.6CaO+0.3B
  YaraMila WINNER 15-09-20+1.3MgO+3.4S+TE
  YaraMila UNIK 16-16-16
  YaraMila FASTER 25-7-7
  YARAMILA COMPLEX 12-11-18-3Mg-8S+0.02Zn+0.03Mn-2.56Ca+0.22Fe
  YaraTera KRISTA MKP 0-52-34
  Vrea
  Nitroplus (ZA)
  MK FOS 0-52-34
  HSP Astiva
  KSP
  CAP TAWON 12-12-17-2Mg
  CAP TAWON 15-15-15
  CAP TAWON 15-15-6-4
  CAP TAWON 16-16-16
  CAP TAWON 18-12-6
  CAP TAWON 19-9-19
  HXAS
  HX-MROPH
  HX-MKP 0-50-35
  HX-DAP 18-46-0
  DGW TSP
  DGW KNO3
  COCKHEAD 12-12-17-2Mg
  COCKHEAD 12-6-22-3Mg
  COCKHEAD 13-6-27-4Mg+0.65B
  COCKHEAD 15-15-15
  COCKHEAD 15-15-6-4Mg
  COCKHEAD 16-16-16
  COCKHEAD 7-6-34
  COMPACTION DGW 15-15-15+TE
  BOOSTER DGW 12-6-22-3+TE
  GOLD DGW 16-10-18
  COCKHEAD 13-8-27-4+TE
  DGW 16-16-16+TE
  ENTEC 13-10-20
  NITROPHOSKA 13-10-20
  ENTEC 20-10-10
  NITROPHOSKA PLUS 12-12-17-2
  NITROPHOSKA PERFECT 15-5-20
  ENTEC 13-10-20
  CANTIK CALCINIT
  NITROPHOSKA 15-15-15
  Brucite
  EMCOTE 13-11-11-7Ca-2Mg-6S+TE(0.08Cu+0.5B)
  EMCOTE 13-6-27-2+TE
  MESTI-PATENHIJO 15-10-20+TE
  MESTIFOSKA 15-15-15+TE
  EMCOTE 15-15-6-4+TE
  MESTIFOS 15-20-0+12S
  MESTI-PATENBIRU 16-16-16+TE
  MESTI-BOMBER 19-9-19+TE
  EMCOTE 20-6-14
  MESTI-KP 0-52-34
  Mesti-ZA
  Mesti-TSP
  Mesti-Rock
  Mestikali
  Mestical
  Mesti-GAS
  Mestac
  MestiKisrit
  Borate Evermax

  ONLY return Product SKU Name that is available in Product SKU list.

  return FULL NAME of product SKU IF and only IF you found possible matches.

  ONLY return a comma-separated list, and nothing more.

  RETURN "NOT FOUND" if you don't find any match'''.format(fname = product_name)
  
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