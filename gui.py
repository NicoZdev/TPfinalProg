import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox

# Lista temporal para almacenar los pacientes
patients = []

def create_main_window():
    window = tk.Tk()
    window.title("Gestión de Pacientes")
    
    # Ajustar la ventana a la resolución máxima del dispositivo
    window.state('zoomed')
    
    # Configurar un layout con dos columnas
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    
    # Frame para la lista de pacientes (lado izquierdo)
    table_frame = tk.Frame(window)
    table_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
    
    # Scrollbar vertical
    vsb = tk.Scrollbar(table_frame, orient="vertical")
    vsb.pack(side="right", fill="y")
    
    # Scrollbar horizontal
    hsb = tk.Scrollbar(table_frame, orient="horizontal")
    hsb.pack(side="bottom", fill="x")
    
    # Tabla para mostrar la lista de pacientes
    columns = ("ID", "Nombre", "Fecha Nacimiento", "Edad", "Documento", "Estado civil", "Persona responsable", "Teléfono", "Alergias", "Medico de cabezera", "Diagnostico clinico")
    patient_table = ttk.Treeview(table_frame, columns=columns, show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    for col in columns:
        patient_table.heading(col, text=col)
        patient_table.column(col, width=100)
    patient_table.pack(expand=True, fill='both')
    
    # Configurar scrollbars para la tabla
    vsb.config(command=patient_table.yview)
    hsb.config(command=patient_table.xview)
    
    # Frame para el formulario de paciente (lado derecho)
    form_frame = tk.Frame(window)
    form_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

    # Labels y Entrys para ingresar datos del paciente
    tk.Label(form_frame, text="Nombre Completo:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Fecha de nacimiento:").grid(row=1, column=0, padx=10, pady=5)
    date_entry = tk.Entry(form_frame)
    date_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Edad:").grid(row=2, column=0, padx=10, pady=5)
    age_entry = tk.Entry(form_frame)
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Documento:").grid(row=3, column=0, padx=10, pady=5)
    dni_entry = tk.Entry(form_frame)
    dni_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Estado civil:").grid(row=4, column=0, padx=10, pady=5)
    marital_entry = tk.Entry(form_frame)
    marital_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Persona Responsable:").grid(row=5, column=0, padx=10, pady=5)
    person_entry = tk.Entry(form_frame)
    person_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Teléfono Persona Responsable:").grid(row=6, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(form_frame)
    phone_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Alergias:").grid(row=7, column=0, padx=10, pady=5)
    allergis_entry = tk.Entry(form_frame)
    allergis_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Medico de cabezera:").grid(row=8, column=0, padx=10, pady=5)
    medic_entry = tk.Entry(form_frame)
    medic_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Diagnostico Clinico:").grid(row=9, column=0, padx=10, pady=5)
    diagnostic_entry = tk.Entry(form_frame)
    diagnostic_entry.grid(row=9, column=1, padx=10, pady=5)

    # Frame para los botones
    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=10, column=0, columnspan=2, pady=20)

    add_button = tk.Button(button_frame, text="Agregar Paciente", command=lambda: add_patient(patient_table, name_entry, date_entry, age_entry, dni_entry, marital_entry, person_entry, phone_entry, allergis_entry, medic_entry, diagnostic_entry))
    add_button.grid(row=0, column=0, padx=10, pady=5)

    edit_button = tk.Button(button_frame, text="Editar Paciente", command=lambda: edit_patient(patient_table, name_entry, date_entry, age_entry, dni_entry, marital_entry, person_entry, phone_entry, allergis_entry, medic_entry, diagnostic_entry))
    edit_button.grid(row=0, column=1, padx=10, pady=5)

    delete_button = tk.Button(button_frame, text="Eliminar Paciente", command=lambda: delete_patient(patient_table))
    delete_button.grid(row=0, column=2, padx=10, pady=5)

    #Cargar los datos del paciente seleccionado en el formulario
    def on_patient_select(event):
        selected_item = patient_table.selection()
        if selected_item:
            item = patient_table.item(selected_item)
            values = item['values']
            
            # Cargar datos en el formulario
            name_entry.delete(0, tk.END)
            name_entry.insert(0, values[1])
            date_entry.delete(0, tk.END)
            date_entry.insert(0, values[2])
            age_entry.delete(0, tk.END)
            age_entry.insert(0, values[3])
            dni_entry.delete(0, tk.END)
            dni_entry.insert(0, values[4])
            marital_entry.delete(0, tk.END)
            marital_entry.insert(0, values[5])
            person_entry.delete(0, tk.END)
            person_entry.insert(0, values[6])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, values[7])
            allergis_entry.delete(0, tk.END)
            allergis_entry.insert(0, values[8])
            medic_entry.delete(0, tk.END)
            medic_entry.insert(0, values[9])
            diagnostic_entry.delete(0, tk.END)
            diagnostic_entry.insert(0, values[10])

    patient_table.bind('<<TreeviewSelect>>', on_patient_select)

    # Iniciar el loop principal de la aplicación
    window.mainloop()

def add_patient(patient_table, name_entry, date_entry, age_entry, dni_entry, marital_entry, person_entry, phone_entry, allergis_entry, medic_entry, diagnostic_entry):
    # Obtener datos del formulario
    patient_data = {
        "ID": len(patients) + 1,
        "Nombre": name_entry.get(),
        "Fecha Nacimiento": date_entry.get(),
        "Edad": age_entry.get(),
        "Documento": dni_entry.get(),
        "Estado civil": marital_entry.get(),
        "Persona responsable": person_entry.get(),
        "Teléfono": phone_entry.get(),
        "Alergias": allergis_entry.get(),
        "Medico de cabezera": medic_entry.get(),
        "Diagnostico clinico": diagnostic_entry.get(),
    }

    # Añadir a la lista temporal de pacientes
    patients.append(patient_data)
    
    # Añadir a la tabla visual
    patient_table.insert("", "end", values=list(patient_data.values()))

    # Limpiar los campos del formulario después de agregar
    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    marital_entry.delete(0, tk.END)
    person_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    allergis_entry.delete(0, tk.END)
    medic_entry.delete(0, tk.END)
    diagnostic_entry.delete(0, tk.END)

def edit_patient(patient_table, name_entry, date_entry, age_entry, dni_entry, marital_entry, person_entry, phone_entry, allergis_entry, medic_entry, diagnostic_entry):
    selected_item = patient_table.selection()
    if selected_item:
        if msgbox.askyesno("Confirmar Edición", "¿Estás seguro de que deseas editar este paciente?"):
            item = patient_table.item(selected_item)
            patient_id = item['values'][0]
            
            # Buscar el paciente en la lista temporal
            for patient in patients:
                if patient['ID'] == patient_id:
                    # Actualizar los valores
                    patient['Nombre'] = name_entry.get()
                    patient['Fecha Nacimiento'] = date_entry.get()
                    patient['Edad'] = age_entry.get()
                    patient['Documento'] = dni_entry.get()
                    patient['Estado civil'] = marital_entry.get()
                    patient['Persona responsable'] = person_entry.get()
                    patient['Teléfono'] = phone_entry.get()
                    patient['Alergias'] = allergis_entry.get()
                    patient['Medico de cabezera'] = medic_entry.get()
                    patient['Diagnostico clinico'] = diagnostic_entry.get()
                    
                    # Actualizar la tabla visual
                    patient_table.item(selected_item, values=list(patient.values()))
                    break

def delete_patient(patient_table):
    selected_item = patient_table.selection()
    if selected_item:
        if msgbox.askyesno("Confirmar Eliminación", "¿Estás seguro de que deseas eliminar este paciente?"):
            item = patient_table.item(selected_item)
            patient_id = item['values'][0]
            
            # Eliminar de la lista temporal
            global patients
            patients = [patient for patient in patients if patient['ID'] != patient_id]
            
            # Eliminar de la tabla visual
            patient_table.delete(selected_item)

# Ejecutar la aplicación
create_main_window()
    
# Aquí agregarías el código para insertar en la base de datos
# print(f"Paciente agregado: {name}, {date}, {age}, {dni}, {marital}, {person}, {phone}, {allergis}, {medic}, {diagnostic}")
