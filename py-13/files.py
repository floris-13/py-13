import os


def find_markdown_files(path):
    """
    Searches the given folder and subfolders for .md files and returns
    a list of full paths.

    :param path: The path to the root folder
    :return: List of the found .md-files
    """
    markdown_files = []
    for root, dirs, files in os.walk(path):
        for datei in files:
            if datei.lower().endswith('.md'):
                full_path = os.path.join(root, datei)
                markdown_files.append(full_path)
    return markdown_files


def string_to_file(path: str, content: str) -> str:

    """
    Schreibt einen String in eine Datei.

    :param path: Pfad und Dateiname der Datei
    :param content: Inhalt der Datei als String
    :return: sprechender Fehlertext oder OK
    """

    try:
        with open(path, 'w', encoding='utf-8') as datei:
            datei.write(content)
        return "OK"
    except FileNotFoundError:
        return "Fehler: Der angegebene Pfad wurde nicht gefunden."
    except PermissionError:
        return "Fehler: Keine Berechtigung zum Schreiben der Datei."
    except IsADirectoryError:
        return "Fehler: Der angegebene Pfad ist ein Verzeichnis, keine Datei."
    except Exception as e:
        return f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}"


def file_to_string(path):

    """
    Liest einen String aus einer Datei.

    :param path: Pfad und Dateiname der Datei
    :return: Inhalt der Datei als String oder "ERROR"
    """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception:
        return "ERROR"
