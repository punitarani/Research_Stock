import streamlit as st

from polygon_data import Financials

st.set_page_config(layout="wide")

# Title
st.title('Research Stock')


# Get polygon API Key input
polygon_api_key = st.text_input("Enter Polygon API Key")


# Cache API key
@st.cache(show_spinner=False)
def cache_api_key(api_key):
    return api_key


polygon_api_key = cache_api_key(polygon_api_key)

if not polygon_api_key:
    st.warning("Please Input Polygon API Key")
    st.stop()

# Get ticker input
ticker = st.text_input("Enter Ticker", "AAPL").upper()


# Get financials data
@st.cache(show_spinner=False)
def get_financials(t):
    return Financials(ticker=t, api_key=polygon_api_key).get_financials()


with st.spinner('Getting Financials...'):
    df_financials = get_financials(ticker)

# Display Financials Dataframe
st.subheader('Financials')
st.dataframe(df_financials)

# Plot Financials
metrics = df_financials.index.to_list()
st.subheader('Plot Financials')
metrics_selected = st.multiselect('Metrics', metrics)

if not metrics_selected:
    metrics_selected = ['marketCapitalization']

df_financials_plot = df_financials.copy().loc[metrics_selected].T
st.line_chart(df_financials_plot)
