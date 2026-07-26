---
title: "Python CLI Todo App"
difficulty: "easy"
labels: ["week-1", "python", "cli"]
---

## Task Description
Build a command-line Todo application using Python.

## Requirements
- Add, list, complete, and delete tasks
- Persist tasks to a JSON file (`todos.json`)
- Tasks have: id, title, completed (bool), created_at (timestamp)
- Clean terminal output using `rich` or `colorama`

## Acceptance Criteria
- [ ] `python todo.py add "Buy groceries"` adds a task
- [ ] `python todo.py list` shows all tasks with their completion status
- [ ] `python todo.py done 1` marks task #1 as complete
- [ ] `python todo.py delete 1` removes task #1
- [ ] Data persists between runs (saved to `todos.json`)
- [ ] Type hints used on all functions

## Resources
- [Python JSON module](https://docs.python.org/3/library/json.html)
- [Click library](https://click.palletsprojects.com/)
