import sys 
import os
import re
import glob
from cleetcode.configs import cfg


def load_module(file_path, module_name=None):
    """
    Load a module by name and search path

    This function should work with python 2.7 and 3.x

    Returns None if Module could not be loaded.
    """
    if module_name is None:
        module_name = os.path.basename(os.path.splitext(file_path)[0])
    if sys.version_info >= (3, 5,):
        import importlib.util

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not spec:
            return

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    else:
        import imp
        mod = imp.load_source(module_name, file_path)
        return mod


def auto_module(path):
    path_basename = os.path.basename(path)
    problem_id = re.findall(r"(cL.*?)_.*.py", path_basename)[0]
    path_list = glob.glob(os.path.join(cfg.PATH_ctasks, f"**/{problem_id}.py"))
    assert len(path_list) == 1
    path_module = path_list[0]
    module = load_module(path_module)
    return module
