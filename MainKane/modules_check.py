import subprocess

modules = [
    'colorama',
    'termcolor',
]

print('modules to check:')
for i in modules: print('\t',i)

for i in modules:
    try:
        exec(f'import {i}')
    except:
        print(f'module {i} missing')
        subprocess.call(f'pip install {i}', shell=True)

print('all required modules are correctly installed')
