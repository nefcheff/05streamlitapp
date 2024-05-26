import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Pinguin Analyser")

# Daten laden
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    return pd.read_csv(url)

data = load_data()

if st.checkbox("Zeige Rohdaten"):
    st.write(data)

chart_type = st.radio(
    "Wähle die Art der Grafik",
    ('Scatterplot', 'Barplot', 'Histogram')
)

x_axis = st.selectbox("Wähle die x-Achse", data.columns)
y_axis = st.selectbox("Wähle die y-Achse", data.columns)

num_rows = st.slider("Anzahl der Zeilen zur Anzeige", min_value=10, max_value=len(data), value=20)
data = data.head(num_rows)

# Grafik erstellen
st.subheader(f"{chart_type} von {x_axis} und {y_axis}")

if chart_type == 'Scatterplot':
    fig = px.scatter(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == 'Barplot':
    fig = px.bar(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == 'Histogram':
    fig = px.histogram(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
