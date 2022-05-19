import os


def find_directories(r):
    '''
    While we could have used os.walk to list dir tree, for the sake of recursion, used os.listdir which list all the files & dirs     inside the root.
    '''
    for file in os.listdir(r):
        d = os.path.join(r, file)

        # Base Case - when d is a file do nothin

        # Subprogram - when d is a dir, recurse
        if os.path.isdir(d):
            print(d)
            find_directories(d)


find_directories("/home/runner/Data-Structures-and-Algorithms")
