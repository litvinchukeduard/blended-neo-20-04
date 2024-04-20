import save_data
import logging

def print_info():
    print(save_data.get_all_users())
    # INFO

def insert_info(name):
    try:
        save_data.add_user(name)
        # INFO
    except ValueError as e:
        # raise ValueError
        print(str(e))
        # ERROR

while True:
    command, *args = input(">>> ").split() # add Ihor 
    # command = 'add'
    # args = ['Ihor']
    if command == 'exit':
        break
    elif command == 'add':
        insert_info(args[0])
    elif command == 'all':
        print_info()


# try:
#     ...
# except FileNotFoundError:
#     ...
# except Exception:
#     ...