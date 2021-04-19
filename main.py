

import streamlit as st
import tkinter as tk
from tkinter import filedialog
import json
import os

# to make your app take up all the available space in the browser window
# (not just a single column)
#st.set_page_config(layout='wide')

st.title("Title of an app")

html = """

  <style>
    
    /* 1st button */
    .element-container:nth-child(1) {
      left: 500px;
      top: 0px;
    }
    
  </style>
  
"""



dir_details={}
col1, col2 = st.beta_columns(2)

#st.markdown(html, unsafe_allow_html=True)

# this will put a button in the middle column
#with col1:
col1.text("")



if col1.button("DO1"):
    pass
    #if image_file is not None:
     #   st.title(image_file.getvalue())
      #  dir_details={"dirName":image_file.name,"dirType":image_file.type}


    # DO HERE WHAT EVER YOU WANT IF THE FIRST BUTTON CLICKED


#just a way to put spaces between buttons
col1.header("")
col1.text("")
col1.text("")

if col1.button("DO2"):
    #DO HERE WHAT EVER YOU WANT IF THE FIRST BUTTON CLICKED
    pass

#just a way to put spaces between button
col1.text("")
col1.header("")
col1.text("")

if col1.button("DO3"):
    # DO HERE WHAT EVER YOU WANT IF THE FIRST BUTTON CLICKED
    pass






#in "type here..." we can put the response we want to display

col2.text_area("text response",dir_details)


col2.text_area("text response 2","type here...")
uploaded_file = col2.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getbuffer()
    st.write(bytes_data)
col2.text_area("text response 3","type here...")
#st.write("Now on to the other columns")


# this command will make 3 columns of unequal width
# first column is largest and 3x the size of the last,
# second column is 2x the size of the last



# this will put a checkbox in the last column
col4, col5, col6 = st.beta_columns([3,2,1])


# this will put a checkbox in the last column
