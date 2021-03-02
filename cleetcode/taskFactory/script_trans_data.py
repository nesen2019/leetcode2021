import json
import os

from cleetcode.taskFactory.make_dataset_text import OneProb, AllProb
from cleetcode.taskFactory.utils import OneProblem




if __name__ == '__main__qwe':
    path = "/root/progs/leetcode2021/cleetcode/taskFactory/problems_all_p01.json"

    with open(path, "r") as f:
        data = json.load(f)
    all_probs = list()
    for slug in data:
        one_problem = data[slug]["one_problem"]
        data_slug_all = data[slug]["data_slug_all"]
        one = OneProb()
        one.load_stat_status_pair(one_problem, data_slug_all)
        all_probs.append(one.dump_dict())

    with open("./problems_middleware.json", "w") as f:
        json.dump(all_probs, f, indent=4)







