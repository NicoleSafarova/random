import json
from random import randint

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/member')
def index():
    with open('templates/n.json') as file:
        f = file.read()
        data = json.loads(f)
    n1 = randint(0, len(data) - 1)
    return render_template('index.html', data=data[n1])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')