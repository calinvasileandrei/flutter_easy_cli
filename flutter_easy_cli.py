import argparse # Add the argparse import
import subprocess
import os, fnmatch

gitRepo = 'https://github.com/calinvasileandrei/flutter_easy_start'


def create_project(name,company):
    print('Process Started')
    initProcess(name,company)
    findReplace(name+'/lib','flutter_easy_start',name,'*.dart')
    singleFileReplace(name+'/pubspec.yaml','flutter_easy_start',name)
    print('Name changed to ',name)
    endProcess(name)
    print('Done!')

def initProcess(name,company):
    print("App Name: ",name)
    subprocess.run(["bash", "flutter", "create", "--org", company, name])

    subprocess.call("git clone "+gitRepo, shell=True)
    # Remove unnecessary files
    subprocess.call("rm -rf "+name+"/lib", shell=True)
    subprocess.call("rm "+name+"/test/widget_test.dart", shell=True)
    subprocess.call("rm -rf "+name+"/pubspec.yaml", shell=True)
    # Import the files fromt the starter
    subprocess.call("mv flutter_easy_start/lib "+name, shell=True)
    subprocess.call("mv flutter_easy_start/assets "+name, shell=True)
    subprocess.call("mv flutter_easy_start/pubspec.yaml "+name, shell=True)
    subprocess.call("mv flutter_easy_start/.env "+name, shell=True)
    # Remove the cloned directory
    subprocess.call("rm -rf flutter_easy_start", shell=True)

def endProcess(name):
    print('Flutter updating packages')
    commands = '''
    cd ''' +name+'''
    flutter pub get 
    flutter pub upgrade
    '''
    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print(out.decode('utf-8'))
    print('Flutter upgraded!')

# Helper methods
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


#------------------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Create a new Flutter project based on a custom template on git')
parser.add_argument('--name', default="example_project", help="the project name")
parser.add_argument('--company', default="com.example", help="the company name")

args = vars(parser.parse_args())

if(args['name'] == '' or args['name'] == None):
    print('Error: Please pass a valid name parameter!')
elif(args['company'] == '' or args['company'] == None):
    print('Error: Please pass a valid company parameter!')
else:
    if(not args['name'].islower() or not args['company'].islower() ):
        print('Error: Project name must be lower case with underscores and the company name should be also in lowercase')
    else:
        create_project(args['name'],args['company'])