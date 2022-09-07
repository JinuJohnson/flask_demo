import joblib as jb
from flask import Flask, render_template, request
import numpy as np

app= Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    TSH=(request.form['TSH'])
    FTI=(request.form['FTI'])
    TT4=(request.form['TT4'])
    T3=(request.form['T3'])
    query_hypothyroid=(request.form['query_hypothyroid'])
    on_thyroxine=(request.form['on_thyroxine'])
    sex=(request.form['sex'])
    pregnant=(request.form['pregnant'])
    psych=(request.form['psych'])

    arr=np.array([[TSH,FTI,TT4,T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])

    model=jb.load('model_RandomForest.pkl')
    result= model.predict(arr)
    if result ==1 :
        return render_template('after.html',data='Your values are abnormal and positive for thyroid disorder')
    else:
        return render_template('after.html',data='Your values are normal')
    
if __name__ == '__main__':
    app.run()






