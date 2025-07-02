
import importlib
import sys
import markdown
from files import *
from argparse import ArgumentParser
from config import Config


# py-13: Easy to use Templating Engine, that generates static websites from Markdown - written in Python.


# mainConfig = Config()


def compile_project(path: str):

    """
    Compiles source files to website files within the given project-folder.

    :param path: Path to the project folder.
    """

    mod = importlib.import_module("templates.base")
    mod.compile_project(path)


if __name__ == '__main__':

    # Parse command line arguments

    parser = ArgumentParser()
    parser.add_argument("-c", "--compile", help="compile files within the project directory",
                        action="store", metavar='PROJECT_DIR')
    parser.add_argument("-i", "--init", help="initialize a new project directory", action="store",
                        metavar='PROJECT_DIR')
    parser.add_argument('--version', action='version', version='%(prog)s version 0.1')
    args = parser.parse_args()

    # Console output

    print('\n')
    print('                            .o    .oooo.   ')
    print('                          o888  .dP""Y88b  ')
    print('   oo.ooooo.  oooo    ooo  888        ]8P\' ')
    print('    888\' `88b  `88.  .8\'   888      <88b.  ')
    print('    888   888   `88..8\'    888       `88b. ')
    print('    888   888    `888\'     888  o.   .88P  ')
    print('    888bod8P\'     .8\'     o888o `8bd88P\'   ')
    print('    888       .o..P\'                       ')
    print('   o888o      `Y8P\'                        ')
    print('\n')

    if args.compile:
        compile_project(args.compile)
        # print(f'Compiling project directory "{args.compile}".')
        # print("Oops ..Your wish is my command .. but sorry .. not yet implemented.")
    elif args.init:
        print(f'Initializing project directory "{args.init}".')
        print("Oops ..Your wish is my command .. but sorry .. not yet implemented.")
    else:
        print('Usage:\n')
        print('py13 compiles source-files within a given project directory into website-files within the same project '
              'directory. To do so, you need a .. project directory.\n')
        print('If you already have one and want to COMPILE the files it contains, please use:\n')
        print('py13.py -c path/to/your/existing_project_directory\n')
        print('If you don\'t have one yet, but want to create one or INITIALIZE an empty existing one, please use:\n')
        print('py13.py -i path/to/your/new_project_directory\n')
        print('Please visit py-13.website.fake to find out how go get started and for detailed documentation.\n')
