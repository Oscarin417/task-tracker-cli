import json
import random
import string
from intefaz import TASKINTERFAZ
from datetime import datetime

try:
    with open("db.json", "r") as f:
        json.load(f)
except FileNotFoundError:
    data: list = []
    with open("db.json", "w") as f:
        json.dump(data, f, indent=4)

class Task:
    def __init__(self) -> None:
        self.fecha = datetime.now().strftime("%d/%m/%YT%H:%M:%S")

    def generate_id(self) -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=4))

    def list_tasks(self, status: str | None) -> None:
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        if status:
            for t in tasks:
                if t["status"] == status:
                    print(
                        f"{t['id']} - {t['descripcion']} - {t['status']}"
                    )
        else:
            for t in tasks:
                print(
                    f"{t['id']} - {t['descripcion']} - {t['status']}"
                )


    def create_task(self, descripcion: str) -> None:
        task: TASKINTERFAZ = {
            "id": self.generate_id(),
            "descripcion": descripcion,
            "status": "todo",
            "createdAt": self.fecha,
            "updatedAt": "",
        }
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        tasks.append(task)
        with open("db.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print("task creado")

    def update_task(self, descripcion: str, id: str)-> None:
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        for t in tasks:
            if t["id"] == id:
                t["descripcion"] = descripcion
                t["updatedAt"] = self.fecha
                break
        with open("db.json", "w") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print("task atualizado")

    def update_status_progress(self, id: str)-> None:
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        for t in tasks:
            if t["id"] == id:
                t["status"] = "in-progress"
                t["updatedAt"] = self.fecha
                break
        with open("db.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print("status atualizado")

    def update_status_done(self, id: str)-> None:
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        for t in tasks:
            if t["id"] == id:
                t["status"] = "done"
                t["updatedAt"] = self.fecha
                break
        with open("db.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print("status atualizado")

    def delete_task(self, id: str)-> None:
        with open("db.json", "r") as f:
            tasks: list[TASKINTERFAZ] = json.load(f)
        tasks = [t for t in tasks if t["id"] != id]
        with open("db.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print("task eliminado")
