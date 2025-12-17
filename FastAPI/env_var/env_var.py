import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

# Run from bash terminal:
# next line to set the environment variable and run the script
# MY_NAME=FastAPI python FastAPI/env_var/env_var.py
# it will print: Hello FastAPI from Python
# or just run without setting the variable
# python FastAPI/env_var/env_var.py
# it will print: Hello World from Python
# to see the default value in action