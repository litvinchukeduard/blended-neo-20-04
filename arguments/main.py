def funct(arg_one, arg_two, arg_three):
    if arg_one == 0:
        print('Error!')
        return
    arg_two / arg_one

def funct_two(arg_one, arg_two, arg_three):
    """arg_two should be less than arg_one"""
    # 4, 2
    result = []
    for i in range(arg_one, arg_two):
        pass
    
# isinstance
# type

def funct_three(arg_one: int, arg_two, arg_three):
    """
        - arg_one: int
    """
    if type(arg_one) != int:
        print(...)