foo = 12

try:
    bar = 12
except Exception:
    pass


try:
    bar = 12
except (FileNotFoundError, UnicodeDecodeError):
    pass
