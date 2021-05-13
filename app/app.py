from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':

    with open("./output/file.txt", "w") as f:
       f.write("hello there!!!!")

    app.run(host='0.0.0.0', port=8080)
