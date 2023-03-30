from pathlib import Path
from datetime import datetime


def today_date():
    #%Y-%m-%d to match file.stat() time
    today = datetime.today().strftime('%Y-%m-%d')

    return today


def find_path(str_input)->Path:
    if str_input == "telegram":
        path = Path(r"C:\Users\utilisateur\Downloads\Telegram Desktop")
    elif str_input == "telechargement":
        path = Path(r"C:\Users\utilisateur\Downloads")

    return path


def get_epub_file(str_input) ->list:

    path = find_path(str_input).glob('*.pdf')
    today = today_date()
    result = []

    for file in path:
        # get time info from the file
        date_created = datetime.fromtimestamp(file.stat().st_mtime)
        # convert time format to a subscriptable object
        date = str(date_created)

        if date[:10] == today :
            result.append(file)

    return result
    
    # else:
    #     # return de la forme : ["path/to/file0", "path/to/file1", "path/to/file2"]
    #     return "pas de fichier aujourd'hui"


def move_file(str_input):
    file_list = get_epub_file(str_input)
    files = [file for file in file_list]
    print(files)

    for file in files:

        to_path = Path(r"C:\Users\utilisateur\Desktop\Livres\epub_2023") / file.name
        print(f'moving file to... {to_path}')
        file.rename(to_path)   
        print('done')


# str_input = str(input('Path : ["telegram" ou "telechargement]: '))
# # files = get_epub_file(str_input)
# # print(files)

# # # today_date()
# move_file(str_input)
