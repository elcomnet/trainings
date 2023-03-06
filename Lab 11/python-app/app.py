from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Docker Training!'

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')
