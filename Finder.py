import os
from os.path import isfile, isdir, join

file_formats = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'drc', 'gifv', 'mng', 'avi', 'mov', 'qt', 'wmv', 'yuv', 'rm',
                'rmvb', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpe', 'mpv', 'mpeg', 'm2v', 'svi', '3gp',
                '3g2', 'mxf', 'roq', 'nsv', 'f4v', 'f4p', 'f4a', 'f4b', 'wma', 'mka', 'mks', 'divx', 'm2p', 'ps',
                'm2ts']

folder_path = input("Enter a folder path: ").strip("\"").strip("\'").strip("‘").strip("’").strip("“").strip("”")
good_ans = isdir(folder_path)
while not good_ans:
    print("Folder path not valid, try again...")
    folder_path = input("Enter a folder path: ").strip("\"").strip("\'").strip("‘").strip("’").strip("“").strip("”")
    good_ans = isdir(folder_path)

print("Movie path set:", folder_path, "\n\n")
movie_folders = []

non_folder_movies = []

for x in os.listdir(folder_path):
    if isdir(join(folder_path, x)):
        movie_folders.append(x)
    elif isfile(join(folder_path, x)):
        non_folder_movies.append(x)


def is_sample(filename):
    text = ""
    if "sample" in filename.lower():
        text = "  \033[93mSAMPLE\x1b[0m"
    return text


print("MOVIES WITH NO PARENT FOLDERS:")
for movie in non_folder_movies:
    print("\"" + join(folder_path, movie) + "\"" + is_sample(movie))
print()

multi_folder = {}
for movie_folder in movie_folders:
    movie_file_list = []
    for full_folder, folder_names, file_names in os.walk(join(folder_path, movie_folder)):
        for a in file_names:
            if a.split('.')[-1] in file_formats:
                movie_file_list.append(a)
    if len(movie_file_list) > 1:
        multi_folder[join(folder_path, movie_folder)] = movie_file_list
print("FOLDERS WITH MORE THAN ONE MEDIA FILE:")
for key, data in multi_folder.items():
    print("\"" + key + "\"")
    for x in data:
        print("- \"" + x + "\"", is_sample(x))
    print()