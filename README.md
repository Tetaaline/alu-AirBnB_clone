# AirBnB Clone - The Console

## Description

This project is the first step toward building a full-stack web application that replicates AirBnB. It lays the foundation for all subsequent phases (HTML/CSS, database storage, API, and front-end) by implementing:

- A **command-line interpreter** to manage application objects
- A set of **data models** (User, Place, City, State, Amenity, Review) that inherit from a common `BaseModel`
- A **file storage engine** that serializes objects to JSON and deserializes them back

All data created through the interpreter persists across sessions via a JSON file (`file.json`).

## The Command Interpreter

The command interpreter is a interactive shell (powered by Python's `cmd` module) that lets you create, read, update, and delete objects from the command line — much like a mini ORM without a real database.

### Supported Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `create` | `create <class>` | Create a new instance and print its `id` |
| `show` | `show <class> <id>` | Print the string representation of an instance |
| `destroy` | `destroy <class> <id>` | Delete an instance permanently |
| `all` | `all [class]` | Print all instances, or all instances of a given class |
| `update` | `update <class> <id> <attr> <value>` | Add or update an attribute on an instance |
| `quit` | `quit` | Exit the interpreter |
| `EOF` | `Ctrl+D` | Exit the interpreter |
| `help` | `help [command]` | Show help for all or a specific command |

**Supported classes:** `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, `Review`

### How to Start

Clone the repository and make the console executable:

```bash
git clone https://github.com/Tetaaline/alu-AirBnB_clone.git
cd alu-AirBnB_clone
chmod +x console.py
```

**Interactive mode** — launch the shell and type commands at the prompt:

```bash
$ ./console.py
(hbnb)
```

**Non-interactive mode** — pipe commands directly:

```bash
$ echo "help" | ./console.py
```

### How to Use

Once the `(hbnb)` prompt appears, enter any of the supported commands. Arguments are separated by spaces; string values containing spaces should be wrapped in double quotes.

#### General syntax

```
(hbnb) <command> <ClassName> [<id>] [<attribute_name>] [<attribute_value>]
```

### Examples

#### Creating instances

```
$ ./console.py
(hbnb) create User
9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a
(hbnb) create Place
2c9d2c88-7f63-4e50-b07d-3e2f0c1d5a7b
```

#### Showing an instance

```
(hbnb) show User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a
[User] (9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a) {'id': '9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a', 'created_at': datetime.datetime(2024, 1, 1, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 1, 0, 0, 0)}
```

#### Listing all instances

```
(hbnb) all
["[User] (9b6e4c22-...) {...}", "[Place] (2c9d2c88-...) {...}"]
(hbnb) all User
["[User] (9b6e4c22-...) {...}"]
```

#### Updating an attribute

```
(hbnb) update User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a email "user@example.com"
(hbnb) update User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a first_name "Aline"
(hbnb) show User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a
[User] (9b6e4c22-...) {'id': '9b6e4c22-...', ..., 'email': 'user@example.com', 'first_name': 'Aline'}
```

#### Destroying an instance

```
(hbnb) destroy User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a
(hbnb) show User 9b6e4c22-4ca5-4fef-8e8b-0f9d6f2c2e3a
** no instance found **
```

#### Exiting

```
(hbnb) quit
$
```

#### Non-interactive example

```bash
$ echo "create BaseModel" | ./console.py
(hbnb) 7da56403-cc45-4f1b-a1d7-0b72e03e1e58
$ echo "all BaseModel" | ./console.py
(hbnb) ["[BaseModel] (7da56403-...) {...}"]
```

#### Error messages

```
(hbnb) create
** class name missing **
(hbnb) create FakeClass
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel fake-id
** no instance found **
(hbnb) update BaseModel 7da56403-cc45-4f1b-a1d7-0b72e03e1e58
** attribute name missing **
```

## Project Structure

```
alu-AirBnB_clone/
├── console.py              # Entry point — the command interpreter
├── models/
│   ├── __init__.py         # Creates the global FileStorage instance
│   ├── base_model.py       # BaseModel: id, created_at, updated_at, save, to_dict
│   ├── user.py             # User model
│   ├── state.py            # State model
│   ├── city.py             # City model
│   ├── amenity.py          # Amenity model
│   ├── place.py            # Place model
│   ├── review.py           # Review model
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py # Serialization/deserialization to file.json
└── tests/
    └── test_models/        # Unit tests for all models and storage engine
```

## Running Tests

```bash
python3 -m unittest discover tests
```

## Authors

See the [AUTHORS](./AUTHORS) file.
