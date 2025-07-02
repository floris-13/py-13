
from config import Config
from files import *
import markdown


mainConfig = Config()


def compile_project(path: str):

    """
    Compiles source files to website files within the given project-folder.

    :param path: Path to the project folder.
    """

    # Load Config file and read Version Info

    config_file = path + "/config.txt"
    mainConfig.load_config_file(config_file)

    print(f'Loaded config file: "{config_file}"')
    print(f'py13 Version is "{mainConfig.get_py13_version()}"')

    # Find markdown files

    markdown_files = find_markdown_files(path + "/" + mainConfig.get_source_folder())

    print("Found these Markdown files:")
    for markdown_file in markdown_files:
        print(markdown_file)

    # Read index.md from source folder

    source_file = path + "/" + mainConfig.get_source_folder() + "/index.md"
    content = file_to_string(source_file)

    print(f'Read source file: "{source_file}"')
    print(f'It contains: "{content}"')

    # Convert Markdown to HTML

    html = markdown.markdown(content)

    # Write index.html to website folder

    website_file = path + "/" + mainConfig.get_website_folder() + "/index.html"
    ret = string_to_file(website_file, html)
    print(f'Write website file: "{website_file}"')
    print(f'It contains: "{html}"')
    print(f'Write returned: "{ret}"')

    # Hello World

    print(f'Hello World, I\'m the base template, working now on path: "{path}"')
