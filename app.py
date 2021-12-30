from fastai.vision import *
import streamlit as st
import pickle

st.set_page_config(layout="wide")

# CNN = pickle.load(open('convolutional_model.pkl','rb'))

'''
Created on friday Dec 29, 2021 by Sujan Neupane
'''

path = Path('data/genders')
st.title("Gender Classification System")

