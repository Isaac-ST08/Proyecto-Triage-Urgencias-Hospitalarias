class Agenda:
    """
    Agenda de contactos guardada de forma ordenada.
    """

    def __init__(self):
        """
        Se crea una agenda vacia.
        Complejidad: O(1)
        """
        self._contactos = []

    def __len__(self):
        """
        Se devuelve la cantidad de contactos.
        Complejidad: O(1)
        """
        return len(self._contactos)

    def _buscar_posicion(self, nombre: str):
        # Busqueda binaria para hallar el indice
        inicio = 0
        fin = len(self._contactos) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            contacto_actual = self._contactos[medio]
            nombre_actual = contacto_actual[0]

            if nombre_actual == nombre:
                return True, medio
            elif nombre_actual < nombre:
                inicio = medio + 1
            else:
                fin = medio - 1

        return False, inicio

    def contiene(self, nombre: str) -> bool:
        """
        Dice si un nombre esta en la agenda.
        Complejidad: O(log n)
        """
        resultado = self._buscar_posicion(nombre)
        encontrado = resultado[0]
        return encontrado

    def telefono_de(self, nombre: str) -> str:
        """
        Devuelve el telefono de un contacto.
        Complejidad: O(log n)
        """
        resultado = self._buscar_posicion(nombre)
        encontrado = resultado[0]
        posicion = resultado[1]

        if encontrado == False:
            raise KeyError("El contacto no existe")

        contacto = self._contactos[posicion]
        return contacto[1]

    def nombres(self) -> list:
        """
        Devuelve la lista con todos los nombres ordenados.
        Complejidad: O(n)
        """
        lista_nombres = []
        for contacto in self._contactos:
            lista_nombres.append(contacto[0])
        return lista_nombres

    def agregar(self, nombre: str, telefono: str) -> None:
        """
        Se agrega o actualiza un contacto en la agenda.
        Complejidad: O(n)
        """
        if nombre == "":
            raise ValueError("El nombre no puede estar vacio")

        telefono_texto = str(telefono)
        resultado = self._buscar_posicion(nombre)
        encontrado = resultado[0]
        posicion = resultado[1]

        if encontrado == True:
            self._contactos[posicion] = (nombre, telefono_texto)
        else:
            self._contactos.insert(posicion, (nombre, telefono_texto))

    def eliminar(self, nombre: str) -> None:
        """
        Se elimina un contacto de la agenda.
        Complejidad: O(n)
        """
        resultado = self._buscar_posicion(nombre)
        encontrado = resultado[0]
        posicion = resultado[1]

        if encontrado == False:
            raise KeyError("El contacto no existe")

        self._contactos.pop(posicion)