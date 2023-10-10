
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plots_variable1 = ('Histogram', 'Boxplot', 'Violin Plot', 'Density plot')
plots_variable2 = ('Line plot', 'Scatter plot', 'Boxplot', 'Stacked area chart', 'Heatmap')
plots_variable3 = ('Bubble chart', '3D scatter plot', '3D surface plot', '3D line plot', '3D heatmap')

dict = {1: plots_variable1, 2: plots_variable2, 3: plots_variable3}

# 1d-function plots
def histo(df):
	fig, ax = plt.subplots()
	ax.hist(df)
	return fig

def boxp(df):
	fig, ax = plt.subplots()
	sns.boxplot(df)
	return fig

def violin(df):
	fig, ax = plt.subplots()
	sns.violinplot(df)
	return fig

def kd(df):
	fig, ax = plt.subplots()
	sns.kdeplot(df)
	return fig




# 2d-function plots
def lp(df,v1,v2):
	fig, ax = plt.subplots()
	ax.plot(df[v1],df[v2])
	return fig

def sc(df,v1,v2):
	fig, ax = plt.subplots()
	ax.scatter(df[v1],df[v2])
	return fig

def boxp2(df,v1,v2):
	fig, ax = plt.subplots()
	sns.boxplot(df,x=v1 ,y=v2)
	return fig

def stck(df,v1,v2):
	fig, ax = plt.subplots()
	ax.stackplot(df[v1],df[v2])
	return fig

def htm(df,v1,v2):
	fig, ax = plt.subplots()
	sns.heatmap(df, annot=True, fmt=".1f")
	return fig

def br_g(df,v1,v2):
	width = 0.35
	fig, ax = plt.subplots()
	rects1 = ax.bar(v1 - width / 2, v2, width, label='Var1')
	rects2 = ax.bar(v1 + width / 2, v2, width, label='Var2')
	ax.legend()
	fig.tight_layout()

# 1-variable plots
one_variable_dict = {
	'Histogram': histo,
	'Violin Plot': violin,
	'Boxplot': boxp,
	'Density plot': kd
}

# 2-variable plots
two_variables_dict = {
	'Scatter plot': sc,
	'Boxplot': boxp2,
	'Line plot': lp,
	# 'Grouped bar chart': br_g,
	'Stacked area chart': stck,
	'Heatmap': htm
}

# 3-variable plots
'''
three_variables_dict = {
	'Bubble chart': plt.scatter,
	'3D scatter plot': ax.scatter3D,
	'3D surface plot': ax.plot_surface(),
	'3D line plot': ax.plot3D(),
	'3D heatmap': ax.plot_surface()
}

'''

var_func_dict ={1:one_variable_dict, 2:two_variables_dict}