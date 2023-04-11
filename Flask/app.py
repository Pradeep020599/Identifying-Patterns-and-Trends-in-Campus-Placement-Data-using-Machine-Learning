from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("rdf.pkl",'rb'))

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/guest', methods = ["POST"])
def Guest():
    return render_template("secondpage.html")

@app.route('/y_predict', methods=["POST"])
def y_predict():
    if request.method == "POST":
        sen1 = request.form["sen1"]
        sen2 = request.form["sen2"]
        sen3 = request.form["sen3"]
        sen4 = request.form["sen4"]
        sen5 = request.form["sen5"]
        sen6 = request.form["sen6"]
        X_test = np.array([[sen1, sen2, sen3, sen4, sen5, sen6]], dtype=float)
        prediction = model.predict(X_test)
        prediction = prediction[0]
        return render_template("secondpage.html", y=prediction)
    else:
        return "Invalid request method"



if __name__ == '__main__':
    app.run(debug=True)
