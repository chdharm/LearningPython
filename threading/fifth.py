from multiprocessing import Process

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()

run_cpu_tasks_in_parallel([
    lambda: print('CPU task 1 running!'),
    lambda: print('CPU task 2 running!'),
])