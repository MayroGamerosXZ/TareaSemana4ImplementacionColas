from CustomQueue import CustomQueue

class TaskManagerX:
    """Gestor de tareas con prioridad."""
    def __init__(self):
        self.high_priority_queue = CustomQueue()
        self.normal_priority_queue = CustomQueue()

    def add_task(self, task, priority):
        """Agrega una tarea con un nivel de prioridad específico."""
        if priority == "high":
            self.high_priority_queue.enqueue(task)
        elif priority == "normal":
            self.normal_priority_queue.enqueue(task)
        else:
            raise ValueError("Invalid priority level")

    def process_tasks(self):
        """Procesa las tareas en orden de prioridad."""
        while not self.high_priority_queue.is_empty():
            task = self.high_priority_queue.dequeue()
            print(f"Processing high priority task: {task}")
        while not self.normal_priority_queue.is_empty():
            task = self.normal_priority_queue.dequeue()
            print(f"Processing normal priority task: {task}")