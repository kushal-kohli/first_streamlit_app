import streamlit
import pandas
streamlit.title('My Parent New healthy Dinner')
streamlit.header('🥣 Breakfast menu')
streamlit.text('🥗 Omega3 and Blueberry Oat meal')
streamlit.text('🥑Kale pinach and Rocket smoothie')
streamlit.text('🐔 Hard boiled egg-free range eggs')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)


