from flask import Flask,render_template

app = Flask(__name__)

projects=[
    {"title":"Python coding","link":"https://github.com/YashfaRubab/Python_Programs"},{"title":"C-Coding","link":"https://github.com/YashfaRubab/C_Codes"}
    ]


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html",projects=projects)

app.run(debug=True)