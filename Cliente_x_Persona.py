class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None, cedula=None):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula

    def __str__(self):
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}, cedula: {self._cedula}]')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    def saludar(self):
        print(f'Hola soy {self._nombre}')


class Cliente(Persona):
    '''
    Crear los objetos de tipo Cliente
    '''
    def __init__(self, nombre, genero, ocupacion, cedula, email=None):
        super().__init__(nombre, genero, ocupacion, cedula)
        self._email = email

    def __str__(self):
        return (f'Cliente: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}, cedula: {self._cedula}, '
                f'email: {self._email}]')


if __name__ == '__main__':
    cliente1 = Cliente('Maria', 'F', 'Tecnolog', '1234567890', 'maria@example.com')
    print(cliente1)

    cliente2 = Cliente('Juan', 'M', 'Estudiante', '0987654321')
    cliente2.email = 'juan@example.com'
    print(cliente2)
