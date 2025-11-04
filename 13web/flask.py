from flask import Flask

app = Flas(__name__)

@app.route('/')
def home():
    app.logger.debug('home path')
    return '<p>Hello world</p>'


if __name__ == '__main__':
    app.run(debug=True)