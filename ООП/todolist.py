class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """добавление новой задачи в список"""
        task = {'description': description,'completed': False}
        self.tasks.append(task)
        print(f"добавлено {description}")

    def remove_task(self, index):
        """удаление задачи по индексу"""
        if 0 <= index < len(self.tasks): # проверяем есть ли такой номер
            removed_task = self.tasks.pop(index) # удаляем
            print(f"удалено {removed_task['description']}")
        else:
            print("не правильный индекс")

    def mark_completed(self, index):
        """выполненные задачи"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f"законченно {self.tasks[index]['description']}")
        else:
            print("не правильный индекс")

    def show_all_tasks(self):
        """показать все задачи"""
        if not self.tasks:
            print("нет задач в списке")

        print("\n---все задачи---")
        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. [{status}] {task['description']}")

    def show_completed_tasks(self):
        """показать только выполненные задачи"""
        completed_tasks = [task for task in self.tasks if task['completed']]

        if not completed_tasks:
            print("нет выполненных задач")

        print("\n---выполненные задачи---")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task['description']}")


# пример использования
todo = TodoList() # завел новый блокнот
# добавление задач
todo.add_task("купить продукты") # записал первую задачу
todo.add_task("доделать домашнее задание")
todo.add_task("позвонить маме")
# показать все задачи
todo.show_all_tasks()
# отметить выполненные задачи
todo.mark_completed(0)
# удалить задачу
todo.remove_task(1)
# вывод результата
todo.show_all_tasks()# вывод того что осталось
todo.show_completed_tasks()# вывод только сделанных
