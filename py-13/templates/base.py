
from config import Config
from files import *
import markdown


mainConfig = Config()


def compile_project(path: str):

    """
    Compiles source files to website files within the given project-folder.

    :param path: Path to the project folder.
    """

    # Load Config file and print initial compile text.

    config_file = path + "/config.txt"
    mainConfig.load_config_file(config_file)

    print(f'Welcome to py13 version 0.0.0.')
    print(f'Compiling project folder "{path}" containing version {mainConfig.get_py13_version()} with BASE template.\n')

    # Find markdown files

    markdown_files = find_markdown_files(path + "/" + mainConfig.get_source_folder())

    print(f'Found {len(markdown_files)} Markdown files to compile:\n')

    for markdown_file in markdown_files:

        # Read index.md from source folder

        content = file_to_string(markdown_file)

        print(f'Read source file: "{markdown_file}"')

        # Convert Markdown to HTML

        html = markdown.markdown(content)

        # Write index.html to website folder

        filename_without_extension = os.path.splitext(os.path.basename(markdown_file))[0]

        website_file = path + "/" + mainConfig.get_website_folder() + "/" + filename_without_extension + ".html"
        ret = string_to_file(website_file, html)

        print(f'Write website file: "{website_file}"')
        print(f'{ret}\n')

