#! /usr/bin/env python3
import scripts.new_src_file as nsf
import scripts.new_cxx_project as ncp
import scripts.new_src_dir as nsd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-hpp","--header", help="Creates hpp file with header guard",
                    action="store_true")
parser.add_argument("-cpp","--cpp_file", help="Creates cpp file",
                    action="store_true")
parser.add_argument("-p","--new_project",  help="Creates new project", 
                    action="store_true")
parser.add_argument("-d","--new_src_directory",  help="Creates a new directory under src along with CMakeLists.txt file", 
                    action="store_true")
parser.add_argument("-i","--ignore",  help="Adds .gitignore file to directory", 
                    action="store_true")
parser.add_argument("-n","--name", required=False)
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.getcwd()

if args.new_project:
    ncp.newCMakeProject(script_dir, args.name)
if args.new_src_directory:
    nsd.newCMakeDir(script_dir, args.name)
if args.header:
    nsf.newHeader(current_dir, args.name)
if args.cpp_file:
    nsf.newCpp(current_dir, args.name)
if args.ignore:
    with  open(script_dir + '/data/.gitignore') as f:
        ignore_filedata = f.read()
    if args.name:
        with open(args.name + '/.gitignore', 'w') as f:
            f.write(ignore_filedata)
    else:
        with open('.gitignore', 'w') as f:
            f.write(ignore_filedata)
