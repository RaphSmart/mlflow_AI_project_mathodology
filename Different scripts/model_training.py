def training_model(a, b):
    a = data_df.drop(["Car", "Model", "CO2"], axis = 1)
    b = data_df[["CO2"]]
    X_train, X_test, y_train, y_test = train_test_split(a, b, test_size = 0.2)
    print(y_train.shape)
    return X_train, X_test, y_train, y_test
    
X_train, X_test, y_train, y_test = training_model(X, y)
