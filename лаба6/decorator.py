def require_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Введіть пароль для доступу до функції: ")

            if password == correct_password:
                return func(*args, **kwargs)
            else:
                print("Доступ заборонено: неправильний пароль.")
                return None
        return wrapper
    return decorator
