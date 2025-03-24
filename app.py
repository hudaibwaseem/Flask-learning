from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':"Software Developer",
        'company':"Google",
        'location':"Mountain View, CA",
        'salary': 100000
    },
    {
        'id':2,
        'title':"Data Scientist",
        'company':'ABC' ,
        'location':"karqachi Pakistan",
    },
    {
        'id':3,
        'title':"AI Engineer",
        'company':"X",
        'location':"America",
        'salary': 105000
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS,company_name="hudaib"
)

@app.route("/jobs")
def get_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)