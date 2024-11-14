AirBnB Clone - The Console
Project Overview
This project is a command-line interpreter for managing objects related to an AirBnB clone. It is the first step towards building a complete web application, incorporating front-end, API, and database storage. This command interpreter will be used to create, modify, and delete instances of various classes, such as User, State, City, Place, and more.

Command Interpreter
The command interpreter, known as the console, allows users to interact with and manage various AirBnB objects directly from the command line. The console is built in Python and works in both interactive and non-interactive modes.

Features of the Command Interpreter
Create new objects.
Retrieve object details.
Update existing objects.
Delete objects.
List all objects or objects of a particular type.

How to Start
To start the command interpreter, open a terminal in the project directory and run the following command:./console.py
This will launch the interpreter in interactive mode, displaying a prompt that awaits user commands.

Alternatively, you can run the interpreter in non-interactive mode by piping commands to it. For example:echo "help" | ./console.py

Usage
The command interpreter accepts the following commands:

help: Displays available commands and how to use them.
quit: Exits the command interpreter.
EOF: Exits the command interpreter.
Additional commands for managing objects will be implemented in future updates.

Examples
Interactive Mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$

Non-Interactive Mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
