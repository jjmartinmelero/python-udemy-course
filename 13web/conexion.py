from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'sql7805841'
    USERNAME = 'sql7805841'
    PASSWORD = 'CInU3u9Cwv'
    DB_PORT = '3306'
    HOST = 'sql7.freesqldatabase.com'
    POOL_SIZE = 5
    POOL_NAME = 'project_app'
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def get_conexion(cls):
        return cls.get_pool().get_connection()

    @classmethod
    def clear_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.get_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.clear_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
