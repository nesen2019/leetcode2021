import os
import glob
import argparse
import sys
import re

from cleetcode.configs import cfg
from cleetcode.scripts.utils import load_module 


def check_title(path_dir=None):
    path_dir = os.path.join(cfg.PATH_PROJECT, "cleetcode", "ctest")
    # print(path_dir, os.path.isdir(path_dir))
    path_list_py = glob.glob(os.path.join(path_dir, r"*.py"))
    path_list_py += glob.glob(os.path.join(path_dir, r"*/*.py"))
    path_list_py += glob.glob(os.path.join(path_dir, r"*/*.txt"))
    path_list_py += glob.glob(os.path.join(path_dir, r"*.txt"))
    # print(path_list_py)

    for i in path_list_py:
        basename = os.path.basename(i)
        if i.endswith(".txt"):
            i_new = os.path.splitext(i)[0]+".py"
            os.rename(i, i_new)
            i = i_new

        if basename.startswith("cL"):
            pass
        elif basename in ["all_test.py", "utils.py"]:
            pass
        else:
            module = load_module(i)
            if module.__doc__:
                idx = re.match(r"^\d*", module.__doc__.strip()).group()
                if idx:
                    print(i)
                    os.rename(i, os.path.join(os.path.dirname(i), f"cL{idx.zfill(4)}.py"))




if __name__ == '__main__':
    print(os.path.join(cfg.PATH_PROJECT, "cleetcode", "ctest"))
    check_title()


