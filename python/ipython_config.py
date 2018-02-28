# flake8: NOQA

import os


home = os.environ['HOME']


c.InteractiveShellApp.extensions = ['autoreload']

c.InteractiveShellApp.exec_lines = ['%autoreload 2', '%autocall	1']

c.TerminalInteractiveShell.confirm_exit = False

c.InteractiveShellApp.exec_files = [os.path.join(home, 'projects/eddie/python/ipython_init.py')]
