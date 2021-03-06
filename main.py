from flask import Flask, request
from caesar import rotate_string 

app = Flask(__name__)
app.config['DEBUG'] = True

DF = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

    <form action="index.html" method="post">
      <label for ="name">Rot:</label>
      <input id="number" type="number" value="0">
      <label for="comment">Comment:</label>
      <textarea name="text">{}</textarea>
      <button type="submit">Submit Comment</button>
    </form>

    </body>
</html>"""

app.run()


def encrypt():
    rot = int(request.form["number"])
    text = request.form["text"] 
    return rotate_string(rot,text)


@app.route('/', methods=['POST'])

@app.route('/')
def index():
    return DF

