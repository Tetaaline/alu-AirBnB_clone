# AirBnB Clone - The Console

## Description

This project is the first step toward building a full web application that clones AirBnB. The goal of this stage is to create a command interpreter that manages AirBnB objects. The project also introduces concepts such as object-oriented programming, file storage, serialization, deserialization, and unit testing.

The command interpreter allows users to:

* Create new objects
* Retrieve objects
* Update object attributes
* Delete objects
* Display all objects or objects of a specific class

## The Command Interpreter

### How to Start

Interactive mode:

```bash
$ ./console.py
(hbnb)
```

Non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```

### How to Use

Type commands at the `(hbnb)` prompt.

Available commands include:

* `create <class>` - Creates a new instance
* `show <class> <id>` - Displays an instance
* `destroy <class> <id>` - Deletes an instance
* `all [class]` - Displays all instances
* `update <class> <id> <attribute> <value>` - Updates an instance
* `quit` - Exits the console
* `EOF` - Exits the console using Ctrl+D
* `help` - Displays available commands

### Examples

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```
