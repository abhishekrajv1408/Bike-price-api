from flask import Flask,request,jsonify
from  modle import predict
import pandas as pd

app=Flask(__name__)



@app.route("/",methods=['POST'])
def bike():
    kms=request.form.get('kms')
    age=request.form.get('age')
    power=request.form.get('power')
    brand=request.form.get('brand')
    owner=request.form.get('owner')
    d={'kms_driven':[kms],
       'owner':[owner],
        'age':[age],
        'power':[power],
        'brand':[brand],
       
    }
    data=pd.DataFrame(d)
    result= predict(data)
    result=result.tolist()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
