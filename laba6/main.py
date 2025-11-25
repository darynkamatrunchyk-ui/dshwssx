from decorator_auth import require_password

@require_password("12345")
def secret_info():
    return "This is top-secret information!"

@require_password("pass")
def add(a, b):
    return a + b
