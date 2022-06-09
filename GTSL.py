#import module
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config('Home-Gaurav Transport',initial_sidebar_state= "expanded")

""" # GAURAV TRANSPORT - ePortal for Digital LR, GDN and GRN"""


with st.expander("Driver Section"):
    st.write('This is inside Driver Section')
    
with st.expander("Transporter Section"):
    st.date_input('CN Date')
    st.text_input('Consignment Note Number',value="")
    st.text_input('Consignor Name & Address',value="")
    st.text_input('Consignee Name & Address',value="")
    st.text_input('Vehicle Number')
    st.text_input('Vehicle load capacity')
    st.text_input('Vehicle Type')
    st.radio('Payment Terms',options = ['To Be Billed','To Pay','Paid'], horizontal= True)
    st.radio('GST under RCM payable by',options = ['Consignor','Consignee'], horizontal= True)
    st.button('Submit Details')
    
    
with st.expander("Consignor Section"):
    st.file_uploader('Upload Invoices/Challans/Ewaybill')
    st.camera_input('Capture Material Loaded picture')
  
    st.button('Material loaded and Vehicle released')
    
  
with st.expander("Consignee Section"):

    st.camera_input('Capture Delivered Material picture')
    st.radio('Rate the delivery',options = ['Not Satisfactory','Neutral','Satisfactory'], horizontal= True)
    st.text_area('Remarks if any (optional)')
    st.button('Material Received')

   
st.write("Hello ji")






