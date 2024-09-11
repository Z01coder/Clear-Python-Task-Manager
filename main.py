"""
Задача: Создай класс `Task`¹, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
описание задачи², срок выполнения³ и статус (выполнено/не выполнено)⁴. Реализуй функцию для добавления задач⁵,
отметки выполненных задач⁶/⁸ и вывода списка текущих (не выполненных) задач⁷.
"""


class Task:  # ¹Создал класс
    def __init__(self, description, due_date):
        self.description = description  # ²Описание задачи
        self.due_date = due_date        # ³Срок выполнения
        self.completed = False          # ⁴Статус (по умолчанию: не выполнено)

    def mark_completed(self):           # ⁶Функция описывающая, каким образом задача будет отмечаться выполненной
        self.completed = True

    def __str__(self):                  # функция для текстового отображения
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:  # Создал ещё один класс, чтобы проще было работать с доп. функциями ⁵/⁶/⁷
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):  # ⁵Добавление задач. Принимает описание и срок
        task = Task(description, due_date)      # Здесь это будет храниться
        self.tasks.append(task)                 # Так это будет добавляться
        print(f"Задача '{description}' добавлена.")

    def mark_task_completed(self, task_index):   # ⁸Отметка выполненной задачи. Принимает номер (индекс) задачи
        self.tasks[task_index].mark_completed()  # "Закрывает" задачу по нужному индексу
        print(f"Задача '{self.tasks[task_index].description}' выполнено.")

    def show_pending_tasks(self):                # ⁷Показать невыполненные задачи
        print("Список текущих задач:")
        for i, task in enumerate(self.tasks):    # Берёт индекс и задачу
            if not task.completed:               # Если находит не выполненную
                print(f"{i}. {task}")


# Тестирую
task_manager = TaskManager()
task_manager.add_task("Сделать сальтуху", "11.09.2024")
task_manager.add_task("Купить слона", "11.09.2024")
task_manager.add_task("Позвонить в колокол", "11.09.2024")

# Проверяю как добавились
task_manager.show_pending_tasks()

# "Убиваю" таск по индексу
task_manager.mark_task_completed(1)

# Проверяю, обновился ли список
task_manager.show_pending_tasks()