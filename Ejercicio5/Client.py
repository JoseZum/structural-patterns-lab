class Client:
    def __init__(self, username: str, role: str):
        self.__username = username  
        self.__role = role          # "admin", "supervisor", "viewer"

    # Métodos getter para acceder a los atributos privados
    def getUsername(self):
        return self.__username

    def getRole(self):
        return self.__role