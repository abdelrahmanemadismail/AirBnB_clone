# AirBnB Clone Project
![hbnb](https://github.com/abdelrahmanemadismail/AirBnB_clone/assets/122925308/a0c96b88-2582-4162-95a6-c3c8214d9529)

## Description
This project is a part of the ALX SE Program, is an AirBnB clone, where we implement a command-line interpreter in Python to manage AirBnB objects. It serves as the first step towards building a full web application.

## Command Interpreter Description
The command interpreter allows users to manage objects within the AirBnB project. Users can perform various operations such as creating new objects, retrieving objects, updating attributes, and more. It provides an interactive shell where users can input commands and receive corresponding outputs.

## Features
- Creation of Python package for AirBnB objects management
- Command-line interpreter for managing AirBnB objects
- Serialization and deserialization of objects
- File storage engine implementation
- Unit tests for validation of classes and storage engine

## Requirements
- Python 3.8.5 or higher
- Ubuntu 20.04 LTS
- `pycodestyle` for code style enforcement

## Installation
1. Clone the repository:
   `git clone <repository-url>`

2. Navigate to the project directory:
   `cd <project-directory>`

3. Ensure Python 3.8.5 is installed:
   `python3 --version`

4. Install `pycodestyle`:
   `pip install pycodestyle`

## Usage
1. To start the command-line interpreter in interactive mode:
   `./console.py`

2. Available commands:
   - `help`: Display available commands and their usage.
   - `EOF`: Exit the interpreter.
   - `quit`: Exit the interpreter.

3. Example usage in non-interactive mode:
   `echo "help" | ./console.py`

## Testing
1. Execute all unit tests:
   `python3 -m unittest discover tests`

2. Execute tests file by file:
   `python3 -m unittest tests/test_models/test_base_model.py`

## File Organization
- The Python scripts are organized into modules based on functionality.
- Test files are organized under the `tests` directory in a corresponding structure to the project.

## Contributors
- [Abdelrahman Ismail](https://github.com/abdelrahmanemadismail) <abdelrahman.e.ismail@gmail.com>
  
Please refer to the [AUTHORS](AUTHORS) file at the root of the repository for a complete list of individuals who have contributed to the project.

## Acknowledgements
- Special thanks to our mentors and instructors for their guidance and support.
- A special mention to Derrick Ampire for his support throughout the Program.
