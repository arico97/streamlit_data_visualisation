import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *

st.set_page_config(page_title='CSV Data Visualisation')
st.title('CSV Data Visualisation')
st.subheader('Feed me with your CSV Data')

#remove from original code
df_for_testing = pd.read_csv('./train.csv')

# end
'''
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file:
	st.markdown('...')
	df = pd.read_csv(uploaded_file)
'''

# undo when finish tests
# df_for_testing = df
#end undo
# add time series option
# add different plot options
selected_column = st.selectbox(
	'Select the number of variables you want to plot',
	(1,2,3)
)

fig, ax = plt.subplots()
ax = df_for_testing[selected_column].hist()

st.subheader(f'Graph showing the distribution of {selected_column}')
st.pyplot(fig)


#st.subheader(f'Graph showing the distribution of {selected_column}')
#fig = sns.catplot(df_for_testing,x=selected_column,kind = 'count