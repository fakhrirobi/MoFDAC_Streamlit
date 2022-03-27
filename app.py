# 1ST Import all required packages 
from pyroapi import optim
import streamlit as st 
import pandas as pd 
from  st_aggrid import AgGrid
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

st.set_option('deprecation.showPyplotGlobalUse', False)
#Create Basic Apperance of the web 
st.title('Welcome to MOFDAC Streamlit App : ')



#how to run the scipt ? 
# you can use streamlit run <your python file name>.py e.g. streamlit run app.py 
# or python -m streamlit run app.py


# Display Component 
# st.image('contoh_gambar.jpg')

st.caption('Building Image')

#display dataframe using diabetes dataset 

data = pd.read_csv('diabetes.csv')
with st.expander('Data Display') : 
    # #directly show dataframe 
    st.write('directly show dataframe ')
    data
    # #using st.table
    st.write('Display DataFrame using table')
    st.table(data=data)


    # #using st.table
    # st.write('Display DataFrame using st.dataframe()')
    # st.dataframe(data=data)

    #alternative using st.AgGrid  pip install streamlit-aggrid
    #using st.aggrid 
    st.write('AgGrid')
    AgGrid(data)


#chart element 
with st.expander('Chart Element : ') : 
    st.write('Matplotlib Chart Element : ') 

    plt.scatter(x=data['Glucose'],y=data['BloodPressure'])
    fig  = plt.show()
    st.pyplot(fig)

    figure = go.Figure()

    figure.add_trace(go.Scatter(x=data['Glucose'],y=data['BloodPressure']))



    st.plotly_chart(figure)                 

#Adding Input Widget st.text_input mirip st.num_input
with st.expander('Input Element') :
    input_1 = st.text_input('Please input any words')
    if input_1 : 
        st.success(f'Output of text box above : {input_1}')
        
    #
    st.write('Example Button')
    button_1 = st.button('Press to Turn Camera')
    if button_1 : 
        capture = st.camera_input('Camera Box')
        
    file_uploaded = st.file_uploader('Upload .csv files ')
    if file_uploaded : 
        st.success('successfully upload the data')
        uploaded_data = pd.read_csv(file_uploaded)# new
        show_btn = st.button('Show Uploaded Data')
        if show_btn : 
            st.dataframe(uploaded_data)
#Layout
#adding sidebar 
radio_button_sidebar = st.sidebar.radio('Click Menus to Show : ',options=['1.Data Viz','2.Modelling'])
with st.sidebar.container() : 
    st.header('This is sidebar')

if radio_button_sidebar == '1.Data Viz' : 
    st.info('You Clicked Data Viz Menu !') 
    # viz_data = pd.read_csv('diabetes.csv')
    # AgGrid(viz_data,key=545)


#adding checkbox
sidebar_checkbox = st.sidebar.multiselect('Mark columns  your wish/es : ',options=[x for x in data.columns])

if sidebar_checkbox and radio_button_sidebar == '1.Data Viz' : 
    st.info(f'You choosed Columns{sidebar_checkbox}')
    AgGrid(data[sidebar_checkbox],key=256)
    
    
#column implementation 

with st.expander('Trial Expander') : 
    st.write('Example of Expander')
st.write('Columns Example')
col_1,col_2 = st.columns(2)

col_1.write('This Is Columns 1')    
col_2.write('This Is Columns 2')    

# FORM INPUT 
st.write('FORM EXAMPLE')
with st.form("Form Prediction"):
    num = st.number_input("Input Any Number ")
    text = st.text_input("Input Any tEXT ")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success('Successfully submit the form')
        st.write('form values : ')
        st.write(" NUMBER : ", num, "TEXT : ", text)

