import os
def get_filename(path):
    return os.path.basename(path)
def get_name_without_ext(path):
    return os.path.splitext(os.path.basename(path))[0]
path = r"d:https://www.youtube.com/hashtag/jackj97"
print(get_filename(path))
print(get_name_without_ext(path))