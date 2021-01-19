import subprocess

with open('required_modules', 'r') as f:
    modules = f.readlines()

print('modules to check:')
for i in modules: print('\t',i)

pip=0
for i in modules:
    try:
        exec(f'import {i}')
    except:
        print(f'module {i} missing')
        if not pip: pip=input('press 3 to use pip3 ore press ENTER to use pip')
        subprocess.call(f'pip{pip} install {i}', shell=True)

print('all required modules are correctly installed')
