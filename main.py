import argparse # Add the argparse import
import subprocess
import os, fnmatch



def create_project(name):
    print('Process Started')
    subprocess.run(["bash", "./shell_init.sh",name])
    findReplace(name+'/lib','flutter_starter',name,'*.dart')
    findReplace(name+'/test','flutter_starter',name,'*.dart')
    singleFileReplace(name+'/pubspec.yaml','flutter_starter',name)
    print('Name changed to ',name)
    subprocess.run(["bash", "./shell_end.sh",name])
    print('Done!')


def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

def singleFileReplace(fileName,find,replace):
    # Read in the file
    with open(fileName, 'r') as file:
        filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(find, replace)
    # Write the file out again
    with open(fileName, 'w') as file:
        file.write(filedata)

parser = argparse.ArgumentParser(description='Create a new Flutter project based on a custom template on git')
parser.add_argument('--name', default="example_project", help="the project name")

args = vars(parser.parse_args())
if(args['name'] == '' or args['name'] == None):
    print('Error: Please pass a valid name parameter!')
else:
    if(not args['name'].islower()):
        print('Error: Project name must be lower case with underscores')
    else:
        create_project(args['name'])