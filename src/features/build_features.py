

import numpy as np


def replace_value_with_grouped_mean(data):
  """
  Replaces missing values (NaN) in each column of a NumPy array with the column mean.

  Args:
      data: A NumPy array of any dimension.

  Returns:
      A new NumPy array with missing values replaced by the column mean.
  """
  mu1 = (data.dropna()).mean()
  print(mu1)
  result = data.apply(lambda x: x.fillna((mu1), axis=0))
  print(result)
  return result

def explore_data(df):
    """ Print out the shape of the dataframe, the first few rows, last rows and the
        data types of the columns.
        Describe the data frame.
        If missing values are present, print out the percentage of missing values

        :param df: The dataframe to explore
    """
    print(f"Shape: {df.shape}")
    print(f"Head: {df.head()}")
    print(f"Tail: {df.tail()}")
    print(f"Description: {df.describe()}")
    print(f"Data Types: {df.dtypes}")


    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        print(f"Missing Values: {missing / len(df)}")

