# py_cmake
 
Python scripts to aid in making C++ CMake projects.

## How to Use

### New Project
```
pymake.py -p <project_name> 
```
creates new project with name <project_name>.
### New Directory
```
pymake.py -p <directory_path_name> 
```
creates new directory at src/<directory_path_name>.
### New File
```
pymake.py -hpp <path_to_file/file_name> 
```
creates header source file including header guard with extension the hpp. 
```
pymake.py -cpp <path_to_file/file_name> 
```
creates C++ source file with extension cpp and adds it to the appopriate CMakeLists.txt file for compilation. 
