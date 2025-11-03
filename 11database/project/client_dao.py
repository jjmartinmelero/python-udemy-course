class ClientDAO:

    SELECT = 'SELECT * FROM clients order id'
    INSERT = 'INSERT INTO clients(name, last_name, membership) VALUES (%s, %s, %s)'
    UPDATE = 'UPDATE clients SET name=%s, last_name=%s, membership=%s WHERE id=%s'
    DELETE = 'DELETE FROM clients WHERE id=%s'

    @classmethod
    def select(cls):
        conexion = None
        Try:



        except Exception as e:
            print(f'An error ocurred: {e}') 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.clear_conexion()
