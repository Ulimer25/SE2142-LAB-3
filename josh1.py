def greet(name):
    return f"Hello, I am {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))