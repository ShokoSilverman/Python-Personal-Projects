from Imports.importHelloWorld import test_hello_world # imports a single func but keeps name
from Imports.importHelloWorld import hello_user as user_hello # imports a single func and alias' it
from Imports import anotherImportTest as full_import_file # imports the whole file, keeping original func names




def main():
    test_hello_world()
    user_hello(input('what is your name: '))
    full_import_file.info()


#use this if it is the main program running, if it is used as an import this wont run
if __name__ == '__main__':
    print('running!')
    main()