# 0x00. AirBnB clone - The console

_For this project, students are expected to look at these concepts:_

- <a href="https://docs.python.org/3.4/tutorial/modules.html#packages">Python packages</a>
- <a href="https://intranet.hbtn.io/concepts/74">AirBnB clone</a>


## Background Context
### Welcome to the AirBnB clone project! (The Holberton B&B)
Before starting, please read the __AirBnB__ concept page.

_click on the following image for a general description of the project:_
<a href="https://www.youtube.com/watch?v=E12Xc3H2xqo&feature=emb_logo"><img src="https://i.postimg.cc/Jny7fBMK/hbnb.png"></a>

#### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances.
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>…) that inherit from <code>BaseModel</code>.
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources
Read or watch:

- <a href="https://docs.python.org/3/library/cmd.html">cmd module</a>
- __packages concept page__
- <a href="https://docs.python.org/3/library/uuid.html">uuid module</a>
- <a href="https://docs.python.org/3/library/datetime.html">datetime</a>
- <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest">unittest module</a>
- <a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a>
- <a href="https://www.pythonsheets.com/notes/python-tests.html">Python test cheatsheet</a>

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage <code>datetime</code>
- What is an <code>UUID</code>
- What is <code>*args</code> and how to use it
- What is <code>**kwargs</code> and how to use it
- How to handle named arguments in a function

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(\_\_import__("my_module").\_\_doc__)')
- All your classes should have a documentation (python3 -c 'print(\_\_import__("my_module").MyClass.\_\_doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(\_\_import__("my_module").my_function.\_\_doc__)' and python3 -c 'print(\_\_import__("my_module").MyClass.my_function.\_\_doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(\_\_import__("my_module").\_\_doc__)')
- All your classes should have a documentation (python3 -c 'print(\_\_import__("my_module").MyClass.\_\_doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(\_\_import__("my_module").my_function.\_\_doc__)' and python3 -c 'print(\_\_import__("my_module").MyClass.my_function.\_\_doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case