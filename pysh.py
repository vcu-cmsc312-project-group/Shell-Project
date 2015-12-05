#!/bin/python

import os
import sys
import io
import subprocess
## Still Left to do:
## Environ, Help 
## 2. Check assignment but it appears to deal with executing programs
## 3. Take commandline input from a file 

pwd = os.getcwd()

def prompt():
    return '[' + os.getlogin() + ' ' + pwd + ']$ '

def builtin_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def builtin_chdir(path):
    global pwd
    if path == None:
        print(pwd)
    else:
        try:
            os.chdir(path)
            pwd = os.getcwd()
        except OSError as e:
            print(e, file=sys.stderr)

def builtin_dir(path):
    try:
        contents = os.listdir(path)
        contents.sort()
        for f in contents:
            print(f)
    except OSError as e:
        print(e, file=sys.stderr)

def builtin_echo(txt):
    if txt is not None:
        print(txt)

def builtin_pause():
    sys.stdin.read(1)

def builtin_pwd():
    print(pwd)

def builtin_help():
    file = open("help.txt")
    print(file.read())

#def builtin_proc(args):
 #   try:
  #      proc = subprocess.Popen(args, executable = args[0], stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr)
  #  except OSError as e:
   #     print(e)
    #else:
     #   print("Executing child process", proc.pid)
      #  proc.wait()
        
def builtin_file(cmdargs):
    with open(cmdargs) as f:
        for line in f:
            line = line.strip()
            builtin_commandcall(line)

def builtin_commandcall(line):
    line = line.split(' ', 1)
    lines = line[1] if len(line) > 1 else None
    if line[0] == "quit":
        sys.exit()
    elif line[0] == "dir":
        builtin_dir(lines)
    elif line[0] == "cd":
        builtin_chdir(lines)
    elif line[0] == "clr":
        builtin_clear()
    elif line[0] == "pause":
        builtin_pause()
    elif line[0] == "echo":
        builtin_echo(lines)
    elif line[0] in ("help","-h"):
        builtin_help()
    

while(True):
    command = input(prompt())
    args = command.split(' ', 1)
    cmdargs = args[1] if len(args) > 1 else None
    print (cmdargs)
    if args[0] == "quit":
        sys.exit()
    elif args[0] == "dir":
        builtin_dir(cmdargs)
    elif args[0] == "cd":
        builtin_chdir(cmdargs)
    elif args[0] == "clr":
        builtin_clear()
    elif args[0] == "pause":
        builtin_pause()
    elif args[0] == "echo":
        builtin_echo(cmdargs)
    elif args[0] in ("help","-h"):
        builtin_help()
    elif args[0] == "myshell":
        builtin_file(cmdargs)