import streamlit
import pandas as pd
streamlit.title('My new healthy dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥑 Omega 3 & Blueberry Outmeal🍇')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie🥛')
streamlit.text('🥚Hard-Boiled Free-Range Egg🥚')

my_list_of_csv = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_list_of_scv 
streamlit.dataframe(my_list_of_scv)
