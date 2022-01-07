from flask import Flask,render_template, request
import model 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    print(request.method)
    if request.method == 'POST':
        age = request.values.get("age")
        sleep = model.predict(age)
        sleep = round(sleep)


        return render_template('index.html',age = age,sleep = sleep)
        

    return render_template('index.html')




if __name__ =='__main__':
    app.run("PORT",port=3000,debug=True)    