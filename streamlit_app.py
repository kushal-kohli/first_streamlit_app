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
streamlit.dataframe(my_fruit_list)
