import os

def newCMakeProject(script_dir, project_name):
    if not os.path.exists(project_name + '/src'):
        os.makedirs(project_name + '/src')
    else:
        print(f"The directory '{project_name + '/src'}' already exists./n"+
              "Overwriting project files")

    with open(script_dir + '/data/CMakeLists.txt') as f:
        cmakelists_filedata = f.read().replace('default_project', project_name)
        cmakelists_filedata = cmakelists_filedata.replace('default_target', project_name)

    with open(project_name + '/CMakeLists.txt', 'w') as f:
        f.write(cmakelists_filedata)

    with  open(script_dir + '/data/CMakePresets.json') as f:
        presets_filedata = f.read()
    with open(project_name + '/CMakePresets.json', 'w') as f:
        f.write(presets_filedata)

    with open(script_dir + '/data/src/CMakeLists.txt') as f:
        cmakelists_src_data = f.read()
    with open(project_name + '/src/CMakeLists.txt', 'w') as f:
        f.write(cmakelists_src_data)
