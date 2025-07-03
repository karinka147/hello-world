from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
    <head><title>Hello World</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Hello World!</h1>
        <p>Moja pierwsza aplikacja w Pythonie na Azure!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
