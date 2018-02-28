import sys
import re


old_file = new_file = sys.argv[1]

old_data = open(old_file).read()
blocks = old_data.split('\n\n\n')


def get_cls_name(block):
    line = block[0]
    if block[0].startswith('@'):
        line = block[1]
    try:
        if '(' in line:
            cls_name = line.split('class ')[1].split('(')[0]
        else:
            cls_name = line.split('class ')[1].split(':')[0]
        return cls_name
    except:
        print(block)
        print('0000000000000')


def replace_super(block):
    block = block.split('\n')
    cls_name = get_cls_name(block)
    replaced = False
    cont = False

    x = 'super({}, self)'.format(cls_name)
    y = 'super({}, cls)'.format(cls_name)

    new_block = ''
    for line in block:
        if x in line:
            new_line = line.replace(x, 'super()')
            replaced = True
            diff = len(line) - len(new_line) - len(cls_name) - len(', self')
            if diff != 0:
                print(diff, old_file, cls_name, line, new_line, sep='\n')
                print('--------------------------------------------')

        elif y in line:
            new_line = line.replace(y, 'super()')
            replaced = True
            diff = len(line) - len(new_line) - len(cls_name) - len(', cls')
            if diff != 0:
                print(diff, old_file, cls_name, line, new_line, sep='\n')
                print('--------------------------------------------')
        else:
            new_line = line

        new_block += new_line + '\n'
        if cont:
            new_block.lstrip()
            cont = False

    new_block = new_block.strip()
    return replaced, new_block


def has_class(block):
    block = block.split('\n')
    try:
        if (
                block[0].startswith('class ') or
                block[0].startswith('# ') and block[1].startswith('class ') or
                block[0].startswith('@') and block[1].startswith('class ')
        ):
            return True
    except:
        pass


new_data = ''

changed = False

for block in blocks:
    if has_class(block):
        replaced, block = replace_super(block)
        if replaced:
            changed = replaced
    new_data += block + '\n\n\n'

if not changed:
    sys.exit()

new_data = new_data.strip() + '\n'

test = True
test = not True

if test:
    # print(old_data)
    print('=====================')
    print(new_data)
else:
    open(new_file, 'w+').write(new_data)

# import difflib
# d = difflib.Differ()
# result = list(d.compare(data, new_file))
# from pprint import pprint; pprint(result)
