from flask import Flask,render_template,url_for,request,jsonify
import joblib
model = joblib.load('KMeans_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input_page')
def input_page():
    return render_template('input_page.html')

@app.route('/predicted_page',methods=['GET','POST'])
def predicted_page():
    if request.method == 'POST':

        K = request.form["K"]
        N = int(request.form["N"])
        P = int(request.form["P"])
        temprature = int(request.form["temprature"])
        ph = int(request.form["ph"])
        humidity = int(request.form["humidity"])
        rainfall = int(request.form["rainfall"])

        user_data = [[K,N,P,temprature,humidity,ph,rainfall]]
        
        pred = model.predict(user_data)[0]
        return render_template('predicted_page.html',output = str(pred))


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=2525,debug=True) 
