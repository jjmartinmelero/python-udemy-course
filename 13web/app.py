from flask import Flask, render_template
from client_dao import ClientDAO
from client import Client
from client_form import ClientForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'


title_app = 'GYM APP Python'

@app.route('/')
@app.route('/index.html')
def home():
    app.logger.debug('home path')
    # get clients from db
    clients_db = ClientDAO.select()
    
    # client form empty
    client = Client()
    client_form = ClientForm(obj=client)
    return render_template('index.html', title=title_app, clients=clients_db, client_form=client_form)


if __name__ == '__main__':
    app.run(debug=True)