foo = 12

try:
    bar = 12
    baz = 111
except Exception:
    pass


try:
    bar = 12
    baz = 111
except (FileNotFoundError, UnicodeDecodeError):
    pass
