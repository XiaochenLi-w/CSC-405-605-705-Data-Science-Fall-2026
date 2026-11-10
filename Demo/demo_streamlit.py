import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Add title and subtitle of the map.
st.title("Accidents in United Kingdom")
st.markdown("This report analyzes accident data in United Kingdom from 2012-2014")
st.write("This report analyzes accident data in United Kingdom from 2012-2014")


@st.cache_data
def load_data(uploaded_file, nrows):

    data = pd.read_csv(uploaded_file, nrows = nrows, parse_dates =[['Date', 'Time']])
    data.rename(columns ={"date_time": "date / time"}, inplace = True)
        
    data.dropna(subset =['Latitude', 'Longitude'], inplace = True)

    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis ="columns", inplace = True)
    
    return data
    #return pd.read_csv(file)

uploaded_file = st.file_uploader("Upload your CSV dataset", 
                                max_upload_size=150, 
                                accept_multiple_files=False, 
                                type="csv"
                                )

if uploaded_file is not None:
    data = load_data(uploaded_file, 10000)
    st.write(data)


st.header("Where are the most people casualties in accidents in UK?")
st.subheader("Where are the most people casualties in accidents in UK?")

st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")

casualties = st.slider("Number of persons died", 1, int(data["number_of_casualties"].max()))
st.map(data.query("number_of_casualties >= @casualties")[["latitude", "longitude"]])

fig, ax = plt.subplots(figsize=(8,6))

corr = data[['accident_severity', 'number_of_vehicles', 'number_of_casualties', 'day_of_week']].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)