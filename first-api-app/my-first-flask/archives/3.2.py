users = ["Alice", "Bob", "Charlie"]

def get_user(index):
    try:
        return users[int(index)]
    except ValueError:
        return {"ERROR": f"{index} must be a number"}
    except IndexError:
        return "User index out of range"

user_index = input("Enter user index: ")
user = get_user(user_index)

print("Selected user:", user)
