text = 'fubar'


with open('text.bin', 'wb') as fh:
    fh.write(bytes(text, 'utf-8'))


with open('text.txt', 'w') as fh:
    fh.write(text)
