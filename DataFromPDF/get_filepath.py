import os

def get_names(root):
    file_paths_list = []
    for file_or_dir in os.listdir(root):
        full_path = os.path.join(root, file_or_dir)
        if os.path.isfile(full_path) and ((file_or_dir.endswith('.pdf'))):
            full_path = full_path.replace(os.sep, '/')
            file_paths_list.append(full_path)
        elif os.path.isdir(full_path):
            full_path = full_path.replace(os.sep, '/')
            file_paths_list.extend(get_names(full_path))
    return file_paths_list



'''
neu

def get_names(root):
    file_paths_list = []
    for file_or_dir in os.listdir(root):
        full_path = os.path.join(root, file_or_dir)
        if os.path.isfile(full_path) and file_or_dir.endswith('.pdf'):
            full_path = full_path.replace(os.sep, '/')
            file_paths_list.append(full_path)
        elif os.path.isdir(full_path):
            full_path = full_path.replace(os.sep, '/')
            file_paths_list.extend(get_names(full_path))
    return file_paths_list
'''








