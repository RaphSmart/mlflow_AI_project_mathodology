def Predict(X_train, X_test, y_train, y_test):
    lr = LinearRegression()
    model = lr.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

Predict(X_train, X_test, y_train, y_test)
