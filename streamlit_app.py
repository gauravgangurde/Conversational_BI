import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import openai
import json
import ast

image = Image.open('exl.png')
	
with st.sidebar:
	st.image(image, width = 150)
	st.header('Generative AI')


st.header("Test")

response = """{ "mails": [ { "name": "Agent 1", "performance category": "Consistent achiever", "mail": "Dear Agent 1,\n\nI am writing to provide you with feedback on your latest performance data. It is great to see that you have consistently achieved your targets and even exceeded them last month. Keep up the good work!\n\nHowever, I would suggest that you focus on improving your communication skills with clients. This can help you build better relationships and increase sales.\n\nHere are two articles that can help you improve your sales skills:\n1. https://hbr.org/2017/06/the-best-salespeople-are-deeply-empathetic\n2. https://www.salesforce.com/blog/2017/01/5-sales-tips-from-people-who-hate-sales.html\n\nThank you for your hard work.\n\nBest regards,\nManager" }, { "name": "Agent 5", "performance category": "Consistent achiever", "mail": "Dear Agent 5,\n\nI am writing to provide you with feedback on your latest performance data. It is great to see that you have consistently achieved your targets and even exceeded them last month. Keep up the good work!\n\nHowever, I would suggest that you focus on improving your time management skills. This can help you increase your productivity and achieve even better results.\n\nHere are two training links that can help you improve your sales skills:\n1. https://www.udemy.com/course/time-management-salespeople/\n2. https://www.carew.com/time-management-sales-training/\n\nThank you for your hard work.\n\nBest regards,\nManager" }, { "name": "Agent 9", "performance category": "Consistent achiever", "mail": "Dear Agent 9,\n\nI am writing to provide you with feedback on your latest performance data. It is great to see that you have consistently achieved your targets and even exceeded them last month. Keep up the good work!\n\nHowever, I would suggest that you focus on improving your product knowledge. This can help you better understand your clients' needs and offer them more suitable products.\n\nHere are two articles that can help you improve your sales skills:\n1. https://www.salesforce.com/blog/2015/04/7-tips-to-boost-your-product-knowledge.html\n2. https://www.business.com/articles/5-ways-to-improve-your-product-knowledge-for-sales/\n\nThank you for your hard work.\n\nBest regards,\nManager" } ] }"""
res = ast.literal_eval(response.replace('\n','\\n'))
st.markdown(res["mails"][0]['mail'])


t = pd.ExcelWriter('test_xlsx')
df = pd.DataFrame.from_dict(res["mails"])
st.dataframe(df)
  # Adjust the path as per your repository structure
csv = df.to_excel(t)
st.download_button(
    label="Download data as Excel",
    data=csv,
    file_name='mail.xlsx',
)
