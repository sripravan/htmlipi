from flask import Flask
import requests

from templates import gallery

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = requests.get("https://picsum.photos/v2/list")
    images = response.json()
    return gallery.render({"images": images})