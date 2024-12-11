import tkinter as tk
from tkinter import ttk, messagebox

win = tk.Tk()
win.geometry("600x400")

input_name = tk.Entry(win)
input_phone = tk.Entry(win)
label_name = tk.Label(win, text="Nombre:")
label_phone = tk.Label(win, text="Telefono:")
tree_agenda = ttk.Treeview(win, columns=(
    "id", "name", "phone"), show="headings")

agenda = []


def add():
    name = input_name.get()
    phone = input_phone.get()
    if not (name and phone):
        messagebox.showwarning(
            "Campos vacios", "Debes rellenar todos los campos")
        return
    for cont in agenda:
        if name in cont and phone in cont:
            messagebox.showwarning("Duplicados", "Este contacto ya existe")
            return

    id = str(len(agenda)+1)
    agenda.append([id, name, phone])
    update()


def update():
    for elem in tree_agenda.get_children():
        tree_agenda.delete(elem)
    for contact in agenda:
        tree_agenda.insert("", "end", values=(
            contact[0], contact[1], contact[2]))


def remove_selected():
    selected = tree_agenda.selection()
    if selected:
        contact = tree_agenda.item(selected, "values")
        agenda.remove(list(contact))
        tree_agenda.delete(selected)


def update_selected():
    selected = tree_agenda.selection()
    if selected:
        name = input_name.get()
        phone = input_phone.get()
        contact = list(tree_agenda.item(selected, "values"))
        idx = agenda.index(contact)
        agenda[idx] = [contact[0], name, phone]
        update()


btn_add = tk.Button(win, text="Añadir", command=add)
btn_remove = tk.Button(win, text="Borrar", command=remove_selected)
btn_update = tk.Button(win, text="Actualizar", command=update_selected)


label_name.grid(row=0, column=0)
input_name.grid(row=0, column=1)
label_phone.grid(row=0, column=2)
input_phone.grid(row=0, column=3)
btn_add.grid(row=1, column=0)
btn_update.grid(row=1, column=1)
btn_remove.grid(row=1, column=2)
tree_agenda.grid(row=2, column=0, columnspan=4)

tree_agenda.heading("id", text="No.")
tree_agenda.heading("name", text="NOMBRE")
tree_agenda.heading("phone", text="TELEFONO")

tree_agenda.column("id", anchor="center")
tree_agenda.column("name", anchor="center")
tree_agenda.column("phone", anchor="center")

win.mainloop()
