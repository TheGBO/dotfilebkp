#!/bin/python3
# Script to take a snapshot of the dotfiles
from pathlib import Path
#Base dump directory for dotfiles and configs
DUMP_ROOT = './dump/'

#these args are file paths.
def open_and_dump(open_file, dump_file):
    content = ''
    try: 
        with open(Path(open_file).expanduser()) as f:
            content = f.read()
            f.close()

        with open( Path(f'{DUMP_ROOT}{dump_file}').expanduser(), 'w') as f:
            f.write(content)
            f.close()
            print(f'{open_file} was successfully synced and dumped as {dump_file}')
    except Exception as e:
        print(f'File or path {open_file} might not even exist to be honest vro...')

def main():
    #dump bashrc
    open_and_dump('~/.bashrc', 'bashrc')
    #dump i3wm
    #open_and_dump('~/.config/i3/config', 'i3wmconfig')

if __name__ == '__main__':
    main()
