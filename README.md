# **AirBnB Clone**
<p align="center">
  <img src="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/Images/airbnb%20banner.gif" width="550" height="200">
</p>

## **📋 Table of Contents**
1. [Introduction](#introduction)
2. [Synopsis](#synopsis)
3. [Project](#Project)
  - [Python Scripts Requirements](#Python-Scripts-Requirements)
  - [Python Unit Tests Requirements](#Python-Unit-Tests-Requirements)
  - [Functions and system calls used](#functions-and-system-calls-used)
    - [Description of each file](#description-of-each-file)
  - [Environment](#environment)
  - [Testing](#testing)
    - [Interactive](#interactive-mode)
    - [Non-Interactive](#non-interactive-mode)
5. [Authors](#authors)

## **📜Introduction**
* In this project we coded from scratch an AirBnb clone.
* This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances.

[Back to Top](#AirBnB-Clone)
    
## **💡Synopsis**
The application begins in console.py, which calls an instance of the FileStorage class in __init__.py. This class manages all files within the storage system. For file operations, the FileStorage class calls methods from the base_model.py and file_storage.py scripts, each responsible for different aspects of the system.

[Back to Top](#AirBnB-Clone)
  
## **💽Project**

### **📑Python Scripts Requirements**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All your files should end with a new line
  - The first line of all your files should be exactly #!/usr/bin/python3
  - A README.md file, at the root of the folder of the project, is mandatory
  - Your code should use the pycodestyle (version 2.7.*)
  - All your files must be executable
  - The length of your files will be tested using wc
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c       '       'print(__import__("my_module").MyClass.my_function.__doc__)')
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### **📑Python Unit Tests Requirements**
  - Allowed editors: `vi`, `vim`, `emacs`
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
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c   '           'print(__import__("my_module").MyClass.my_function.__doc__)')
  
### **💻Functions and system calls used**

  
#### **🗃Description of each file**

<!DOCTYPE html>
<html>

  <body>

<table style="width:100%">
  <tr>
    <th>File Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/console.py">console.py</a></td>
    <td>Entry point for the application. It provides a user interface for the console. It contains the main loop that waits for input from the user, processes the input and provides output.</td>  
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/__init__.py">__init__.py</a></td>
    <td>Initialises a new instance of FileStorage. This is the setup file for the models package. It contains import statements for all classes in the package, creating an instance of the FileStorage class and immediately calling the reload() method on it.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/base_model.py">base_model.py</a></td>
    <td>Contains the BaseModel class, with common methods for saving, updating, and deleting records. It defines the attributes that are common to all other classes, and methods for managing the serialization and deserialization of instances. ($)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py">file_storage.py</a></td>
    <td>Contains the FileStorage class, which handles serialization and deserialization of instances to JSON format, writing and reading from a JSON file. It is also responsible for managing the dictionary objects, where all instances are stored, and for saving and loading instances to and from the JSON file.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/user.py">user.py</a></td>
    <td>A user model that inherits from BaseModel. This class represents a user of the application. Attributes include email, password, first_name, and last_name.</td>
  </tr>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/state.py">state.py</a></td>
    <td>A state model that inherits from BaseModel. This class represents a state. It includes an attribute name for the name of the state.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/city.py">city.py</a></td>
    <td>A city model that inherits from BaseModel. This class represents a city. Attributes include state_id and name. state_id is a string that represents the id of the State instance the City is linked to. name is the name of the city.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/amenity.py">amenity.py</a></td>
    <td>An amenity model that inherits from BaseModel. This class represents an amenity. It includes an attribute name for the name of the amenity.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/place.py">place.py</a></td>
    <td>A place model that inherits from BaseModel. This class represents a place. Attributes include city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, and amenity_ids.</td>
  </tr>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/review.py">review.py</a></td>
    <td>A review model that inherits from BaseModel. This class represents a review. Attributes include place_id, user_id, and text.</td>
  </tr>
</table>

</body>
</html>

### **🌎Environment**
  - Language: Python
  - OS: Ubuntu 20.04
  - Compiler: python3 (version 3.8.5)
  - Style guideines: pycodestyle (version 2.7.*)

### **💻Testing**
  
   -You can test our custom version of the AirBnb Clone in the interactive and non-interactive mode.
    
#### **💻Interactive mode**

  - The console should work like this in interactive mode:
```
    $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================

EOF  help  quit

(hbnb) 

(hbnb) 

(hbnb) quit
$
```
    
#### **💻Non-Interactive mode**

  -In the non-interactive mode should work like this:
```
  $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================

EOF  help  quit
(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF  help  quit

(hbnb) 

$
```      
[Back to Top](#AirBnB-Clone)

## 🤝Authors
![Braian Perez](https://github.com/BraianPerez97)
![Eduardo Figueroa](https://github.com/semaed)

[Back to Top](#AirBnB-Clone)
