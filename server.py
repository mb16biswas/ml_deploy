from flask import Flask , render_template  , request 
import numpy as np 
import pickle 
model = pickle.load(open('boston_model.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def body():
    return render_template("index.html")

@app.route("/home" , methods = ["post"])
def home():
    int_fea = [float(x) for x in request.form.values()]
    int_fea = [np.array(int_fea)]
    pred = model.predict(int_fea)
    print("prerds "  , pred)

    return render_template('index.html', pred='house price ..... $ {}'.format(pred))



if __name__ == "main" :
    app.run(debug= True)



# flask run