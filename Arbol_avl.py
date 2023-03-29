class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        self.raiz = self.__agregar(self.raiz, dato)

    def __agregar(self, nodo, dato):
        if not nodo:
            return Nodo(dato)
        elif dato < nodo.dato:
            nodo.izquierda = self.__agregar(nodo.izquierda, dato)
        else:
            nodo.derecha = self.__agregar(nodo.derecha, dato)

        nodo.altura = 1 + max(self.__altura(nodo.izquierda), self.__altura(nodo.derecha))

        balance = self.__factor_equilibrio(nodo)

        # Realizar las rotaciones
        if balance > 1 and dato < nodo.izquierda.dato:
            return self.__rotacion_derecha(nodo)

        if balance < -1 and dato > nodo.derecha.dato:
            return self.__rotacion_izquierda(nodo)

        if balance > 1 and dato > nodo.izquierda.dato:
            nodo.izquierda = self.__rotacion_izquierda(nodo.izquierda)
            return self.__rotacion_derecha(nodo)

        if balance < -1 and dato < nodo.derecha.dato:
            nodo.derecha = self.__rotacion_derecha(nodo.derecha)
            return self.__rotacion_izquierda(nodo)

        return nodo

    def __altura(self, nodo):
        if not nodo:
            return 0

        return nodo.altura

    def __factor_equilibrio(self, nodo):
        if not nodo:
            return 0

        return self.__altura(nodo.izquierda) - self.__altura(nodo.derecha)

    def __rotacion_derecha(self, nodo):
        temp = nodo.izquierda
        temp2 = temp.derecha

        temp.derecha = nodo
        nodo.izquierda = temp2

        nodo.altura = 1 + max(self.__altura(nodo.izquierda), self.__altura(nodo.derecha))
        temp.altura = 1 + max(self.__altura(temp.izquierda), self.__altura(temp.derecha))

        return temp

    def __rotacion_izquierda(self, nodo):
        temp = nodo.derecha
        temp2 = temp.izquierda

        temp.izquierda = nodo
        nodo.derecha = temp2

        nodo.altura = 1 + max(self.__altura(nodo.izquierda), self.__altura(nodo.derecha))
        temp.altura = 1 + max(self.__altura(temp.izquierda), self.__altura(temp.derecha))

        return temp

    def recorrido_inorden(self):
        self.__recorrido_inorden(self.raiz)

    def __recorrido_inorden(self, nodo):
        if nodo:
            self.__recorrido_inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.__recorrido_inorden(nodo.derecha)

    def recorrido_preorden(self):
        self.__recorrido_preorden(self.raiz)

    def __recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self.__recorrido_preorden(nodo.izquierda)
            self.__recorrido_preorden(nodo.derecha)

    def recorrido_postorden(self):
        self.__recorrido_postorden(self.raiz)

    def __recorrido_postorden(self, nodo):
        if nodo:
            self.__recorrido_postorden(nodo.izquierda)
            self.__recorrido_postorden(nodo.derecha)
            print(nodo.dato, end=" ")

    def altura(self):
        if not self.raiz:
            return 0

        return self.raiz.altura

    def nodos_hoja(self):
        return self.__nodos_hoja(self.raiz)

    def __nodos_hoja(self, nodo):
        if not nodo:
            return [nodo.dato]

        if not nodo.izquierda and not nodo.derecha:
            return [nodo.dato]
            
        return self.__nodos_hoja(nodo.izquierda) + self.__nodos_hoja(nodo.derecha)


# Ejemplo de uso
arbol = AVL()

n = int(input("Ingrese la cantidad de números a agregar: "))

for i in range(n):
    dato = int(input("Ingrese un número: "))
    arbol.agregar(dato)

print("\nÁrbol AVL Equilibrado:")
arbol.recorrido_inorden()

print("\nRecorrido en Preorden:")
arbol.recorrido_preorden()

print("\nRecorrido en Orden")
arbol.recorrido_inorden()
print("\nRecorrido en Postorden:")
arbol.recorrido_postorden()

print("\nAltura del árbol AVL:", arbol.altura())

print("\nNodos hoja del árbol AVL:", arbol.nodos_hoja())
