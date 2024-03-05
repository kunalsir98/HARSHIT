from flask import Flask 
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return 'machine learning projects'

if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True)
