from flask import Flask, render_template, request
from csp import *
import csp
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('submit.html')  # Update to use 'w_details.html'

@app.route('/', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        equipment = str(request.form['equip'])
        body_part = str(request.form['body'])
        workout_time = int(request.form['wt'])
        difficulty = int(request.form['diff']) 
        calories = int(request.form['cal']) 
        best1=csp.calculate_best_exercise(equipment,workout_time,difficulty,calories,body_part,i,variables)
        best1.sort(reverse=True)
        best=best1[:5]
        print(best)
       
        return render_template("single_final.html",ex1=best[0][1].capitalize(),ex2=best[1][1].capitalize(),ex3=best[2][1].capitalize(),ex4=best[3][1].capitalize(),ex5=best[4][1].capitalize())

      

    

if __name__ == '__main__':
    app.run(debug=True)
