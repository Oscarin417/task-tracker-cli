# Task Tracker / Gestor de Tareas

A simple command-line task manager built in Python. / Un gestor de tareas simple para línea de comandos construido en Python.

---

## English

### Overview

Task Tracker is a CLI application that allows you to manage tasks with three statuses: `todo`, `in-progress`, and `done`. Tasks are stored locally in a `db.json` file.

### Project Structure

```
task-tracker/
├── main.py        # Entry point with CLI argument parsing
├── utils.py       # Task class with CRUD operations
├── intefaz.py     # TypedDict interface for task structure
├── db.json        # Local JSON database (auto-created)
└── __init__.py    # Package initializer
```

### Requirements

- Python 3.10+

### Usage

Run the application from the project directory:

```bash
python main.py <command> [arguments]
```

### Commands

| Command | Description | Example |
|---|---|---|
| `add <description>` | Create a new task | `python main.py add "Fix login bug"` |
| `list [status]` | List all tasks, optionally filtered by status | `python main.py list todo` |
| `update <id> <description>` | Update a task's description | `python main.py update abc1 "New description"` |
| `mark-in-progress <id>` | Mark a task as in-progress | `python main.py mark-in-progress abc1` |
| `mark-done <id>` | Mark a task as done | `python main.py mark-done abc1` |
| `delete <id>` | Delete a task | `python main.py delete abc1` |

### Task Structure

Each task contains:

- **id** - Random 4-character identifier
- **descripcion** - Task description
- **status** - One of: `todo`, `in-progress`, `done`
- **createdAt** - Creation timestamp
- **updatedAt** - Last update timestamp (empty until modified)

---

## Español

### Descripción

Task Tracker es una aplicación de línea de comandos que permite gestionar tareas con tres estados: `todo`, `in-progress` y `done`. Las tareas se almacenan localmente en un archivo `db.json`.

### Estructura del Proyecto

```
task-tracker/
├── main.py        # Punto de entrada con análisis de argumentos CLI
├── utils.py       # Clase Task con operaciones CRUD
├── intefaz.py     # Interfaz TypedDict para la estructura de tareas
├── db.json        # Base de datos JSON local (se crea automáticamente)
└── __init__.py    # Inicializador del paquete
```

### Requisitos

- Python 3.10+

### Uso

Ejecuta la aplicación desde el directorio del proyecto:

```bash
python main.py <comando> [argumentos]
```

### Comandos

| Comando | Descripción | Ejemplo |
|---|---|---|
| `add <descripción>` | Crear una nueva tarea | `python main.py add "Corregir bug de login"` |
| `list [estado]` | Listar todas las tareas, opcionalmente filtradas por estado | `python main.py list todo` |
| `update <id> <descripción>` | Actualizar la descripción de una tarea | `python main.py update abc1 "Nueva descripción"` |
| `mark-in-progress <id>` | Marcar una tarea como en progreso | `python main.py mark-in-progress abc1` |
| `mark-done <id>` | Marcar una tarea como completada | `python main.py mark-done abc1` |
| `delete <id>` | Eliminar una tarea | `python main.py delete abc1` |

### Estructura de una Tarea

Cada tarea contiene:

- **id** - Identificador aleatorio de 4 caracteres
- **descripcion** - Descripción de la tarea
- **status** - Uno de: `todo`, `in-progress`, `done`
- **createdAt** - Marca de tiempo de creación
- **updatedAt** - Marca de tiempo de última actualización (vacío hasta que se modifique)
