# 0x00. AirBnB clone - The console

_For this project, students are expected to look at these concepts:_

- <a href="https://docs.python.org/3.4/tutorial/modules.html#packages">Python packages</a>
- <a href="https://intranet.hbtn.io/concepts/74">AirBnB clone</a>


## Background Context
### Welcome to the AirBnB clone project! (The Holberton B&B)
Before starting, please read the __AirBnB__ concept page.

_click on the following image for a general description of the project:_
<a href="https://www.youtube.com/watch?v=E12Xc3H2xqo&feature=emb_logo"><img src="https://i.postimg.cc/Jny7fBMK/hbnb.png"></a>

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


### flowchart
<img src="https://i.ibb.co/GpDQn3P/Hbnb-clone.jpg"></a>
<img src="https://i.ibb.co/86GzbvP/Hbnb-clone-1.jpg"></a>

### How to install

- In your linux terminal use the command `git clone https://github.com/jdanielue/AirBnB_clone`


### How to use it

- You should excecute the command :
```
./console.py
```

- once you have done that you will get into the interactive mode.
- press help to get an orientation about the commands:
```
jdanielue AirBnB_clone->./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

### classes allowed
---
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

---

### Commands

#### Create:
- Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
```
(hbnb) create BaseModel
86bf74e2-831b-4c46-950f-5da0aff84a69
```
#### show:
- Prints the string representation of an instance based on the class name and id
```
(hbnb) show BaseModel 86bf74e2-831b-4c46-950f-5da0aff84a69
[BaseModel] (86bf74e2-831b-4c46-950f-5da0aff84a69) {'id': '86bf74e2-831b-4c46-950f-5da0aff84a69', 'created_at': datetime.datetime(2021, 2, 22, 14, 40, 32, 722037), 'updated_at': datetime.datetime(2021, 2, 22, 14, 40, 32, 722061)}
(hbnb)
```

#### update:
- Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
```
(hbnb) update BaseModel 86bf74e2-831b-4c46-950f-5da0aff84a69 email 2380@holbertonschool.com
(hbnb)

(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 86bf74e2-831b-4c46-950f-5da0aff84a69
[BaseModel] (86bf74e2-831b-4c46-950f-5da0aff84a69) {'id': '86bf74e2-831b-4c46-950f-5da0aff84a69', 'created_at': datetime.datetime(2021, 2, 22, 14, 40, 32, 722037), 'updated_at': datetime.datetime(2021, 2, 22, 14, 44, 37, 142678), 'email': '2380@holbertonschool.com'}
```

#### all:
-  Prints all string representation of all instances based or not on the class name
```
(hbnb) all BaseModel
["[BaseModel] (94203acf-0913-4467-a378-6b3411f3de67) {'id': '94203acf-0913-4467-a378-6b3411f3de67', 'created_at': datetime.datetime(2021, 2, 17, 22, 43, 13, 586088), 'updated_at': datetime.datetime(2021, 2, 17, 22, 43, 13, 586101), 'name': 'Holberton', 'my_number': 89}", "[BaseModel] (86bf74e2-831b-4c46-950f-5da0aff84a69) {'id': '86bf74e2-831b-4c46-950f-5da0aff84a69', 'created_at': datetime.datetime(2021, 2, 22, 14, 40, 32, 722037), 'updated_at': datetime.datetime(2021, 2, 22, 14, 44, 37, 142678), 'email': '2380@holbertonschool.com'}"]
(hbnb)
```

#### destroy:
- Deletes an instance based on the class name and id (save the change into the JSON file).
```
(hbnb) destroy BaseModel 86bf74e2-831b-4c46-950f-5da0aff84a69
```

### Authors


Jorge Daniel Urrego - [Github](https://github.com/jdanielue) / [Twitter](https://twitter.com/jdanielue)
Vanessa Garcia - [Github](https://github.com/vagava) / [Twitter](https://twitter.com/vagava)