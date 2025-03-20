# TareaSemana4ImplementacioncOLAS
# Proyecto de Colas con Prioridad

Este proyecto implementa una cola personalizada y utiliza esta cola para gestionar tareas con prioridad y atender a clientes en un sistema de atención al cliente.

## Contenido

- `queue.py`: Contiene la implementación de la clase `CustomQueue`, una cola personalizada.
- `task_manager.py`: Contiene la implementación de la clase `TaskManager`, un gestor de tareas con prioridad.
- `customer_service.py`: Contiene la implementación de la clase `CustomerService`, un sistema de atención al cliente que prioriza a los clientes VIP.
- `main.py`: Contiene el script principal que ejecuta los ejemplos.

## Clases

### CustomQueue

Implementación de una cola personalizada con las siguientes funcionalidades:

- `enqueue(element)`: Agrega un elemento al final de la cola.
- `dequeue()`: Elimina y devuelve el primer elemento de la cola.
- `front()`: Devuelve el primer elemento sin eliminarlo.
- `is_empty()`: Verifica si la cola está vacía.
- `size()`: Devuelve el número de elementos en la cola.

### TaskManager

Gestor de tareas con prioridad que maneja dos colas:

- `add_task(task, priority)`: Agrega una tarea con un nivel de prioridad específico.
- `process_tasks()`: Procesa las tareas en orden de prioridad.

### CustomerService

Simulación de un sistema de atención al cliente que prioriza a los clientes VIP:

- `add_customer(customer, vip=False)`: Agrega un cliente a la cola de VIP o regular.
- `serve_customer()`: Atiende a los clientes en orden de prioridad.

## Uso

Para ejecutar los ejemplos, simplemente ejecuta `main.py`:

```bash
python main.py

Processing tasks:
Processing high priority task: Task 1
Processing high priority task: Task 3
Processing normal priority task: Task 2
Processing normal priority task: Task 4

Serving customers:
Serving VIP customer: Customer B
Serving VIP customer: Customer D
Serving regular customer: Customer A
Serving regular customer: Customer C

