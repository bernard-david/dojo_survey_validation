from flask import Flask, render_template, request, redirect
from validate import validate
app = Flask(__name__)
app.secret_key = "lol a secret"

@app.route('/')
def show_form():
    return render_template("index.html")

@ app.route('/result', methods=['POST'])
def result():
    if validate(request.form):
        return render_template("result.html", name_on_template=request.form['name'], language_on_template=request.form['language'], location_on_template=request.form['location'], comment_on_template=request.form['comment'])
    else:
        return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
