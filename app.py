import streamlit as st
import pandas as pd
import numpy as np

# Read data
@st.cache
def load_data():
    return pd.DataFrame()

# Initial load of data
df = load_data()

# Define sidebars
st.sidebar.title('Navigation')
pages = st.sidebar.radio('Go to', ['Home', 'Booking', 'Add Data'])

# Define functionality for each page
if pages == 'Home':
    st.title('Welcome to the Tennis Court Booking App')

elif pages == 'Booking':
    st.title('Book a Tennis Court')

    # Show available slots
    st.subheader('Available Slots')
    st.table(df)

    # Booking form
    st.subheader('Book a slot')
    name = st.text_input('Your Name')
    date = st.date_input('Date')
    slot = st.selectbox('Slot', np.arange(24))
    if st.button('Book Slot'):
        # Check if the slot is not already booked
        if not ((df['Date'] == pd.to_datetime(date)) & (df['Slot'] == slot)).any():
            new_row = {'Name': name, 'Date': pd.to_datetime(date), 'Slot': slot}
            df = df.append(new_row, ignore_index=True)
            st.success('Booking Successful')
            st.table(df)
        else:
            st.error('This slot is already booked. Please select another slot.')

elif pages == 'Add Data':
    st.title('Add your own Data')

    # Option to add data manually through text input
    name = st.text_input('Your Name')
    date = st.date_input('Date')
    slot = st.selectbox('Slot', np.arange(24))
    if st.button('Add Data'):
        new_row = {'Name': name, 'Date': pd.to_datetime(date), 'Slot': slot}
        df = df.append(new_row, ignore_index=True)
        st.success('Data added successfully')
        
    # Option to add data using CSV file upload
    file_upload = st.file_uploader("Upload CSV", type=['csv'])
    if file_upload is not None:
        data = pd.read_csv(file_upload)
        df = df.append(data)
        st.success('CSV data added successfully')

# To run the app, save the above code to a file app.py and then execute in command line:
# streamlit run app.py