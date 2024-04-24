import PySimpleGUI as sg

user_input_title = sg.Text("To-Do Box ")
user_input_box = sg.Input(tooltip="Enter todo")
add_box = sg.Button("add")

window = sg.Window('My To-Do Lists', layout=[[user_input_title], [user_input_box,add_box]])

window.read()
window.close()