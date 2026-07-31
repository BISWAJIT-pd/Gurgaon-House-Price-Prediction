
import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="🏡",
)
st.write("welcome  to my page")
st.sidebar.success("select anything")


from streamlit_lottie import st_lottie
import requests
page_bg = """
<style>

[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1800&q=80");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
background: rgba(255,255,255,0.85);
}

h1,h2,h3,h4,h5,h6,p,div{
color:black;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# -------------------- LOAD LOTTIE --------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_house = load_lottie(
    "https://assets5.lottiefiles.com/packages/lf20_q5pk6p1k.json"
)

# -------------------- LAYOUT --------------------
left, right = st.columns([1.3, 1])

with left:
    st.title("🏡 House Price Prediction System")

    st.markdown("""
### Welcome!

This application allows you to:

✅ Predict House Prices

📊 Explore Data Analysis

📈 View Interactive Visualizations

🏘 Compare Flats & Houses

---

Use the **sidebar** to navigate between pages.
""")

    st.success("Choose a page from the sidebar to get started!")

with right:
    if lottie_house:
        st_lottie(
            lottie_house,
            height=400,
            key="house"
        )

# -------------------- METRICS --------------------
st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Properties", "3000+")

with c2:
    st.metric("Prediction Accuracy", "90%")

with c3:
    st.metric("Locations", "Many")

st.sidebar.success("📌 Select a page above")
