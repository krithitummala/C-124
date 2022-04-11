from flask import Flask, jsonify, request

app = Flask("__name__")
tasks = [
    {
        "id":1,
        "title":"buy groceries",
        "discription":"milk,cheese,pizza,fruits",
        "done": False,

    },
    {
        "id":2,
        "title":"learn python",
        "discription":"need to find a good python tutorial on web",
        "done": False,
    }
]

@app.route("/add-data",methods = ["POST"])

def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data in json format"
        }, 400)
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "discription":request.json.get("discription",""),
        "done": False,
    }

    tasks.append(task)
    return jsonify({
        "status" : "success",
        "message":"Task added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run()