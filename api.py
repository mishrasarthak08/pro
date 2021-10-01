from flask import Flask,request,jsonify
app = Flask(__name__)

tasks = [
    {
        "id":1,
        "name":u"Rahul",
        "contact":u"9893390984",
        "done":False
    },
    {
        "id":2,
        "name":u"sarthak",
        "contact":u"8435534855",
        "done":False
    }
]

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400
        
        )
    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)