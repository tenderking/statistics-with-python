

def replace_value_with_grouped_mean(df, value, column, to_groupby):
    """ For a given numeric value (e.g., 0) in a particular column, take the
        mean of column (excluding value) grouped by to_groupby and return that
        column with the value replaced by that mean.

        :param df: The dataframe to operate on.
        :param value: The value in column that should be replaced.
        :param column: The column in which replacements need to be made.
        :param to_groupby: Groupby this variable and take the mean of column.
                           Replace value with the group's mean.
        :returns: The data frame with the invalid values replaced
    """
    invalid_mask = (df[column] == value)

    # get the mean without the invalid value
    means_by_group = (df[~invalid_mask]
        .groupby(to_groupby)[column]
        .mean())

    # get an array of the means for all of the data
    means_array = means_by_group[df[to_groupby].values].values

    # assignt the invalid values to means
    df.loc[invalid_mask, column] = means_array[invalid_mask]

    return df