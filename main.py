from pickle import load
import flask as f
from pandas import DataFrame


app = f.Flask(__name__)
model = load(open("model.pkl","rb"))


@app.route("/")
def home():
    return f.render_template("index.html")


@app.route("/predict",method=["POST"])

def predict():
    A=[]
    for i in f.request.form.values():
        A.append(int(i))
    pred_profit = model.predict(DataFrame([[A[0],A[1]]]))[0][0]
    return f.render_template("index.html",pred = pred_profit)

if __name__=="__main__":
    app.run(debug=True)




