#!/usr/bin/python3
import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        rows = self.c.fetchall()
        for row in rows:
            print()
            print("ID = ", str(row[0]) + ",", "Task = ", "\"" + str(row[1]) + "\"" + ",", "Priority = ", row[2])

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def find_task(self):
        name = input("Input the name of the task: ")
        query = f"SELECT * FROM tasks WHERE name LIKE '%{name}%' COLLATE NOCASE"
        self.c.execute(query)
        rows = self.c.fetchall()
        for row in rows:
            print()
            print("ID = ", str(row[0]) + ",", "Task = ", "\"" + str(row[1]) + "\"" + ",", "Priority = ", row[2])

    def change_priority(self):
        item_id = int(input("Input the ID of the task: "))
        priority = int(input("Input the desired priority: "))
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, item_id))
        self.conn.commit()

    def delete(self):
        item_id = int(input("Input the ID of the task: "))
        self.c.execute('DELETE FROM tasks WHERE id = ?', (item_id,))
        self.conn.commit()

    def read_user_choice(self):
        user_choice = int(input("Enter the number of desired action, 0....5: "))
        if user_choice in range(0, 7):
            return user_choice
        else:
            print("Not a valid choice")


    def menu(self):
        print('*TASKS DATABASE*')
        print('****************\n')
        print("1. Show tasks")
        print("2. Add task")
        print("3. Change priority")
        print("4. Delete task")
        print("5. Find task")
        print("0. Exit")


app = Todo()
while app.conn:
    app.menu()
    choice = app.read_user_choice()
    if choice == 1:
        app.show_tasks()
    if choice == 2:
        app.add_task()
    if choice == 3:
        app.change_priority()
    if choice == 4:
        app.delete()
    if choice == 5:
        app.find_task()
    if choice == 0:
        print("Exiting")
        exit(0)
else:
    print("Server not responding - exiting")
    exit(1)
