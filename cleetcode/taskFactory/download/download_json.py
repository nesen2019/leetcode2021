import os
import json
import argparse

import requests
from tqdm import tqdm
import time
from cleetcode.taskFactory.make_dataset_text import OneProb
from cleetcode.taskFactory.utils import get_all, login


def download_json(path_json):
    with open(path_json, "r") as f:
        data = json.load(f)
    try:
        session = requests.Session()
        login(session)
        for i in tqdm(data):
            if data[i]["data_slug_all"]:
                continue
            all_msg = get_all(session, i)
            data[i]["data_slug_all"] = all_msg
    except:
        print(f"error --- -- -" * 3)

    finally:
        with open(path_json, "w") as f:
            json.dump(data, f, indent=4)


def download_json_all(path_json, path_save):
    with open(path_json, "r") as f:
        data = json.load(f)
        data = data["stat_status_pairs"]

    datas = dict()
    session = requests.Session()
    login(session)
    k = 0
    for one_problem in tqdm(data):
        slug = one_problem["stat"]["question__title_slug"]
        datas[slug] = {"one_problem": one_problem}
        try:
            data_slug_all = get_all(session, slug)
        except:
            print(f"error --- -- ->>{slug}<<" * 3)
            continue
        finally:
            with open(path_save, "w") as f:
                json.dump(datas, f, indent=4)

        # one_prob = OneProb().load_stat_status_pair(one_problem, data_slug_all, session=session)
        datas[slug].update(dict(data_slug_all=data_slug_all))

        time.sleep(1.5)


if __name__ == '__main__12':
    with open("/root/progs/leetcode2021/cleetcode/taskFactory/problems_all.json", "r") as f:
        data = json.load(f)

    for slug in data:
        one_problem = data[slug]["one_problem"]
        data_slug_all = data[slug]
        data_slug_all.pop("one_problem")
        data[slug] = dict(one_problem=one_problem, data_slug_all=data_slug_all)

    with open("/root/progs/leetcode2021/cleetcode/taskFactory/problems_all_p01.json", "w") as f:
        data = json.dump(data, f, indent=4)

if __name__ == '__main__qw':
    download_json_all('/root/progs/leetcode2021/cleetcode/taskFactory/problems.json',
                      path_save="/root/progs/leetcode2021/cleetcode/taskFactory/problems_all.json")

if __name__ == '__main__as':
    download_json("/root/progs/leetcode2021/cleetcode/taskFactory/download/segs/seg_99.json")
