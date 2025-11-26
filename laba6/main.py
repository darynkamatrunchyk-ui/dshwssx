from decorator import require_password

@require_password("12345")
def secret_info():
    return "Це надсекретна інформація!"

@require_password("pass")
def add(a, b):
    return a + b
