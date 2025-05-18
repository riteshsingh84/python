# Python Commandline Argument Processing using argparse

In Python, the argparse module is used to handle command-line arguments. It allows you to write user-friendly command-line interfaces and automatically generates help and usage messages.

## 🧰 Why use argparse?
* Makes your script flexible and configurable
* Automatically handles --help messages
* Validates input types
  
## 🔍 Key Components

* **ArgumentParser()** - Creates the parser
* **add_argument()** - Defines what arguments the program expects
* **parse_args()** - Parses the arguments from the command line
* **args.argument_name** - Accesses the value of the argument
* **Typed of Arguments** - You can specify the **type=** of the argument (e.g., int, float, str).
   * parser.add_argument("count", type=int, help="Number of items")
* **Default Values** - Use **default=** to provide a fallback if the argument is not given
    * parser.add_argument("--mode", default="fast", help="Mode of operation")
* **Choices** - Restrict the argument to a set of valid values.
    * parser.add_argument("--level", choices=["low", "medium", "high"], help="Set difficulty level")


## 🧩 Type Arguments 
1. Positional Arguments
    * Required arguments that must be provided in the correct order.
    * No prefix (--) is used.

    Example:

        parser.add_argument("filename", help="Name of the file")

2. Optional Arguments
    * Not required; usually have a default value.
    * Use -- or - prefix.

     Example:

        parser.add_argument("--verbose", help="Enable verbose mode", action="store_true")


## 🧠 Exercise

1. Take subject marks as command line arguments

    Example: 
    python3 cmd.py --physics 60 --chemistry 70 --maths 90

2. Find average marks for the three subjects using command line input of marks.  
   
   [Solution](https://github.com/riteshsingh84/python/tree/main/Basics/20_command_argument/exercise.py)
