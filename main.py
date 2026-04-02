import argparse
from utils import Task

def main():
    task: Task = Task()
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Programa de tasks"
    )

    subparser = parser.add_subparsers(dest="comando", required=True)

    parser_listar = subparser.add_parser("list", help="List all tasks")
    parser_listar.add_argument(
        "status",
        nargs="?",
        default=None,
        choices=["todo", "in-progress", "done"]
    )
    parser_agregar = subparser.add_parser("add", help="Add new task")
    parser_agregar.add_argument("description", type=str)
    parser_actualizar = subparser.add_parser("update", help="Update a task")
    parser_actualizar.add_argument("id", type=str)
    parser_actualizar.add_argument("description", type=str)
    parser_status_progress = subparser.add_parser("mark-in-progress", help="Update a status")
    parser_status_progress.add_argument("id", type=str)
    parser_status_done = subparser.add_parser("mark-done", help="Update a status")
    parser_status_done.add_argument("id", type=str)
    parser_eliminar = subparser.add_parser("delete", help="Delete a task")
    parser_eliminar.add_argument("id", type=str)

    args: argparse.Namespace = parser.parse_args()

    if args.comando == "list":
        task.list_tasks(args.status)
    elif args.comando == "add":
        task.create_task(args.description)
    elif args.comando == "update":
        task.update_task(args.description, args.id)
    elif args.comando == "mark-in-progress":
        task.update_status_progress(args.id)
    elif args.comando == "mark-done":
        task.update_status_done(args.id)
    elif args.comando == "delete":
        task.delete_task(args.id)

if __name__ == "__main__":
    main()
