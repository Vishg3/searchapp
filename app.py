from flask import Flask,render_template,request,jsonify
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search',methods=['POST','GET'])
def search():
    api_key=request.form.get('APIkey')
    cx=request.form.get('cx')
    query=request.form.get('query')
    url='https://www.googleapis.com/customsearch/v1'
    parameters={
        'key':api_key,
        'cx':cx,
        'q':query
        }
    response=requests.get(url,params=parameters)
    data=response.json()
    items=data.get('items', [])
    return render_template('index.html', items=items)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5002)