import pandas as pd
import numpy as np

def add_series(df, lst, col_name="new_col"):
	"""
	Add a list into pandas dataframe as a new column.

	Parameters:
	===========
	df: the target dataframe to get a new column from the lsit
	lst: the list to be added to the dataframe
	col_name: optional. name of the new column

	Output:
	=======
	df_out: the dataframe with a lst added to the df.
	"""

	if not df.shape[0] == len(lst):
		raise Exception("Size mismatch")

	df_out = df.copy()
	df_out[col_name] = lst
	
	return df
