
import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Plotting demo")
st.title("Price predictor 💰")
import pickle
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = joblib.load(BASE_DIR / "df (1).pkl")
pipeline = joblib.load(BASE_DIR / "pipeline (1).pkl")

print("Model loaded successfully!")
st.header('Enter your inputs')
property_type=st.selectbox('property_type',['flat','house'])
sector=st.selectbox('sector',sorted(df['sector'].unique().tolist()))
bedRoom=float(st.selectbox('bedRooms',sorted(df['bedRoom'].unique().tolist())))
bathroom=float(st.selectbox('bathrooms',sorted(df['bathroom'].unique().tolist())))
balcony=(st.selectbox('balconyies',sorted(df['balcony'].unique().tolist())))
property_Age=(st.selectbox('Prroperty Age',sorted(df['agePossession'].unique().tolist())))
built_up_area=float(st.number_input('BUILT_UP AREA'))
servant_room=float(st.selectbox('Servant room',[0.0,1.0]))
store_room=float(st.selectbox('Store room',[0.0,1.0]))
furnishing_type=(st.selectbox('Furnishing_type',sorted(df['furnishing_type'].unique().tolist())))
luxury_category=(st.selectbox('Luxury_category',sorted(df['luxury_category'].unique().tolist())))
floor_category=(st.selectbox('Floor_category',sorted(df['floor_category'].unique().tolist())))
if st.button('Predict'):
    #form a DF then predict then display
    data = [[property_type, sector, bedRoom, bathroom, balcony, property_Age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)
    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price-0.22
    high=base_price+0.22
    st.text('The price of the flat in between around {} and {} cr'.format(round(low,2),round(high,2)))
