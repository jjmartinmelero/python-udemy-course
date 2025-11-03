from client_dao import ClientDAO
from client import Client
print('********************** APP **********************')

option = None

while option != 5:
    print(f'''Menu:
    1. Client list
    2. Add Client
    3. Update Client
    4. Delete client
    5. Exit
''')
    option = int(input('Select an option: '))
    if option == 1:
        clients = ClientDAO.select()
        print('\n Client list: ')
        for client in clients:
            print(client)
    elif option == 2:
        client_name = input('Client name: ')
        client_last_name = input('Client last name: ')
        client_membership = input('Client membership: ')
        client = Client(name=client_name, last_name=client_last_name, membership=client_membership)

        clients_insert = ClientDAO.insert(client)
        print(f'Client inserts: {clients_insert}')
    elif option == 3:
        client_id = int(input('Select an client id to update: '))
        client_name = input('Client name: ')
        client_last_name = input('Client last name: ')
        client_membership = input('Client membership: ')

        clients_updated = ClientDAO.update(Client(client_id, client_name, client_last_name, client_membership))
        print(f'Client updated: {clients_updated}')
    elif option == 4:
        client_id = int(input('Select an client id to update: '))
        
        clients_deleted = ClientDAO.delete(Client(client_id))
        print(f'Client deleted: {clients_deleted}')