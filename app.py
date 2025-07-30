from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'MB.web ist online – IBX-MAX aktiviert.'

if __name__ == '__main__':
    app.run()
