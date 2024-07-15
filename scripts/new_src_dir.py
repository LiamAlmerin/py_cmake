import os

def newCMakeDir(script_dir, dir_path_name):
    if '/' in dir_path_name:
        if not os.path.exists(dir_path_name):
            os.makedirs(f"{dir_path_name}")
        else:
            print(f"The directory '{dir_path_name}' already exists. " +
              "Overwriting CMake files")
    else:
        dir_path_name = 'src/' + dir_path_name
        if not os.path.exists(dir_path_name):
            os.makedirs(dir_path_name)
        else:
            print(f"The directory '{dir_path_name}' already exists. " +
              "Overwriting CMake files")
    with open(script_dir + '/data/src/CMakeLists.txt') as f:
        cmakelists_src_data = f.read()
    with open(f"{dir_path_name}/CMakeLists.txt", 'w') as f:
        f.write(cmakelists_src_data)
    if '/' in dir_path_name:
        dir_file = dir_path_name.split('/')
        par_dir_name = '/'.join(dir_file[:-1])
        dir_name = dir_file[-1]
    else:
        par_dir_name = 'src'
        dir_name = dir_path_name

    with open(f'{par_dir_name}/CMakeLists.txt', 'r') as f:
        file_data = f.read()
        is_included = (file_data.find(f'add_subdirectory({dir_name})') > 0)
        print('read:',not is_included)
        if not is_included:
            with open(f'{par_dir_name}/CMakeLists.txt', 'a') as f:
                f.write(f'add_subdirectory({dir_name})\n')
