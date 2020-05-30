from flask import Flask, render_template, flash, redirect, request
from forms import BmiForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/home', methods=['GET','POST'])
def index():
    b=0
    w=0
    h=0
    form  = BmiForm()
    if request.method == 'POST':
        w = request.form['weight']
        h = request.form['height']
        if form.validate_on_submit():
            b = int(w)/(float(h)*float(h))
            flash(f'BMI for {h} and {w} is {b} kg/m^2')
            return redirect('/home')
    return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)