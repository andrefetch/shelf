import argparse
from shelf import storage
from shelf.models import Note

def cmd_add(args):
    notes = storage.load()
    note = Note(title=args.title, body=args.body, tags=args.tags or [])
    notes.append(note)
    storage.save(notes)
    print(f"Added [{note.id}] {note.title}")

def cmd_list(args):
    notes = storage.load()
    if not notes:
        print("No notes yet.")
        return
    for n in notes:
        tags = " ".join(f"#{t}" for t in n.tags)
        print(f"[{n.id}] {n.title}  {tags}")

def cmd_remove(args):
    notes = storage.load()
    original_len = len(notes)
    notes = [n for n in notes if n.id != args.id]
    if len(notes) == original_len:
        print(f"No note with id '{args.id}'")
        return
    storage.save(notes)
    print(f"Removed {args.id}")

def cmd_help(args):
    parser.print_help()

def main():
    parser = argparse.ArgumentParser(prog="shelf")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a note")
    p_add.add_argument("title")
    p_add.add_argument("body")
    p_add.add_argument("--tags", nargs="*")

    p_list = sub.add_parser("list", help="List all notes")

    p_remove = sub.add_parser("remove", help="Remove a note by id")
    p_remove.add_argument("id")

    args = parser.parse_args()
    dispatch = {"add": cmd_add, "list": cmd_list, "remove": cmd_remove}
    if args.command in dispatch:
        dispatch[args.command](args)
    else:
        parser.print_help()
