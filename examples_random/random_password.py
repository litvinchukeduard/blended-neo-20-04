import random
import re
import string


source = "abcdefghijklmnopqrstuvwxyz"
password_symbols = f'A-Za-z0-9{string.punctuation}'
password_regexp = r"[" + password_symbols + "]{8,}"
# password_regexp = r"[\w]{8,}"

# Password: minimum 8 symbols
def check_password(password: str) -> bool:
    if not re.search(password_regexp, password):
        return False
    return True


# ord chr
# for position in range(ord('a'), ord('z') + 1):
#     print(chr(position), end='')

# "baad"
def get_random_value() -> str:
    return chr(random.randint(33, 126))

def random_password(n: int) -> str:
    password = ""
    for _ in range(n):
        password += get_random_value()
    return password

my_password = random_password(9)
print(my_password)
print('Password is correct:', check_password(my_password))
# print(string.punctuation)

