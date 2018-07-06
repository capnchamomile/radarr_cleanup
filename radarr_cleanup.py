import os
from os import listdir, mkdir
from os.path import isfile, join, splitext

movies = # Enter the folder where your movies are
onlyfiles = [f for f in listdir(movies) if isfile(join(movies, f))]

for file in onlyfiles:    
    if (file.endswith('avi')) or (file.endswith('m4v')) or (file.endswith('mp4')) or (file.endswith('mkv')) or (file.endswith('divx')):
        mov_dir = os.path.splitext(movies + file)[0]
        os.mkdir(mov_dir)
        os.rename(movies + file, mov_dir + '/' + file)
        print('Movie file {} moved to {}'.format(file, mov_dir))
