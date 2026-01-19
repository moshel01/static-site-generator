from textnode import *
import os
import shutil

def main():
    src = './static'
    dst = './public'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    recursive(src, dst)

def recursive(src, dst):
    children = os.listdir(src)
    for child in children:
        if os.path.isfile(os.path.join(src, child)):
            shutil.copy(os.path.join(src, child), dst)
        else:
            if os.path.exists(os.path.join(dst, child)) == False:
                os.mkdir(os.path.join(dst, child))
            recursive(os.path.join(src, child), os.path.join(dst, child))

if __name__ == "__main__":
    main()