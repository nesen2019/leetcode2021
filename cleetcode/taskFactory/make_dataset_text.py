import glob
import logging
import os
import json
import re
import time
import tqdm
import requests
from cleetcode.configs import cfg
from cleetcode.scripts.utils import load_module
from retry import retry

from cleetcode.taskFactory.s_generator_all_problem2json import get_problems
from cleetcode.taskFactory.utils import OneProblem, login, get_all

"""
# dict_keys(['questionId',
# 'questionFrontendId',
# 'title', 'titleSlug',
# 'content',
# 'translatedTitle',
# 'translatedContent',
# 'difficulty',
# 'topicTags',
# 'codeSnippets',
# '__typename'])

"""


def get_had_modules(path=None):
    path = os.path.join(cfg.PATH_PROJECT, "cleetcode/ctasks") if path is None else path
    path_module_list = glob.glob(os.path.join(path, "day*/cL*.py"))
    had_modules = dict((re.findall(rf"(cL.*?).py", i)[-1], load_module(i)) for i in path_module_list)
    return had_modules


class OneProb:
    def __init__(self):
        self.question_id = None,
        self.frontend_question_id = None,
        self.question__title = None,
        self.question__title_slug = None,
        self.level = None,
        self.frequency = None,
        self.question_web = None,

        # May not exist!
        self.is_data_slug_all = False
        self.question_msg_md = None
        self.question_snippet_python = None
        self.topic_list = list()

        self.topicTags = None
        self.codeSnippets = None

    def __repr__(self):
        return str(self.dump_dict())

    def load_stat_status_pair(self, one_problem, data_slug_all=None):
        op = OneProblem(one_problem)
        self.question_id = op.stat.question_id
        self.frontend_question_id = op.stat.frontend_question_id
        self.question__title = op.stat.question__title
        self.question__title_slug = op.stat.question__title_slug
        self.level = op.difficulty.level
        self.frequency = op.frequency
        self.question_web = f"https://leetcode-cn.com/problems/{self.question__title_slug}"

        if data_slug_all is None:
            return
        if data_slug_all:
            data = data_slug_all
        else:
            return
        self.is_data_slug_all = True
        self.question_msg_md = f"{self.frontend_question_id}.{self.question__title}\n{data['translatedContent']}"

        self.topicTags = data["topicTags"]
        self.codeSnippets = data["codeSnippets"]

        for d in data["topicTags"]:
            self.topic_list.append(d["slug"])

        for d in data["codeSnippets"]:
            if d["lang"] == "Python3":
                self.question_snippet_python = d["code"]

    def load_dict(self, data: dict):

        for i, j in data.items():
            setattr(self, i, j)
        return self

    def dump_dict(self):
        return dict(
            question_id=self.question_id,
            frontend_question_id=self.frontend_question_id,
            question__title=self.question__title,
            question__title_slug=self.question__title_slug,
            level=self.level,

            frequency=self.frequency,
            question_web=self.question_web,
            question_msg_md=self.question_msg_md,
            question_snippet_python=self.question_snippet_python,
            topic_list=self.topic_list,

            topicTags=self.topicTags,
            codeSnippets=self.codeSnippets
        )

    def load(self, data: (str, dict)):
        if isinstance(data, str):
            with open(data, "r") as f:
                data = json.load(f)
        elif isinstance(data, dict):
            pass

        else:
            assert False

    def dump(self, file: (str, None) = None):
        if file is None:
            return self.dump_dict()
        elif isinstance(file, str):
            assert os.path.exists(file)
            with open(file, "w") as f:
                json.dump(self.dump_dict(), f)


class AllProb:
    """
    数据来源：
        1. 由OnePro一个个组成
        2. 由problems.json组成
        3. 由网络获取 转成problems.json组成
    """

    def __init__(self, path=None):
        self.all_prob_list = list()
        self.middleware = None
        path = os.path.join(cfg.PATH_PROJECT, "cleetcode/taskFactory/problems_middleware.json") if path is None else path
        with open(path, "r") as f:
            self.load(f)

    def dump(self, f):
        json.dump([i.dump_dict() for i in self.all_prob_list], f)

    def load(self, f):
        self.all_prob_list = [OneProb().load_dict(data) for data in json.load(f)]
        return self

    def selected_level(self, level, reverse, exclude_path=None):

        if exclude_path:
            had_modules = get_had_modules(exclude_path)
            data = [one for one in self.all_prob_list if
                    (one.level == level and "cL" + str(one.question_id).zfill(4) not in had_modules)]
        else:
            data = [one for one in self.all_prob_list if one.level == level]
        if reverse is None:
            return data
        if reverse:
            return sorted(data, key=lambda x: x.frequency, reverse=True)
        else:
            return sorted(data, key=lambda x: x.frequency)

    def get_all_hard(self, reverse=None, exclude_path=None):
        """
        @ reverse:
            None: random
            False: 1,2,3...
            True: n,n-1,n-2...
        """
        return self.selected_level(3, reverse, exclude_path)

    def get_all_medium(self, reverse=None, exclude_path=None):
        """
        @ erverse:

        """
        return self.selected_level(2, reverse, exclude_path)

    def get_all_easy(self, reverse=None, exclude_path=None):
        """
        @ reverse:

        """
        return self.selected_level(1, reverse, exclude_path)

    def generator_problem_per(self, n_hard, n_medium, n_easy):
        """

        """

    def generator_problem_frequency(self, n_hard, n_medium, n_easy):
        """

        """

    def generator_one_frequency_exclude(self, n_hard=1, n_medium=2, n_easy=3):
        """

        """
        path = cfg.PATH_ctasks
        hard = self.get_all_hard(reverse=True, exclude_path=path)
        medium = self.get_all_medium(reverse=True, exclude_path=path)
        easy = self.get_all_easy(reverse=True, exclude_path=path)
        max_index = int(max(len(hard) / 1, len(medium) / 2, len(easy) / 3))

        # print("len: ", len(hard)+len(medium)+len(easy))
        def gener():
            i = 0
            while i < max_index:
                yield hard[i:i + n_hard]

                for z in medium[i * n_medium:(i + 1) * n_medium]:
                    yield [z]

                for z in easy[i * n_easy:(i + 1) * n_easy]:
                    yield [z]
                i += 1

        one_list = list()
        for g in gener():
            one_list += g
            if len(one_list) >= n_hard + n_medium + n_easy:
                yield one_list
                one_list = list()

        yield one_list

    def get_one_pro_id(self, id):
        """

        """
        for one in self.all_prob_list:
            if one.question_id == id:
                return one
        return None

    def get_one_pro_slug(self, slug):
        """

        """
        for one in self.all_prob_list:
            if one.question__title_slug == slug:
                return one
        return

    def get_one_pro(self, sign):

        for one in self.all_prob_list:
            if isinstance(sign, int) and one.question_id == sign:
                return one
            elif isinstance(sign, str) and one.question__title_slug == sign:
                return one
        return
