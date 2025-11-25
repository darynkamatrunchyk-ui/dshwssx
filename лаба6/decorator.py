def require_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Enter password to access the function: ")

            if password == correct_password:
                return func(*args, **kwargs)
            else:
                print("Access denied: incorrect password.")
                return None
        return wrapper
    return decorator
