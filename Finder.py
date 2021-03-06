import os
from sys import argv


def strip_quotes(word):
    return word.strip("\"").strip("\'").strip("‘").strip("’").strip("“").strip("”")


file_formats = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'drc', 'gifv', 'mng', 'avi', 'mov', 'qt', 'wmv', 'yuv', 'rm',
                'rmvb', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpe', 'mpv', 'mpeg', 'm2v', 'svi', '3gp',
                '3g2', 'mxf', 'roq', 'nsv', 'f4v', 'f4p', 'f4a', 'f4b', 'wma', 'mka', 'mks', 'divx', 'm2p', 'ps',
                'm2ts']

if len(argv) > 2:
    print("Unexpected number of arguments found", len(argv) - 1, "expected 1")
    print("Usage: Finder.py <FOLDER_PATH>")
    exit(1)

elif len(argv) < 2:
    print("Not enough arguments")
    print("Usage: Finder.py <FOLDER_PATH>")
    exit(1)

elif argv[1].lower() in ["--help", "-h", "-help", "-?", "/?", "/h", "help"]:
    print("Usage: Finder.py <FOLDER_PATH>")
    exit(1)

folder_path = argv[1]
print("Movie path set:", folder_path, "\n\n")
movie_folders = []

non_folder_movies = []

for x in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, x)):
        movie_folders.append(x)
    elif os.path.isfile(os.path.join(folder_path, x)) and x.split('.')[-1].lower() in file_formats:
        non_folder_movies.append(x)


def is_sample(filename):
    text = ""
    if "sample" in filename.lower():
        text = "  SAMPLE"
    return text


multi_folder = {}
empty_folders = []
for movie_folder in movie_folders:
    movie_file_list = []
    for full_folder, folder_names, file_names in os.walk(os.path.join(folder_path, movie_folder)):
        for a in file_names:
            if a.split('.')[-1].lower() in file_formats:
                movie_file_list.append(a)
    if len(movie_file_list) > 1:
        multi_folder[os.path.join(folder_path, movie_folder)] = movie_file_list
    elif len(movie_file_list) < 1:
        empty_folders.append(os.path.join(folder_path, movie_folder))

print("MOVIES WITH NO PARENT FOLDERS:")
longest_movie = 0
for movie in non_folder_movies:
    if len("\"" + os.path.join(folder_path, movie) + "\"") > longest_movie:
        longest_movie = len("\"" + os.path.join(folder_path, movie) + "\"")
for movie in non_folder_movies:
    movie_text = "\"" + os.path.join(folder_path, movie) + "\""
    print(movie_text + (" " * (longest_movie - len(movie_text))) + "  " + is_sample(movie))
print()

print("\nFOLDERS WITH MORE THAN ONE MEDIA FILE:")
for key, data in multi_folder.items():
    print("\"" + key + "\"")
    longest_x = 0
    for x in data:
        if len("- \"" + x + "\"") > longest_x:
            longest_x = len("- \"" + x + "\"")
    for x in data:
        print("- \"" + x + "\"" + (" " * (longest_x - len("- \"" + x + "\""))) + "  " + is_sample(x))
    print()

print("\nFOLDERS WITH NO MEDIA FILES IN THEM:")
for folder in empty_folders:
    print("- \"" + folder + "\"")
