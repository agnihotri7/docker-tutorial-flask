from flask import Flask
import os
import socket

app = Flask(__name__)
@app.route("/")

def hello():
    html = "<h3>Hello two {name}!</h3> <b> Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


# conn = psycopg2.connect(
#     host="db",
#     database="suppliers",
#     user="postgres",
#     password="Abcd1234")
