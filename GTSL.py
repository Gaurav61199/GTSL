#import module
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
import streamlit as st
from google.cloud import firestore


# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")




st.set_page_config('Home-Gaurav Transport',initial_sidebar_state= "expanded")
st.caption('GAURAV TRANSPORT')
st.title('LR | GDN | GRN e-portal')

if 'flg_material_receipt' not in st.session_state:
    st.session_state.flg_material_receipt = False



userType = st.radio('You are ',options = ['Truck Driver','Transporter','Consignor','Consignee'], horizontal= True)
#col1, col2 = st.columns(2)


if userType == 'Truck Driver':
    if st.session_state.flg_material_receipt == True:
        st.subheader('Please share your feedback and Experience')
        st.radio('Had meal during transit?',options = ['Yes','No'], horizontal= True)
        st.radio('Did you have enough sleep during the transit?',options = ['Yes','No'], horizontal= True)
        st.select_slider('Rate your Experience at Consignor',options=['Not-Satisfactory','Neutral','Satisfactory'])
        st.select_slider('Rate your Experience at Consignee',options=['Not-Satisfactory','Neutral','Satisfactory'])
        st.text_area('Comments if any (optional)')
        st.button('Submit')
     
        
    else:        
        st.text_input('Enter your current location',value="")
        st.button('Update Status')
        st.text('Gaurav Transport 24/7 helpline:  +91 8600852256')
    

    

if userType == 'Transporter':
    #with col1:
   
        with st.expander("Create New LR"):
            with st.form('CreateLR',clear_on_submit=True):
                #retriving last LR Number and adding 1 to it to generate new LR
                doc_ref = db.collection("SEQ").document("LRSEQ")
                newLrNumber = doc_ref.get().to_dict()["LRSEQ"] + 1 
                doc_ref.set({"LRSEQ":newLrNumber})
                
                cnDate = st.date_input('CN Date')
                cnNo = st.text('Consignment Note Number: ' + str(newLrNumber) )
                consignorName=st.text_input('Consignor Name',value="")
                consignorAddress =st.text_area('Consignor Address',value="")
                consigneeName=st.text_input('Consignee Name & Address',value="")
                consigneeAddress=st.text_area('Consignee Address',value="")
                pickupCity = st.text_input('Pickup City',value="")
                dropCity = st.text_input('Drop City',value="")
                driverName = st.text_input('Driver Name',value="")
                driverContactNumber= st.text_input('Driver Contact Number',value="")
                vehicleNumber=st.text_input('Vehicle Number')
                vehicleLoadCapacity=st.text_input('Vehicle load capacity in MT')
                vehicleType=st.text_input('Vehicle Type')
                route =st.text_input('Route (for eg.   Pune--Panvel--Mumbai--Ahmedabad)')
                paymentTerm=st.radio('Payment Terms',options = ['To Be Billed','To Pay','Paid'], horizontal= True)
                invGstPayableBy=st.radio('Invoice and GST under RCM payable by',options = ['Consignor','Consignee'], horizontal= True)
                lrsubmit = st.form_submit_button("Create LR")
             
            
        if lrsubmit:
            doc_ref = db.collection("LR").document(str(cnNo))
            doc_ref.set({
            "CN Date": cnDate.strftime("%d/%m/%Y"),
            "CN Number": cnNo,
            "Consignor Name": consignorName,
            "Consignor Address" : consignorAddress,
            "Consignee Name" : consigneeName,
            "Consignee Address" : consigneeAddress,
            "Pickup City": pickupCity,
            "Drop City": dropCity,
            "Driver Name" : driverName,
            "Driver Contact Number" : driverContactNumber,
            "Vehicle Number" : vehicleNumber,
            "Vehicle Laod Capacity" : vehicleLoadCapacity,
            "Vehicle Type" : vehicleType,   
            "Route" :route,
            "Payment Term":paymentTerm,
            "Invoice and GST payable by" :invGstPayableBy 
                 
            })
            
            
    #with col2 :
        with st.expander("Edit LR"):
            st.text_input('LR Number')
            st.button('Edit')

if userType == 'Consignor':
    st.file_uploader('Upload Invoices/Challans/Ewaybill',accept_multiple_files= True)
    st.camera_input('Capture picture of loaded Vehicle')
    st.button('Material loaded and Vehicle released')




if userType == 'Consignee':    
    st.camera_input('Capture delivered material picture')
    st.radio('Rate the delivery by Gaurav Transport',options = ['Not Satisfactory','Neutral','Satisfactory'], horizontal= True)
    st.text_area('Remarks if any (optional)')
    st.session_state.flg_material_receipt = st.button('Material Received')
    
    
  


