import pypandoc
from pypandoc.pandoc_download import download_pandoc

FILE_COUNT = 1


def save_file(text):
    global FILE_COUNT
    with open(f"file_{FILE_COUNT}", "w", encoding="utf-8") as file:
        file.write(text)
        file.close()
    FILE_COUNT += 1


def simple_doc_converter(text):
    """
    TBD
    :param text:
    :return:
    """
    return text
