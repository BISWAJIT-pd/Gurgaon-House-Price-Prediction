
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
st.set_page_config(page_title="Recommender")

st.title('Select Location and Radius')
location_s=st.selectbox('Select Location',sorted(location_df.columns.tolist()))
radius=st.number_input('Radius in Kilomiteres')
if st.button('Search'):
    x=location_df[location_df[location_s]<radius*1000][location_s].sort_values().to_dict()
    for i,j in x.items():
        st.text(str(i)+' '+str(round(j/1000))+'km')

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

location_df = joblib.load(
    BASE_DIR / "dataset" / "location_distancea_df.joblib"
)

cosine_sim1 = joblib.load(
    BASE_DIR / "dataset" / "cosine_sim1.joblib"
)

cosine_sim2 = joblib.load(
    BASE_DIR / "dataset" / "cosine_sim2.joblib"
)

cosine_sim3 = joblib.load(
    BASE_DIR / "dataset" / "cosine_sim3.joblib"
)


def recommend_properties_with_scores(property_name, top_n=5):

    cosine_sim_matrix = 0.5*cosine_sim1 +0.8*cosine_sim2 + 1*cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    top_properties = location_df.index[top_indices].tolist()
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df

st.title('Recommended Appartments')
selected=st.selectbox('Select ab apartment',sorted(location_df.index.tolist()))
if st.button('Recommended'):
    r=recommend_properties_with_scores(selected)
    st.dataframe(r)
