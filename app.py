from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Shina"
    relation = "Me"
    age= "14"

    name2 = "Dan Oh"
    relation2 = "Friend"
    age2 = "14"

    name3 = "Taehyung"
    relation3= "Classmate"
    age3 ="15"

    return render_template("index.html", 
                           name= name, relation= relation, age = age,
                           name2 = name2, relation2= relation2, age2= age2,
                           name3= name3, relation3= relation3, age3 = age3,
                           )

app.run(debug=True)