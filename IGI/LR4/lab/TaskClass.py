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


class TaskMixin:
    def info(self):
        print("Запущен ", self.__class__.__name__)
        print("Основан на ", self.__class__.__base__.__name__)
