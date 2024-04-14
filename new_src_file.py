import argparse
import datetime as dt
import os


parser = argparse.ArgumentParser()
parser.add_argument("-hpp","--header", help="Creates hpp file with header guard",
                    action="store_true")
parser.add_argument("-cpp","--cpp_file", help="Creates cpp file",
                    action="store_true")
parser.add_argument("filename", help="Filename (with dir) used in creation")

args = parser.parse_args()

current_dir = os.getcwd()
if args.header:
    filepath = f'src/{args.filename}.hpp'
    if '/' in args.filename:
        dir_file = args.filename.split('/')
        filename = f'{dir_file[-1]}'
    else:
        filename = f'{args.filename}'
    now = dt.datetime.now(dt.timezone.utc)
    header_numstr = now.strftime("%Y%m%d%H%M%S%f")
    header_guard = f"{filename.upper()}_HPP_{header_numstr}_INCLUDED"
    with open(f'{current_dir}/{filepath}', 'w') as h:
        h.write(f'#ifndef {header_guard}\n')
        h.write(f'#define {header_guard}\n\n\n\n')
        h.write(fr'#endif \\ {header_guard}'+'\n')

if args.cpp_file:
    if '/' in args.filename:
        dir_file = args.filename.split('/')
        filename = f'{dir_file[-1]}.cpp'
        filepath = "src/"+"/".join(dir_file[:-1])
    else:
        filename = f'{args.filename}.cpp'
        filepath = f'src'
    open(f'{current_dir}/{filepath}/{filename}', 'w').close()
    with open(f'{current_dir}/{filepath}/CMakeLists.txt', 'r') as f:
        file_data = f.read()
        is_included = (file_data.find(filename) > 0)
        print('read:',not is_included)
        if not is_included:
            data = file_data.replace(f'#\tEND_TARGET_SRCS',
                    f'\t{filename}\n#\tEND_TARGET_SRCS')
        if not is_included:   
            print('write:', not is_included)
            with open(f'{current_dir}/{filepath}/CMakeLists.txt', 'w') as f:  
                f.write(data)



