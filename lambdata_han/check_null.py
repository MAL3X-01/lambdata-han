import pandas as pd
import numpy as np


def check_null(df):
	"""
	Checking for null values and return a boolean and the total number of nulls
	for each row label.

	Parameters:
	===========

	Output:
	=======
	: boolean. 
	: pd.DataFrame reporting total number of NaNs in each column.
	"""
	if df.isnull().values.any():
		return True, df.isnull().sum()
	else:
        return False, df.isnull().sum()
