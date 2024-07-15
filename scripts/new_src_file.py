import datetime as dt

# if args.header:
def newHeader(cur_dir,file_path_name):
    filepath = f'{file_path_name}.hpp'
    if '/' in file_path_name:
        dir_file = file_path_name.split('/')
        filename = f'{dir_file[-1]}'
    else:
        filepath = f'src/{filepath}'
        filename = f'{file_path_name}'
    now = dt.datetime.now(dt.timezone.utc)
    header_numstr = now.strftime("%Y%m%d%H%M%S%f")
    header_guard = f"{filename.upper()}_HPP_{header_numstr}_INCLUDED"
    with open(f'{cur_dir}/{filepath}', 'w') as h:
        h.write(f'#ifndef {header_guard}\n')
        h.write(f'#define {header_guard}\n\n\n\n')
        h.write(fr'#endif // {header_guard}'+'\n')

# if args.cpp_file:
def newCpp(cur_dir, file_path_name):
    if '/' in file_path_name:
        dir_file = file_path_name.split('/')
        filename = f'{dir_file[-1]}.cpp'
        filepath = '/'.join(dir_file[:-1])
    else:
        filename = f'{file_path_name}.cpp'
        filepath = f'src'
    open(f'{cur_dir}/{filepath}/{filename}', 'w').close()
    with open(f'{cur_dir}/{filepath}/CMakeLists.txt', 'r') as f:
        file_data = f.read()
        is_included = (file_data.find(filename) > 0)
        print('read:',not is_included)
        if not is_included:
            data = file_data.replace(f'#\tEND_TARGET_SRCS',
                    f'\t{filename}\n#\tEND_TARGET_SRCS')
        if not is_included:   
            print('write:', not is_included)
            with open(f'{cur_dir}/{filepath}/CMakeLists.txt', 'w') as f:  
                f.write(data)



