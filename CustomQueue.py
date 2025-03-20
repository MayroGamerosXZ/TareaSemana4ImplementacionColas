class Node:
    """Representa un nodo en la cola."""
    def __init__(self, value):
        self.value = value
        self.next = None

class CustomQueue:
    """Implementación de una cola personalizada."""
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, element):
        """Agrega un elemento al final de la cola."""
        new_node = Node(element)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self.count += 1

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        removed_value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self.count -= 1
        return removed_value

    def front(self):
        """Devuelve el primer elemento sin eliminarlo."""
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self.front_node.value

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.count == 0

    def size(self):
        """Devuelve el número de elementos en la cola."""
        return self.count