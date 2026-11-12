import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)

st.title("AI-assistant Data Science Report")

st.write("This is an example Data Science Report.")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    max_upload_size=150,
    type = "csv"
)

if uploaded_file is not None:
    data = load_data(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(data.head())

    summary = f"""
    Dataset shape: 
    {data.shape}

    Columns:
    {data.dtypes}

    Missing Values:
    {data.isnull().sum()}

    Basic statistics:
    {data.describe(include='all').transpose()}

    """

st.write(data.describe(include='all').transpose())  

if "overview" not in st.session_state:
    st.session_state.overview = None

if st.session_state.overview is None:

    prompt = f"""
    You are a data analyst.

    Analyze the following dataset summary and give:
    1. Data quality assessment
    2. Key insights
    3. Possible use cases
    4. Risks or issues

    Dataset:
    {summary}
    """
    response = llm.invoke(prompt)

    st.session_state.overview = response.content


st.subheader("AI Analysis Overview")
st.write(st.session_state.overview)

st.header("Data Cleaning")

if "EDA_figure" not in st.session_state:
    st.session_state.EDA_figure = None

if st.session_state.EDA_figure is None:

    prompt = f"""
    You are a senior data scientist.

    Dataset Summary:

    {summary}
    
    My research question is which attribute has the strongest association with the label.
    Please return a JASON object describing which EDA plots should be generated.

    For each plot, include:
    - plot_type
    - columns
    - reason

    Only return JSON
"""
    response = llm.invoke(prompt)
    st.session_state.EDA_figure = response.content

st.subheader("AI Suggested Plot")
st.write(st.session_state.EDA_figure)

if "EDA_figure_code" not in st.session_state:
    st.session_state.EDA_figure_code = None

if st.session_state.EDA_figure_code is None:
    prompt = f"""
        You are an expert Python data visualization assistant.

        Dataset Summary:
    
        {summary}
        
        Write clear, executable Python code using Matplotlib and Seaborn to create one figure containing exactly two subplots.

        I will provide:
        1. A pandas DataFrame named `data`
        2. A JSON specification describing the two subplots

        Requirements:
        - Use `matplotlib.pyplot` and `seaborn`.
        - Create exactly two subplots in one figure.
        - Use only columns that exist in `data`. Do not invent column names or data.
        - If a required column or setting is missing or invalid, add a short Python comment identifying the issue and use a reasonable fallback.

        <json_specification>
        [
        {{
            "plot_type": "scatterplot",
            "columns": ["children", "label"],
            }},
        {{
            "plot_type": "boxplot",
            "columns": ["sex", "label"],
            }}
        ]
        </json_specification>
    """

    response = llm.invoke(prompt)
    st.session_state.EDA_figure_code = response.content

st.subheader("AI Suggested Plot code")
st.write(st.session_state.EDA_figure_code)


# AI code execution

# Create a dummy DataFrame for demonstration purposes,

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Data Visualization', fontsize=16)

# Subplot 1: scatterplot
# Check if 'children' and 'label' columns exist
if 'children' in data.columns and 'label' in data.columns:
    sns.scatterplot(x='children', y='label', data=data, ax=axes[0])
    axes[0].set_title('Scatter Plot of Children vs. Label')
    axes[0].set_xlabel('Number of Children')
    axes[0].set_ylabel('Label')
else:
    # Fallback if columns are missing
    axes[0].text(0.5, 0.5, "Required columns 'children' or 'label' for scatterplot not found.",
                 horizontalalignment='center', verticalalignment='center', transform=axes[0].transAxes)
    axes[0].set_title('Scatter Plot (Columns Missing)')

# Subplot 2: boxplot
# Check if 'sex' and 'label' columns exist
if 'sex' in data.columns and 'label' in data.columns:
    sns.boxplot(x='sex', y='label', data=data, ax=axes[1])
    axes[1].set_title('Box Plot of Label by Sex')
    axes[1].set_xlabel('Sex')
    axes[1].set_ylabel('Label')
else:
    # Fallback if columns are missing
    axes[1].text(0.5, 0.5, "Required columns 'sex' or 'label' for boxplot not found.",
                 horizontalalignment='center', verticalalignment='center', transform=axes[1].transAxes)
    axes[1].set_title('Box Plot (Columns Missing)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
# plt.show()

st.pyplot(fig)


@st.cache_data
def steps_eda():
    steps_eda = llm.invoke('What are the steps of EDA? Please provide a concise answer')
    return steps_eda.content

# sidebar
with st.sidebar:
    st.write('What are the steps of EDA')
    st.write(steps_eda())