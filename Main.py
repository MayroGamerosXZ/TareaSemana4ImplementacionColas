
from TaskManagerX import TaskManagerX
from CustomerServiceX import CustomerServiceX

def run_task_manager():
    task_manager = TaskManagerX()
    task_manager.add_task("Task 1", "high")
    task_manager.add_task("Task 2", "normal")
    task_manager.add_task("Task 3", "high")
    task_manager.add_task("Task 4", "normal")

    print("Processing tasks:")
    task_manager.process_tasks()

def run_customer_service():
    customer_service = CustomerServiceX()
    customer_service.add_customer("Customer A")
    customer_service.add_customer("Customer B", vip=True)
    customer_service.add_customer("Customer C")
    customer_service.add_customer("Customer D", vip=True)

    print("\nServing customers:")
    customer_service.serve_customer()
    customer_service.serve_customer()
    customer_service.serve_customer()
    customer_service.serve_customer()

run_task_manager()
run_customer_service()