def data_preparation(data_df):
    X = data_df.drop(["Car", "Model", "CO2"], axis = 1)
    y = data_df[["CO2"]]
    return X, y

X, y = data_preparation(data_df)
