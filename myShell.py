import os #imports required for calls later on
import sys

#Left over testing to understand how cmdline text is read and parsed
#print ("Number of arguements:", len(sys.argv), "arguements.")
#print ("List: ", str(sys.argv))
#args = sys.argv
#print (args[1])
#print (os.getcwd())

#Python 3.5.0


## Still Left to do:
## Environ, Help, Echo(partial implementation started), DIR (displaying file in directory require)
## 2. Check assignment but it appears to deal with executing programs
## 3. Take commandline input from a file 

def main(): #Left over from initial start of program will remove later
    start()
def get_CLS(): #Works
    os.system('CLS')
def pause_term(): #works
    os.system('pause')
        

def get_directory(args): #needs to be fixed to display files
    try:
        direct = args[1]
    except IndexError:
        print("Current Directory", os.getcwd())

def change_directory(args): #does work, can be checked by getting directory
    try:
        os.chdir(args[1])
    except OSError as e:
        print >> sys.stderr, e
def get_echo(args):
    var = args[1]
    os.system("echo %s" %var)
    print(args)
    
def start(): 
    while(True): #loops until exit
        command = input("Please enter something: ") #needs to be changed to display directory at some point
        args = command.split()
        print (len(args))
        print ("List: ", str(args))
        #print("Entered", command)
        if args[0] == "exit":
            sys.exit()
        if args[0] == "dir":
            print("List: ",str(args))
            get_directory(args)
        if args[0] == "cd":
            change_directory(args)
        if args[0] == "clr":
            get_CLS()
        if args[0] == "pause":
            pause_term()
        if args[0] == "echo":
            get_echo(args)
        
main()        
