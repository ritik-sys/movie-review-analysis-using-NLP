
from flask import Flask,render_template,request,redirect
import Prediction
from flask import Flask,jsonify,request,make_response,url_for,redirect
import requests, json
import ast

app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")


url = 'https://sentim-api.herokuapp.com/api/v1/'

@app.route('/submit2', methods=['GET','POST'])
def create_row_in_gs():
    
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        path = request.form.get("fname")
        print(path)
        create_row_data = {'text': path}
        #pred = Prediction.get_pred(path)
        response = requests.post(
            url, data=json.dumps(create_row_data),
            headers={'Content-Type': 'application/json','Accept':'application/json'}
        )

        result = response.content
        dict_str = result.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        polarity = mydata["result"]["type"]
        print(polarity)
        if (polarity=='positive'):
            return render_template("result.html",result  ={"path":path,"pred":polarity})
        elif(polarity=='negative'):
            return render_template("negative.html",result  ={"path":path,"pred":polarity})
if __name__ == "__main__":
    app.run(debug=True)