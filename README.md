# py_cmake
 
Python scripts to aid in making C++ CMake projects.

## How to Use

### New Project
```
pymake.py -p -n=<project_name> 
```
creates new project with name <project_name>.
### Add .gitignore
```
pymake.py -i -n=<directory_path_name> 
```
Adds .gitignore in <directory_path_name>. One can optionally add the -i, when making a new project.
```
pymake.py -i
```
Adds .gitignore in current directory.
### New Directory
```
pymake.py -p -n=<directory_path_name> 
```
creates new directory at src/<directory_path_name>.
### New File
```
pymake.py -hpp -n=<path_to_file/file_name> 
```
creates header source file including header guard with extension the hpp. 
```
pymake.py -cpp -n=<path_to_file/file_name> 
```
creates C++ source file with extension cpp and adds it to the appopriate CMakeLists.txt file for compilation. 
