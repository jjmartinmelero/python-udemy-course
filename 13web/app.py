from flask import Flask, render_template, redirect, url_for
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


@app.route('/save', methods=['POST'])
def save():
    client = Client()
    client_form = ClientForm(obj=client)
    # print(client_form.errors)

    if client_form.validate_on_submit():
        client_form.populate_obj(client)
        
        if not client.id:
            ClientDAO.insert(client)
        else:
            ClientDAO.update(client)

    return redirect(url_for('home'))

@app.route('/clear')
def clear():
    return redirect(url_for('home'))


@app.route('/edit/<int:id>')
def edit(id):
    client = ClientDAO.select_by_id(id)
    client_form = ClientForm(obj=client)
    clients_db = ClientDAO.select()

    return render_template('index.html', title=title_app, clients=clients_db, client_form=client_form)

@app.route('/delete/<int:id>')
def delete(id):
    client = Client(id)
    ClientDAO.delete(client)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)