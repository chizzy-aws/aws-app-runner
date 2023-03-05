import streamlit as st
import os
"""
# STREAMLIT ON AWS APP-RUNNER 🏃🏿‍♂️🚢⚓️
"""

with open('apprunner.yaml') as f:
    contents = f.read()
    st.markdown(" The `apprunner.yaml` file contains AWS App Runner configuration.")
    st.code(contents, language='yaml')


