from CustomQueue import CustomQueue

class CustomerServiceX:
    """Simulación de un sistema de atención al cliente."""
    def __init__(self):
        self.regular_queue = CustomQueue()
        self.vip_queue = CustomQueue()

    def add_customer(self, customer, vip=False):
        """Agrega un cliente a la cola de VIP o regular."""
        if vip:
            self.vip_queue.enqueue(customer)
        else:
            self.regular_queue.enqueue(customer)

    def serve_customer(self):
        """Atiende a los clientes en orden de prioridad."""
        if not self.vip_queue.is_empty():
            customer = self.vip_queue.dequeue()
            print(f"Serving VIP customer: {customer}")
        elif not self.regular_queue.is_empty():
            customer = self.regular_queue.dequeue()
            print(f"Serving regular customer: {customer}")
        else:
            print("No customers to serve")