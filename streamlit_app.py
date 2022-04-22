import streamlit
import pandas as pd
streamlit.title('My new healthy dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥑 Omega 3 & Blueberry Outmeal🍇')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie🥛')
streamlit.text('🥚Hard-Boiled Free-Range Egg🥚')

# my_list_of_csv = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_list_of_scv 
# streamlit.dataframe(my_list_of_scv)

streamlit.header('🍉🍒Build your own fruit smoothie🍓🍊')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
"""
streamlit.multiselect('Pick some fruits:', list(my_fruit_list['Fruit']))
my_fruit_list

"""

my_fruit_list = my_fruit_list.set_index('Fruit')
"""
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
"""
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_show)
