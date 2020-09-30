

import streamlit as st
import plotly as py
import plotly.io as pio
from plotly import graph_objects as go
from passlib.hash import pbkdf2_sha256
import pandas as pd



# Loading the Dataset
user_df = pd.read_csv('user_credentials.csv')
user_df = user_df[['Username','Password']]

def main():
    
    st.beta_set_page_config(page_title="SML Dashboard", page_icon=None, layout='wide', initial_sidebar_state='auto')
    st.title("Social Media Listening Dashboard")
    st.sidebar.title("Login page")

    st.markdown("This application is a Streamlit dashboard used "
                "for Social Media Listening")
    st.sidebar.markdown("Please select Login and enter username & password")

    st.header("Login Status")

    menu = ["Home","Login"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.info("To access the dashboard select the login option in the sidebar")

    elif choice == "Login":

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            
            known_hash = user_df['Password'][user_df['Username']== username].iloc[0]
            if pbkdf2_sha256.verify(password,known_hash):
                # the above line returns True or False. If True is returned, we show the main dashboard
                st.success("Logged in as {}".format(username))

                labels =  ["People who like streamlit", "People who don't know about streamlit"]
                values = [80, 20]


                # pull is given as a fraction of the pie radius
                fig = go.Figure(data=[go.Pie(labels=labels, values=values,textinfo='label+percent',
                                             insidetextorientation='radial', pull=[0, 0, 0.2, 0] #,hole = 0.2
                                            )])


                fig.update_layout(
                    title_text="Demo streamlit app")


                st.plotly_chart(fig, sharing='streamlit')

            else:
                st.warning("Incorrect Username/Password")
                
if __name__ == '__main__':
    main()




