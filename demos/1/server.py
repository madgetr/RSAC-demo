from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_post():
    if "file" in request.files:
        file = request.files["file"]
        content = file.read().decode("utf-8")
        print(f"Received file content:\n{content}")
    else:
        print(f"Received raw data: {request.data.decode('utf-8')}")

    return "Received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)