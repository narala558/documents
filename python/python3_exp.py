# coding: utf-8
import sys
print(sys.version)




# float
x = float('inf')
print(x)
print(x+1)


# round to 2 points
round(2.333, 2)

# fraction
from fractions import Fraction





# string

print('foo'.title())

# print Numbers with leading zero
print(str(1).zfill(2))
print(['{i:04d}'.format(i=i) for i in range(10)])


# strip all spaces
''.join(' \n ff \n bar \t '.split())
'test.py'.startswith('test')
'test.py'.endswith('.py')

# generate random string of given `length`.
import random
import string
print(''.join(random.choice(string.ascii_letters) for _ in range(10)))


# check if a list of words in another string
list_ = ['one', 'foo']
if any(word in 'some one long two phrase three' for word in list_):
    print(list_)






# dict
foo = 1
bar = 2

# create dict from variables
d = dict(((k, globals()[k]) for k in ('foo', 'bar')))

# sort dict based on value
# import operator
# sorted(d.iteritems(), key=operator.itemgetter(1))






# lists

# reverse a list
l = ["foo", "bar", "baz"]
print(l[::-1])

# index of an item in a list
print(l.index('bar'))

# reverse a list with index also
list(reversed(list(enumerate(l))))



# list comprehension doesn't leak variable
x = 2
y = [x for x in l]
print(x)






# tuples
# Tuples are immutable and usually contains heterogeneous sequence of elements






# files

# path and name of current file
os.path.realpath(__file__)

# line count
test_file = './foo.txt'
print(sum(1 for line in open(test_file)))
print(len(open(test_file).read().splitlines()))


# read file into string
data = open(test_file).read()
print(data)















# builtins


# zip, unzip
print(list(zip('asdf', range(4))))


# property
class Author:
    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

a = Author('john', 'doe')
a.fullname



# vars

# with argument returs __dict__ of object
def foo():
    pass
vars(foo)

# without arguments, it acts like locals
vars()












# use print with repr
x, y = 5, '5'
print(x, y)
print(repr(x), repr(y))


# nested ternary
a, b = 3, 4
print(1 if a > b else -1 if a < b else 0)

a, b = 3, 3
print(1 if a > b else -1 if a < b else 0)




# list of subclasses
class Foo:
    pass


class Bar(Foo):
    pass


Bar.__subclasses__()





x, y = 3, 31
# never use operators for singleton variable.
print(x is not y)


# null check
print(x is None)

# identity check
print(x is y)


# equality check
print(x == y)
print(id(x), id(y))

try:
    1 / 0
except:
    print('exception')
else:
    print('no exception')
finally:
    print('done')









# locals, globals, vars
"""
Python uses namespaces to keep track of variables.

local-namespace - specific to current func/method. read only

global-namespace - specific to current module, read/write

builtin-namespace - global to all modules

If locals() is called inside a function it constructs
a dictionary of the function namespace as of that moment and returns it.
Further name assignments are not reflected in the returned dictionary,
and any assignments to the dictionary are not reflected
in the actual local namespace.

If locals() is called outside a function it returns the
actual dictionary that is the current namespace.
Further changes to the namespace are reflected in the dictionary,
and changes to the dictionary are reflected in the namespace.


vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__.
"""













# unicode

t_string = "python"
print(type(t_string))

t_bytes = b'python'
print(type(t_bytes))

t_unicode = u'python'
print(type(t_unicode))


for i in range(0xC00, 0xC7F):
    print(chr(i))


s = 'café'
print(len(s))


b = s.encode('utf8')
print(b)
print(len(b))


# U+00E1
s = 'Ω'
s.encode('utf-8')
# invalid conversion
s.encode('ascii')


# builtins

# convert dec to hex & vice versa
print(hex(122))
print(int('7a', base=16))
print(int('0x7a', base=16))
print(int('0x7a', base=0))




# generators

# unpacking generator inside a list
g1 = (x for x in range(3))
g2 = (x**2 for x in range(2))
x = [1, *g1, 2, *g2]
print(x)












# functions

def test_func(**kwargs):
    print(kwargs)

test_func(option1='new_value1', option3='new_value3')
test_func(option2='new_value2')


def foo(**kwargs):
    test_func(**kwargs)
    print(kwargs)


def kw_only(**options): print(options)


foo(x=1)





















# standard library
import standardlibrary

# list standard libary modules
import sys
print(sys.builtin_module_names[30:35])

# list standard libary modules
from stdlib_list import stdlib_list
libraries = stdlib_list("3.5")
print(libraries[4:10])

# find operating system type
print(sys.platform)







import argparse
# boolean
parser.add_argument('-a', action="store_true", default=False)






import bisect


a = [12, 35, 4, 58, 6, 48, 98]
a = sorted(a)
index = bisect.bisect(a, 50)

bisect.insort(a, 50)






# collections
import collections

isinstance(dict, collections.Hashable)


d = collections.deque(range(5))
d.rotate(1)
print(d)
d.rotate(-1)
print(d)


c = collections.Counter('aaaaadeeeetadf')

collections.namedtuple










import configparser


config = configparser.ConfigParser()
CONFIG_FILE = os.path.expanduser('~/.config/foo.ini')
config.read(CONFIG_FILE)

try:
    section = config[name]
except KeyError:
    section = None

config['data'] = {'path': '/tmp/foo'}

config.remove_section('data')

with open(CONFIG_FILE, 'w') as fh:
    config.write(fh)







# contextlib

from contextlib import contextmanager


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

print(os.getcwd())
with cd('/tmp'):
    print(os.getcwd())



# copy

# shallow copy
# content is not copied by value, but just creating a new reference.
a = {1: [1,2,3]}
b = a.copy()
print(a, b)
a[1].append(4)
print(a, b)

import copy
c = copy.deepcopy(a)
print(a, c)
a[1].append(5)
print(a, c)









# datetime
import datetime

now = datetime.datetime.now()
print(now)


print(datetime.datetime.strftime(now))

d = '05 Oct 2017 10:27 AM'
dt.datetime.strptime(d, '%d %b %Y %H:%M %p')


month = datetime.timedelta(days=31)
after_month = now + month
print(after_month)

# week_of_the_year
year, week, day = now.isocalendar()










# enum
from enum import IntEnum

class Shape(IntEnum):
    circle = 1
    square = 2

print(Shape.circle.name)
print(Shape.circle.value)

class CommandsEnum(IntEnum):
    forward = 1
    reverse = 2

    @classmethod
    def choices(cls):
        return [i for i in cls._value2member_map_]







# functools
import functools

detros = functools.partial(sorted, reverse=True)

a = [4, 1, 2]
print(detros(a))


reduce(add, [1, 2, 3], 200)
# calculates 200 + 1, 201 + 2, 203 + 3













# glob
import glob

print(glob.glob("/foo/*.pdf"))







# gc
import gc
objects = gc.get_objects()
print(len(objects))














# itertools
import itertools

#nested list to list
n = [[1, 2], [3, 4]]
print(list(itertools.chain.from_iterable(n)))
print(list(itertools.chain(*n)))

a, b = [1, 2], [3, 4]
list(itertools.product(a, b))



def chunker(iterator, size):
    return (iterator[pos:pos+size] for pos in range(0, len(iterator), size))

for chunk in chunker('foobar', size=2):
    print(chunk)






import inspect

# print function source code
def foo():
    return 'foo'


print(inspect.getsource(foo))






# json
import json

d = ['foo', {'bar': ['baz', None, 1.0, 2]}]
j = json.dumps(d)
print(type(j), j)

y = json.loads(j)
print(type(y), y)


json_file = './exercise/test.json'
with open(json_file, 'w') as fp:
    json.dump(j, fp)

x = json.load(open(json_file))
print(type(x), x)


from collections import namedtuple
def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

x = json2obj(x)
print(type(x), x)









# logging
import logging

# set log level
logging.getLogger("urllib3").setLevel(logging.WARNING)


# find all loggers
for key in logging.Logger.manager.loggerDict:
    print(key)



FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(FORMAT)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)

    logger.addHandler(sh)

    return logger





# pickle
import pickle


network = {'wih': 1, 'who': 2}
network_file = 'network.pkl'

with open(network_file, 'wb') as fh:
    pickle.dump(network, fh)

with open(network_file, 'rb') as fh:
    network = pickle.load(fh)
print(network)









# tracemalloc
import tracemalloc
tracemalloc.start(5)
snap1 = tracemalloc.take_snapshot()
x = 10
snap2 = tracemalloc.take_snapshot()
stats = snap2.compare_to(snap1, 'lineno')
print(len(stats))

for i in stats[:3]:
    print(i)











# tempfile
import tempfile






# math
import math

# compute angle from co-ordinates
math.atan2(y, x)









# mock
from unittest.mock import Mock
from unittest.mock import MagicMock

thing = ProductionClass()
thing.method = MagicMock(return_value=3)








# multiprocessing
import multiprocessing


def foo(name):
    while True:
        print(name)

process = multiprocessing.Process(target=foo, kwargs={'name': 'foooooo'})
process.start()

os.kill(process.pid, signal.SIGTERM)







# os
import os

print(os.listdir('.'))

test_file = '/tmp/foo.txt'
print(os.path.split(test_file))
print(os.path.splitext(test_file))


os.path.abspath(test_file)

os.rename('foo', 'bar')

os.path.isfile(test_file)

os.path.exists(test_file)
os.path.dirname(test_file)
os.path.getsize(test_file)

os.system('ls')
os.remove(filename)



# env variables
foo = os.environ('FOO')
foo = os.environ.get('FOO')
foo = os.environ.get('FOO', 'default')
foo = os.getenv('FOO', )

for dir_name, subdir, files in os.walk(root_dir):
    print(dir_name, subdir)
    for fname in files:
        print(fname)





# pprint

import traceback
def prvar(__x):
    print(traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x)


# pretty print a object.
from pprint import pprint
d = {1:2, 3:4}
pprint(d, width=1)






# random
import random

num = random.randint(1, 5)
print(num)




# re
import re

# strip all whitespaces
pattern = re.compile(r'\s+')
print(pattern.sub('', ' \t foo \n bar \n '))

print(re.findall(r'\d+', 'hello 42 I\'m a 32 string 30'))

pattern = re.compile('(?P<year>\d{4})')
match = pattern.search('may 2013')
print(match.group('year'))


match = re.search('foo', 'bar foo bar', re.IGNORECASE)
if match:
    print(match.group())







import shelve

shelve.open()







# shutil
import shutil

# move files even between disks
shutil.move('foo.py', '/home/chillaranand/')








import subprocess


# run a command
cmd = 'ls -ll'
cmd = cmd.split()
print(subprocess.check_output(cmd))


# hide output
FNULL = open(os.devnull, 'w')
out = subprocess.check_output(cmd, stderr=FNULL)
print(out.decode('utf-8'))


# escape quotes
cmd = "find . -name '*.py' | xargs autopep8 -i"
subprocess.check_output(shlex.split(cmd), shell=True)


# run in background
p = subprocess.Popen(["python", "-m", "http.server"])

















# sys
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))

print(sys._getframe().f_code.co_name)


class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind





# weakref

import weakref
stock = weakref.WeakValueDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
print(sorted(stock.keys()))


del catalog
print(sorted(stock.keys()))


del cheese
print(sorted(stock.keys()))



# zipfile
import zipfile
zipfile.ZipFile()












# third party libraries
import thirdpartylibraries


# reloading a module

# py 2.x
# reload(module)

# py 3.3
#imp.reload(module)






# frida
import frida

devices = frida.enumerate_devices()






# github
import github3

user = 'chillaranand'
repo = 'test'

gh_client = github3.login(token=os.environ['GITHUB_TOKEN'])
repo = gh_client.repository(owner='chillara nand', repository='test')

issues = repo.iter_issues(state='all')

r = repo.create_issue(title="aa", body="bb")






# jira











# matplotlib

# In[2]:

data = [
    '2008 70372           332383',
'2009 394567          1188382',
'2010 820161          1763772',
'2011 1445142         2657936',
'2012 2065664         3328785',
'2013 2759442         3969998',
'2014 3040440         3801302',
'2015 3105720         3704174',
'2016 1238114         1438269',
]

data = [i.split() for i in data[:-1]]
y = [int(i[0]) for i in data]
q = [int(i[1]) for i in data]
a = [int(i[2]) for i in data]

users = [
    '2008 21721',
'2009 78410',
'2010 201260',
'2011 362061',
'2012 727722',
'2013 1130602',
'2014 1185788',
'2015 1271272',
'2016 589196',

]
uu = [i.split() for i in users[:-1]]
u = [int(i[1]) for i in uu]


# In[11]:

import matplotlib.pyplot as plt

x = np.arange(10)

plt.xticks(y, y)
plt.plot(y, a)
plt.plot(y, q)
print(x,y,a,q)
plt.legend(['Answers', 'Questions',], loc='upper left')

plt.show()


# In[14]:

x =  [i for i in range(0, 40, 4)]
x.insert(1, 1)
print(x)


# In[33]:

x = [20, 24, 28, 32, 36]

xargs_t = [25.3, 19.2, 13, 13, 16.3]
xargs_c = [8, 12, 16, 15, 13]

para_t = [16, 12, 18, 20, 31]
para_c = [35, 48, 33, 29, 19]

py_t = [24,30,12,20,35]
py_c = [19, 15, 36, 23, 13]

plt.xticks(x, x)

plt.gca().set_color_cycle(['red', 'red', 'green', 'green', 'blue', 'blue'])

plt.plot(x, sh1_t)
plt.plot(x, para_t)
#plt.plot(x, py_t)

plt.plot(x, sh1_c)
plt.plot(x, para_c)
#plt.plot(x, py_c)

plt.legend(['xargs_time', 'xargs_cpu', 'para_time', 'para_cpu', 'py_time', 'py_cpu'],
           loc='upper left')

plt.show()


# In[7]:

import matplotlib.pyplot as plt

plt.xticks(y, y)
plt.plot(y, u)

plt.legend(['New Users'], loc='upper left')

plt.show()


# In[4]:

import matplotlib.pyplot as plt

N = 8
menMeans = q

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
print(y)
fig, ax = plt.subplots()
rects1 = ax.bar(ind, y, width, color='r')

womenMeans = a

rects2 = ax.bar(ind + width, womenMeans, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(y)

ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show()


# In[31]:

fig = plt.figure()

width = .35

plt.bar(y, a, width=width)
#plt.xticks(ind + width / 2, OX)

plt.show()


# ## nltk
#

# In[ ]:

import nltk
s = "foo!! bar's"
print(nltk.word_tokenize(s))












# redis


# pub/sub pattern

# publisher
# ./exercise/pub.py

# subscriber
# ./exercise/sub.py








# requests
import requests

url = 'http://avilpage.com'

r = requests.get(url=url)
with open('foo.html', 'wb') as fh:
    fh.write(r.content)

# form data
data = {'foo': 'bar'}
r = requests.post(url=url, data=data)


# headers
headers = {'content-type': 'application/json'}
r = requests.post(url, headers=headers)


# cookies
cookie = {'foo_session': '17ab96bd8ffbe8ca58a78657a918558'}
r = requests.post('http://wikipedia.org', cookies=cookie)


# disable logging
logging.getLogger("requests").setLevel(logging.WARNING)








# scikit image

# skew correction
from skimage import io
from skimage import transform as tf

# Load the image as a matrix
image = io.imread("/path/to/your/image.jpg")

# Create Afine transform
afine_tf = tf.AffineTransform(shear=0.2)

# Apply transform to image data
modified = tf.warp(image, afine_tf)

# Display the result
io.imshow(modified)
io.show()



# sendgrid

from sendgrid import Mail, SendGridClient


def get_template_id_by_name(template_name):
    response = sg.client.templates.get()
    data = json.loads(response.response_body.decode())
    t_groups = data['templates']

    for t_group in t_groups:
        templates = t_group['versions']
        for template in templates:
            if template['name'] == template_name:
                return t_group['id']


template_id = get_template_id_by_name(template_name)

message = Mail()
message.add_filter('templates', 'enable', '1')
message.add_filter('templates', 'template_id', template_id)
message.set_subject(None)
for to_addr in to_addrs:
    message.add_to(to_addr)
for key, value in context.items():
    message.add_substitution("%{}%".format(key), value)
message.set_from('Foo <foo@bar.com>')
message.set_html('  ')
message.set_text('  ')
message.set_subject('  ')












# scrapy

# xpath selection

# find td with `dc.identifier.uri` as text and get text of its sibling
url = response.xpath('//td[contains(., "dc.identifier.uri")]/following-sibling::td/text()')

# find element with class `file-link` and get `href` of `a` inside it
pdf = response.xpath('//*[contains(@class, "file-link")]//a/@href')



from pygments.lexers import guess_lexer, guess_lexer_for_filename
guess_lexer('#!/usr/bin/python\nprint "Hello World!"')
guess_lexer_for_filename('test.py', 'print "Hello World!"')




# porting 2 to 3





# others
# Convert xls to txt file

import xlrd
workbook = xlrd.open_workbook('data.xls')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows
num_cells = worksheet.ncols
curr_row = -1

with open("xxx.txt", "w") as fh:
    for row in range(num_rows):
        for column in range(num_cells):
            print worksheet.cell_value(row, column)
            fh.write("\n")



# suppress stdout
import contextlib
import sys


@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    yield
    sys.stdout = save_stdout
