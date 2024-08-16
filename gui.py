import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass
sg.theme("DarkGrey10")
label = sg.Text("Enter a todo")
input_text = sg.InputText(tooltip="Enter a todo: ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(), size=(45, 10), enable_events=True, key="todos")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")
clock = sg.Text("", key="clock")
window = sg.Window(title="Todo App", layout=[[clock], [label], [input_text, add_button], [list_box, edit_button, delete_button], [exit_button]], font=("Arial", 18))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    # print(event)
    # print(value)
    match event:
        case 'Add':
            new_todo = value['todo'] + "\n"
            todos = functions.get_todo()
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todos = functions.get_todo()
                new_todo = value['todo'] + '\n'
                todo_to_edit = value['todos'][0]
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please enter a value", font=("Arial", 18))
        case 'Delete':
            try:
                todos = functions.get_todo()
                todo_to_delete = value['todos'][0]
                index = todos.index(todo_to_delete)
                todos.remove(todo_to_delete)
                # todos.pop(index)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a todo", font=("Arial", 18))
        case 'todos':
            try:
                window['todo'].update(value=value['todos'][0])
            except IndexError:
                sg.popup("Please add a value first", font=("Arial", 18))
        case 'Exit':
            break # exit() exit will break the code and code lines after it won't run
        case sg.WINDOW_CLOSED:
            break
window.close()
