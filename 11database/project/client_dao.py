from conexion import Conexion
from client import Client


class ClientDAO:

    SELECT = 'SELECT * FROM customers ORDER BY id'
    INSERT = 'INSERT INTO customers(name, last_name, membership) VALUES (%s, %s, %s)'
    UPDATE = 'UPDATE customers SET name=%s, last_name=%s, membership=%s WHERE id=%s'
    DELETE = 'DELETE FROM customers WHERE id=%s'

    @classmethod
    def select(cls):
        conexion = None
        try:
            conexion = Conexion.get_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECT)
            results = cursor.fetchall()
            print(results)
            clients = []
            for result in results:
                client = Client(result[0], result[1], result[2], result[3])
                clients.append(client)
            
            return clients
        except Exception as e:
            print(f'An error ocurred: {e}') 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.clear_conexion(conexion)

if __name__ == '__main__':
    clients = ClientDAO.select()
    for client in clients:
        print(client)