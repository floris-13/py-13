from argparse import ArgumentParser

# py-13: Easy to use Templating Engine, that generates static websites from Markdown - written in Python.


if __name__ == '__main__':

    # Parse command line arguments

    parser = ArgumentParser()
    parser.add_argument("-c", "--compile", help="compile files in the project directory (default)", action="store_true")
    parser.add_argument("-i", "--init", help="initialize the project directory", action="store_true")
    parser.add_argument("project_directory", type=str, help="path to the project directory")
    args = parser.parse_args()

    print('\n')
    print('                         .o    .oooo.   ')
    print('                       o888  .dP""Y88b  ')
    print('oo.ooooo.  oooo    ooo  888        ]8P\' ')
    print(' 888\' `88b  `88.  .8\'   888      <88b.  ')
    print(' 888   888   `88..8\'    888       `88b. ')
    print(' 888   888    `888\'     888  o.   .88P  ')
    print(' 888bod8P\'     .8\'     o888o `8bd88P\'   ')
    print(' 888       .o..P\'                       ')
    print('o888o      `Y8P\'                        ')
    print('\n')

    if args.compile:
        print('COMPILE selected. Your wish is my command .. but sorry .. not yet implemented.')

    if args.init:
        print('Project INITIALIZATION selected. Your wish is my command .. but sorry .. not yet implemented.')

    print(f'Chosen project directory: "{args.project_directory}".')

