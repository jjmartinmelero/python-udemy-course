class Client:
    def __init__(self, id=None, name=None, last_name=None, membership=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.membership = membership

    def __str__(self):
        return f'Id: {self.id} name: {self.name} last_name: {self.last_name}, membership: {self.membership}'
        
