# Max heaps are used to maintain a maximum value in a dataset
# 2 principal qualities:
# - The root is the max value of the dataset.
# - Every parent's value is grater than its children.

class MaxHeap:
    
    def __init__(self):
        self.heap_list = [None]  # Inicializa la lista del montículo con None como primer elemento
        self.count = 0  # Contador de elementos en el montículo
    
    def parent_idx(self, idx):
        return idx // 2
    
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def add(self, element):
        self.heap_list.append(element)  # Añade el elemento al final de la lista
        self.count += 1
        self.heapify_up()  # Ajusta el montículo hacia arriba
    
    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:  # Mientras el índice del padre sea válido
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:  # Si el padre es menor que el hijo, intercambia sus valores
                self.heap_list[idx], self.heap_list[self.parent_idx(idx)] = parent, child
            idx = self.parent_idx(idx)  # Sube al padre
    
    def get_max(self):
        if self.count > 0:
            return self.heap_list[1]  # Retorna el elemento en la raíz del montículo
        return None
    
    def print_heap(self):
        print(self.heap_list[1:])  # Imprime todos los elementos excepto el primero (None)

# Creando una instancia de MaxHeap
heap = MaxHeap()

# Añadiendo elementos al montículo
heap.add(10)
heap.add(20)
heap.add(5)
heap.add(30)
heap.add(15)

# Imprimiendo el montículo y el máximo
heap.print_heap()  # Debería mostrar el montículo reorganizado
print("Max value:", heap.get_max())  # Debería mostrar el valor máximo (la raíz del montículo)
