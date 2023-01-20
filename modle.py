

def predict(data):
    import pandas as pd 
    df=pd.read_csv('Used_Bikes.csv')
    data1=df.drop("bike_name",axis=1)
    data1.drop("city", axis=1,inplace=True)
    data1.replace(to_replace=["First Owner","Second Owner","Third Owner","Fourth Owner Or More"],value=[1,2,2,2],inplace=True)
    data1.replace(to_replace=["Bajaj","Hero","Royal Enfield","Yamaha","Honda","Suzuki","TVS","KTM","Harley-Davidson","Kawasaki","Hyosung","Benelli","Mahindra","Triumph","Ducati","BMW","Jawa","MV","Indian","Ideal","Rajdoot","LML","Yezdi"],value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],inplace=True)
    data.replace(to_replace=[1,2,3,4], value=[1,2,2,2],inplace=True)
    x=data1.drop("price",axis=1)
    y=data1.price
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=3/4,random_state=21)
    from sklearn.linear_model import LinearRegression
    model=LinearRegression()
    model.fit(x_train,y_train)
    pre=model.predict(data)
    return pre