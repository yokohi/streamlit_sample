import streamlit as st

import seaborn as sns

df = sns.load_dataset("penguins")

st.header("Penguins")
st.write(df)

code = """
import streamlit as st
import pandas as pd
import seaborn as sns
df = sns.load_dataset("penguins")
st.header("Penguins")
st.write(df)
"""
st.code(code)