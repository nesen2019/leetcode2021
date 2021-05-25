import ast
import os
import json
import datetime

from cleetcode.configs import cfg
from cleetcode.taskFactory.make_dataset_text import AllProb, OneProb


class OneMd:
    def __init__(self, idx, slug, description, code_snippet, title, web):
        self.__idx = idx
        self.__slug = slug
        self.data_py = ""
        self.is_des = False if "\n" not in code_snippet else True
        self.description = description
        self.code_snippet = code_snippet
        self.title = title
        self.web = web

    @staticmethod
    def one_md(one_prob):
        return OneMd(
            idx=one_prob.question_id if one_prob.question_id is not None else "idx",
            slug=one_prob.question__title if one_prob.question__title is not None else "slug",
            description=one_prob.question_msg_md if one_prob.question_msg_md is not None else "description",
            code_snippet=one_prob.question_snippet_python if one_prob.question_snippet_python is not None
            else "class Solution: pass\n",
            title="title" if one_prob.question__title is None else one_prob.question__title,
            web="https://google.com" if one_prob.question_web is None else one_prob.question_web
        )

    @staticmethod
    def dumps(one_mds, f, title=None):
        assert isinstance(one_mds, (list, tuple))
        if one_mds:
            st = ""
            st += f"## {title}  \n\n"
            for one in one_mds:
                st += f"- [ ] [{str(one.idx).zfill(4)}_{one.problem_title}]({one.web})\n"
            st += "\n\n"
            k = 0
            for one in one_mds:
                k += 1
                st += f"### {k}-[{str(one.idx).zfill(4)}_{one.problem_title}]({one.web})\n\n"
                st += f"{one.md_problem_description} \n"
                st += f"{one.md_snippet_python}\n"

            st += "\n"
            if isinstance(f, str):
                with open(f, "w", encoding="utf8") as fw:
                    fw.write(st)
            else:
                f.write(st)

    def dump(self, f):
        st = ""
        st += f"### {str(self.idx).zfill(4)}_{self.problem_title}  \n\n"
        st += f"- [ ] [{str(self.idx).zfill(4)}_{self.problem_title}](self.web)  \n\n"
        st += f"{self.md_problem_description} \n"
        st += f"{self.md_snippet_python}\n"
        if isinstance(f, str):
            with open(f, "w", encoding="utf8") as fw:
                fw.write(st)
        else:
            f.write(st)

    @property
    def md_problem_description(self):
        st = ""
        st += self.description
        return st

    @property
    def md_snippet_python(self):
        st = ""
        st += "```python\n"
        st += self.code_snippet + "\n"
        st += "```\n"
        return st

    @property
    def idx(self):
        return self.__idx

    @property
    def slug(self):
        return self.__slug

    @property
    def problem_title(self):
        return self.title


class OneClPy:
    def __init__(self, idx, slug, description, code_snippet):
        self.idx = idx
        self.slug = slug
        self.data_py = ""
        self.is_des = False if (description == "description" or code_snippet == "class Solution: pass\n") else True
        self.data_py += "\n\n".join([
            self.add_doc(description, code_snippet),
            self.add_import(code_snippet),
            self.add_ctest(),
            self.add_code_snippet_python(code_snippet),
            self.add_main_content()
        ])

    @staticmethod
    def one_cl_py(one_prob: OneProb):
        return OneClPy(
            idx=one_prob.question_id if one_prob.question_id is not None else "idx",
            slug=one_prob.question__title if one_prob.question__title is not None else "slug",
            description=one_prob.question_msg_md if one_prob.question_msg_md is not None else "description",
            code_snippet=one_prob.question_snippet_python if one_prob.question_snippet_python is not None
            else "class Solution: pass\n"
        )

    def dump(self, f):
        if isinstance(f, str):
            with open(f, "w", encoding="utf8") as fw:
                fw.write(self.data_py)
        else:
            f.write(self.data_py)

    def add_doc(self, description, code_snippet):
        st = f"'''\n"
        st += f'{self.idx}.{self.slug}'
        st += f"\n{description}\n{code_snippet}\n'''"
        return st

    def add_import(self, code_snippet):
        st = ""
        if "List" in code_snippet:
            st += "from typing import List\n"
        if "ListNode" in code_snippet:
            st += "from cleetcode.structures import ListNode, HandleLink\n"
        if "TreeNode" in code_snippet:
            st += "from cleetcode.structures import TreeNode, HandleTreeTwo\n"
        if "NestedInteger" in code_snippet:
            st += "from typing import Any as NestedInteger\n"

        st += f"from cleetcode import decorator_default\n"
        return st

    def add_ctest(self):
        st = ""
        st += f'@decorator_default("")\n'
        st += f'def ctest(method_name, class_name):  \n'
        st += f'    return f"""\n'
        st += f'    \n'
        st += f'    >>> \n'
        st += f'    >>> res = {{class_name}}().{{method_name}}()\n'
        st += f'    """\n'
        return st

    def add_code_snippet_python(self, code_snippet):
        st = ""
        st += code_snippet.strip()
        st += f"\n        pass\n" if self.is_des else ""
        try:
            ast.parse(st)
        except:
            st = "\n"  
        return st

    def add_main_content(self):
        st = ""
        st += f'if __name__ == "__main__":  \n'
        st += f'    import doctest  \n'
        st += f'    \n'
        st += f'    doctest.testmod()'
        return st


class HandleAddPlan:
    """
    # demo
    if __name__ == '__main__':
        ap = AllProb()
        c = HandleAddPlan(ap)
        c.add_plan_task_now(timedelta=1)

    """

    def __init__(self, ap=None):
        self.ap = AllProb() if ap is None else ap
        pass

    def nums_remain(self):
        path = cfg.PATH_ctasks

        nums_hard_all = len(self.ap.get_all_hard())
        nums_medium_all = len(self.ap.get_all_medium())
        nums_easy_all = len(self.ap.get_all_easy())

        hard = self.ap.get_all_hard(reverse=True, exclude_path=path)
        medium = self.ap.get_all_medium(reverse=True, exclude_path=path)
        easy = self.ap.get_all_easy(reverse=True, exclude_path=path)
        nums_hard = len(hard)
        nums_medium = len(medium)
        nums_easy = len(easy)

        return dict(
            all=(nums_hard+nums_medium+nums_easy, nums_hard_all+nums_medium_all+nums_easy_all),
            hard=(nums_hard, nums_hard_all),
            medium=(nums_medium, nums_medium_all),
            easy=(nums_easy, nums_easy_all)
        )

    def add_plan_task_now(self, timedelta=0, nh=1, nm=2, ne=3):

        dt = datetime.datetime.now() + datetime.timedelta(timedelta)
        ymd_week = f"week_{dt.isocalendar()[1]:02}"
        ymd_day = f"day_{dt.year:02}{dt.month:02}{dt.day:02}{dt.hour:02}"
        path_dir = os.path.join(cfg.PATH_ctasks, ymd_week, ymd_day)
        os.makedirs(path_dir)
        with open(os.path.join(path_dir, "__init__.py"), "w") as f:
            pass
        with open(os.path.join(path_dir, f"{ymd_day}_note.md"), "w") as f:
            pass

        for cur_day_all in self.ap.generator_one_frequency_exclude(nh, nm, ne):
            OneMd.dumps(
                one_mds=[OneMd.one_md(one) for one in cur_day_all],
                f=os.path.join(path_dir, f"{ymd_day}.md"),
                title=f"{ymd_day}"
            )
            for one in cur_day_all:
                module_name = f"cL{one.question_id:04}"
                path_py = os.path.join(path_dir, f"{module_name}.py")
                OneClPy.one_cl_py(one).dump(path_py)

            break

    def add_problem(self, path_save, frontend_question_id=None):

        problem_all = self.ap.get_all_hard()+self.ap.get_all_medium()+self.ap.get_all_easy()
        from typing import cast
        if frontend_question_id:
            for one in problem_all:
                # print(dir(one))
                if one.frontend_question_id == frontend_question_id:
                    OneClPy.one_cl_py(one).dump(path_save)


    def add_problem01(self, frontend_question_id=None):

        problem_all = self.ap.get_all_hard()+self.ap.get_all_medium()+self.ap.get_all_easy()
        if frontend_question_id:
            for one in problem_all:
                # print(dir(one))
                if one.frontend_question_id == frontend_question_id:
                    OneClPy.one_cl_py(one).dump(f"L{one.question_id:04}.py")




if __name__ == '__main__':
    ap = AllProb()
    c = HandleAddPlan(ap)
    c.add_problem("a.py", "24")

if __name__ == '__main__123':
    ap = AllProb()
    c = HandleAddPlan(ap)
    c.add_plan_task_now(timedelta=1)

if __name__ == '__main__qwe':
    ap = AllProb()
    # OneClPy.one_cl_py(ap.get_one_pro(2)).dump("a.py")
    # OneMd.one_md(ap.get_one_pro(2)).dump("a.md")
    omd = lambda x: OneMd.one_md(ap.get_one_pro(x))

    OneMd.dumps([omd(1), omd(2), omd(3)], "b.md", "day001")
