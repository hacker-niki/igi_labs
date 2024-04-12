class Task:
    current_task = None

    def __init__(self, task):
        self.current_task = task

    @property
    def task_num(self):
        return self.current_task

    @task_num.setter
    def task_num(self, task):
        self.current_task = task

    def start_task(self):
        print('You need to choose task to demostrate')
