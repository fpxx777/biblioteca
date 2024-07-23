from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! POST'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)