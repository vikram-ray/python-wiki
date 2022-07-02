"""
This is a type of creational design pattern;
Advantage:
  1. We dont end up creating multiple instance of a class as it may lead to more memory consumption 
      & data inaccuracy
  2. Eg:
    - Logger: We want to have only 1 instance of a logger throughout our application for less memory consumption &         reliabality
    - Database connection: We only want to have 1 DB connection instance so that we dont end up creating muliple         connection to DB which may choke the DB
    - Some config setting should have only 1 instance
  3. Steps:
    a. Make the class constructor as private so that outer modules can't instanciate the class. (TODO)
    b. Expose a function that will return the same instance if called multiple times. If the instance is not               created yet, it will create and return.
    c. We also need the class to be thread safety so that parallel threads should not end up creating the a new           object. For this we need to lock the execution of the code if a thread is executing it. And release it           after the execution. (TODO)
    d. Also the lock is expecsive, so before locking only once if instance is None.
"""
# -----------------------Code without Singletone design-------------------------------------
class Database:
  init_counter = 0
  def __init__(self):
    Database.init_counter+=1

  def post(self, data):
    print(f"Pushed string DB: {data}")

# module1.py
def module1():
  db1 = Database()
  db1.post("Module 1 data")

# module2.py
def module2():
  db2 = Database()
  db2.post("Module 2 data")

module1()
module2()

#print total number of Database instance created
print(f"Database instance count: {Database.init_counter}") 
#It will print: Database instance: 2

"""
  As we can see, for every module where we want to use DB, 
  we will end up creating a new DB instance which is bad
"""

# -----------------------Code with Singletone design-------------------------------------
class Database:
  init_counter = 0
  db_instance = None
  def __init__(self):
    Database.init_counter+=1

  @staticmethod
  def get_db_instance():
    if Database.db_instance is None:
      Database.db_instance = Database()
    return Database.db_instance

  def post(self, data):
    print(f"Pushed string DB: {data}")
  
# module1.py
def module1():
  db1 = Database.get_db_instance()
  db1.post("Module 1 data")

# module2.py
def module2():
  db2 = Database.get_db_instance()
  db2.post("Module 2 data")

module1()
module2()
  
#print total number of Database instance created
print(f"Database instance count: {Database.init_counter}") 
#It will print: Database instance: 1

"""
Congrates! Now we will only get the same 1 instance, even if we call get_db_instance() multiple times;
But, this will not work fine with multithreading. Lets try it out!
"""

"""
INCOMPLETE BELOW!

"""


# import threading
# from multiprocessing import Process
# from concurrent.futures import ThreadPoolExecutor


# def run_io_tasks_in_parallel(tasks):
#     with ThreadPoolExecutor() as executor:
#         running_tasks = [executor.submit(task) for task in tasks]
#         for running_task in running_tasks:
#             running_task.result()

# class Database:
#   init_counter = 0
#   db_instance = None
#   def __init__(self):
    
#     Database.init_counter+=1
#     print(f"Database instance count: {Database.init_counter}") 


#   @staticmethod
#   def get_db_instance():
#     if Database.db_instance is None:
#       Database.db_instance = Database()
#     return Database.db_instance

#   def post(self, data):
#     print(f"Pushed string DB: {data}")
  
# # module1.py
# def module1():
#   print("module1 assigned to thread: {}".format(threading.current_thread().name))
#   #Prints: module1 assigned to thread: Thread-1
#   db1 = Database.get_db_instance()
#   db1.post("Module 1 data")

# # module2.py
# def module2():
#   print("module2 assigned to thread: {}".format(threading.current_thread().name))
#   #Prints: module1 assigned to thread: Thread-2
#   db2 = Database.get_db_instance()
#   db2.post("Module 2 data")

# run_io_tasks_in_parallel([
#     module1,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     module2,
#     # lambda: print('IO task 2 running!'),
# ])

# # t1 = Process(target=module1)
# # t1.start()
# # t2 = Process(target=module2)
# # t2.start()
# # t1.join()
# # t2.join()
  
# #print total number of Database instance created
# print(f"Database instance count: {Database.init_counter}") 
# #It will print: Database instance: 1
