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

    path = find_path(str_input).glob('*.epub')
    today = today_date()
    result = []

    for file in path:
        # get time info from the file
        date_created = datetime.fromtimestamp(file.stat().st_mtime)
        # convert time format to a subscriptable object
        date = str(date_created)

        if date[:10] == today :
            result.append(file)

    return result if result else 0
    
    # else:
    #     # return de la forme : ["path/to/file0", "path/to/file1", "path/to/file2"]
    #     return "pas de fichier aujourd'hui"


def move_file(file_list):

    files = [file for file in file_list]
    print(files)

    for file in files:

        to_path = Path(r"C:\Users\utilisateur\Desktop\Livres\epub_2023") / file.name
        print(f'moving file to... {to_path}')
        file.rename(to_path)   
        print('done')


def check_file_size(files):
    total_size_mb = 0
    for file in files:
        size_mb = file.stat().st_size / (1024 ** 2)
        print(f"{file}: {size_mb:.2f} MB")
        total_size_mb += size_mb
        
        
        if size_mb > 25:
            files.remove(file)
        
        if total_size_mb > 25: 
            pass


if __name__ == "__main__":
    # str_input = str(input('Path : ["telegram" ou "telechargement]: '))
    # files = get_epub_file(str_input)
    # # # print(files)

    # # # # today_date()
    # # move_file(str_input)
    # check_file_size(files)
    pass