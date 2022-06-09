#import module
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config('Home-Gaurav Transport',initial_sidebar_state= "expanded")
st.title('GAURAV TRANSPORT')
st.subheader('LR | GDN | GRN e-portal')

userType = st.radio('You are ',options = ['Truck Driver','Transporter','Consignor','Consignee'], horizontal= True)

if userType == 'Truck Driver':
    st.text_input('Enter your current location',value="")
    st.button('Update Status')
    st.text('Gaurav Transport 24/7 helpline:  +91 8600852256')

    
if userType == 'Transporter':
    st.date_input('CN Date')
    st.text_input('Consignment Note Number',value="")
    st.text_input('Consignor Name & Address',value="")
    st.text_input('Consignee Name & Address',value="")
    st.text_input('Driver Name',value="")
    st.text_input('Driver Contact Number',value="")
    st.text_input('Vehicle Number')
    st.text_input('Vehicle load capacity')
    st.text_input('Vehicle Type')
    st.radio('Payment Terms',options = ['To Be Billed','To Pay','Paid'], horizontal= True)
    st.radio('Invoice and GST under RCM payable by',options = ['Consignor','Consignee'], horizontal= True)
    st.button('Submit Details')

if userType == 'Consignor':
    st.file_uploader('Upload Invoices/Challans/Ewaybill',accept_multiple_files= True)
    st.camera_input('Capture picture of loaded Vehicle')
    st.button('Material loaded and Vehicle released')

if userType == 'Consignee':    
    st.camera_input('Capture Delivered Material picture')
    st.radio('Rate the delivery',options = ['Not Satisfactory','Neutral','Satisfactory'], horizontal= True)
    st.text_area('Remarks if any (optional)')
    st.button('Material Received')





