# todolist da fare in python, 

# aggiungi_task, visualizza_task, completa_task, rimuovi_task
import json

tasks = []
def aggiungi_task():
    nome_task = input("Inserisci la nuova task: ")
    tasks.append({"nome ": nome_task, "completato": False})
    print(f'Task "{nome_task}" aggiunto alla lista.')



aggiungi_task()
print(tasks)

def salva_task():
    with open("tasks.json","w") as file:
        json.dump(tasks,file)

def carica_task():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []