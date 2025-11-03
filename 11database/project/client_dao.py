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

    @classmethod
    def insert(cls, client):
        conexion = None

        try:
            conexion = Conexion.get_conexion()
            cursor = conexion.cursor()
            values = (client.name, client.last_name, client.membership)
            cursor.execute(cls.INSERT, values)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f'An error ocurred: {e}') 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.clear_conexion(conexion)

    @classmethod
    def update(cls, client):
        conexion = None

        try:
            conexion = Conexion.get_conexion()
            cursor = conexion.cursor()
            values = (client.name, client.last_name, client.membership, client.id)
            cursor.execute(cls.UPDATE, values)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f'An error ocurred: {e}') 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.clear_conexion(conexion)

    @classmethod
    def delete(cls, client):
        conexion = None

        try:
            conexion = Conexion.get_conexion()
            cursor = conexion.cursor()
            values = (client.id,)
            cursor.execute(cls.DELETE, values)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f'An error ocurred: {e}') 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.clear_conexion(conexion)

if __name__ == '__main__':
    
    # insert a client
    # client1 = Client(name='test', last_name='test lastname', membership=123)
    # ClientDAO.insert(client1)

    # update a client
    # client1 = Client(1, name='test update', last_name='test lastname update', membership=333)
    # ClientDAO.update(client1)

    # delete a client
    # client1 = Client(id=1)
    # ClientDAO.delete(client1)

    # select clients
    clients = ClientDAO.select()
    for client in clients:
        print(client)

    