import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *

st.set_page_config(page_title='CSV Data Visualisation')
st.title('CSV Data Visualisation')
st.subheader('Feed me with your CSV Data')

# remove from original code
# df_for_testing = pd.read_csv('./train.csv')

# end

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file:
	st.markdown('...')
	df = pd.read_csv(uploaded_file)

# undo when finish tests
# df_for_testing = df
# end undo
# add time series option
# add different plot options
	df_for_testing=df

	n_variables = st.selectbox(
		'Select the number of variables you want to plot',
		(1, 2)
	)

	variables = []

	st.write('Remember that if your data has missing values, the plot may not be displayed.'
	         'Also be careful with the data type and the plot type. ')

	for i in range(n_variables):
		v = st.selectbox(
			'Select the variables you want to plot',
			df_for_testing.columns.values,
			key=i
		)
		variables.append(v)

	func = st.selectbox(
		'Select the plot function that you want to use',
		dict[n_variables]
	)

	f = var_func_dict[n_variables]
	s = f[func]
	t = df_for_testing[variables]

	if n_variables==1:
		st.pyplot(s(t))
	elif n_variables==2:
		st.pyplot(s(t,variables[0],variables[1]))