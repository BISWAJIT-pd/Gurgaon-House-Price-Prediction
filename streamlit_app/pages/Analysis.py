import streamlit as st
st.set_page_config(page_title="Visulaiziation demo")
st.title("Analysis Module")
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
new_df = pd.read_csv(BASE_DIR / 'dataset' / 'data_viz1.csv')
feature_text = joblib.load("dataset/feature_text.pkl")
group_df = new_df.groupby('sector')[
    ['price','price_per_sqft','built_up_area','latitude','longitude']
].mean()
st.header('Sector PRICE_per_squarefit map')
fig=px.scatter_mapbox(
    group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
    mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index
)
st.plotly_chart(fig,use_container_width=True)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.header('Features Wordcloud')
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

st.title('Area vs Price')
property_type=st.selectbox('Select Property Type',['flat','house'])
if (property_type=='house'):
    fig1 = px.scatter(
        new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price"
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(
        new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price"
    )
    st.plotly_chart(fig1, use_container_width=True)

st.header("BHK Pie Chart")

selected_sector = st.selectbox(
    "Select Sector",
    sorted(new_df["sector"].unique())
)
fig2 = px.pie(
    new_df[new_df["sector"] == selected_sector],
    names="bedRoom",
    title=f"BHK Distribution in {selected_sector}"
)
st.plotly_chart(fig2, use_container_width=True)

st.header('Side by side BHK price comparison')
fig3 = px.box(new_df[new_df['bedRoom']<=4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)

import seaborn as sns
fig3, ax = plt.subplots(figsize=(8,5))
sns.distplot(
    new_df[new_df['property_type'] == 'house']['price'],
    hist=False,
    kde=True,
    label='House',
    ax=ax
)
sns.distplot(
    new_df[new_df['property_type'] == 'flat']['price'],
    hist=False,
    kde=True,
    label='Flat',
    ax=ax
)
ax.set_title("Price Distribution")
ax.set_xlabel("Price")
ax.legend()
st.pyplot(fig3)
