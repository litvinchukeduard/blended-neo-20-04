
users = []

def add_user(name: str) -> None:
    try:
        users.append(name)
        raise ValueError
    except ValueError:
        raise ValueError('Name is not valid')

def get_all_users() -> list[str]:
    return users
