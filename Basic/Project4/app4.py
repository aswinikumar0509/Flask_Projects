from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():

    if request.method=='POST':
        First_Name = request.form['First_Name']
        Last_Name =  request.form['Last_Name']
        Age = request.form['Age']
        Gender = request.form['Gender']

        return render_template('result.html',First_Name=First_Name, Last_Name = Last_Name, Age = Age, Gender =Gender )
    return render_template('index.html')

if __name__=='__main__':
    app.run()