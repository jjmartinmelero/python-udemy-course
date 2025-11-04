from flask import Flask, render_template
from client_dao import ClientDAO

app = Flask(__name__)


title_app = 'GYM APP Python'

@app.route('/')
@app.route('/index.html')
def home():
    app.logger.debug('home path')
    # get clients from db
    clients_db = ClientDAO.select()
    return render_template('index.html', title=title_app, clients=clients_db)


if __name__ == '__main__':
    app.run(debug=True)