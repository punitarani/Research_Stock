import streamlit as st

from polygon_data import Financials

st.set_page_config(layout="wide")

# Title
st.title('Research Stock')

# Get ticker input
ticker = st.text_input("Enter Ticker", "AAPL")


# Get financials data
@st.cache
def get_financials(t):
    return Financials(ticker=t).get_financials()


df_financials = get_financials(ticker)
metrics = df_financials.index.to_list()

# Display Dataframe
st.subheader('Financials')
st.dataframe(df_financials)
