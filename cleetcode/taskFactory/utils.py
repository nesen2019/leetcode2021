import ast
import json
import os
import requests

from cleetcode.configs.config import cfg

from requests_toolbelt import MultipartEncoder


def login(session, user_agent=None):
    if user_agent is None:
        user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    url = 'https://leetcode-cn.com'

    # cookies = session.get(url, proxies=cfg.LOGINmsg.proxy_dict)

    url = "https://leetcode-cn.com/accounts/login"

    params_data = dict(
        login=cfg.LOGINmsg.email,
        password=cfg.LOGINmsg.password,
        next="problems"
    )

    headers = {
        "User-Agent": user_agent,
        "Connection": 'keep-alive',
        'Referer': 'https://leetcode-cn.com/accounts/login/',
        "origin": "https://leetcode-cn.com"
    }
    m = MultipartEncoder(params_data)

    headers['Content-Type'] = m.content_type

    session.post(url, headers=headers, data=m,
                 timeout=10, allow_redirects=False,
                 proxies=cfg.LOGINmsg.proxy_dict)
    is_login = session.cookies.get('LEETCODE_SESSION') != None
    return is_login, session


def get_all(session, slug, user_agent=None):
    if user_agent is None:
        user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    url = "https://leetcode-cn.com/graphql"
    params = {
        'operationName':
            "getQuestionDetail",
        'variables': {
            'titleSlug': slug
        },
        'query':
            '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    title
                    titleSlug
                    content
                    translatedTitle
                    translatedContent
                    difficulty
                    topicTags {
                        name
                        slug
                        translatedName
                        __typename
                    }
                    codeSnippets {
                        lang
                        langSlug
                        code
                        __typename
                    }
                    __typename
                }
            }'''
    }
    json_data = json.dumps(params).encode('utf8')
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode-cn.com/problems/' + slug
    }
    resp = session.post(url, data=json_data,
                        headers=headers, timeout=10,
                        proxies=cfg.LOGINmsg.proxy_dict)
    resp.encoding = 'utf8'
    content = resp.json()
    # 题目详细信息
    # print(content)
    question = content['data']['question']
    # print(json.dumps(question, indent=4))
    question = json.dumps(question, indent=4)
    return ast.literal_eval(question)


class ProblemAll:
    def __init__(self, session, slug, user_agent=None):
        self.data = get_all(session, slug, user_agent)

    def get_md_problem_content(self):
        return self.data["translatedContent"]

    def get_code_snippet_python(self):
        for i in self.data["codeSnippets"]:
            if i["lang"] == "Python3":
                return i["code"]

        return None

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




class OneProblem:
    class Stat:
        def __init__(self, st):
            self.question_id = st["question_id"]
            self.question__title = st["question__title"]
            self.question__title_slug = st["question__title_slug"]
            self.question__hide = st["question__hide"]
            self.total_acs = st["total_acs"]
            self.total_submitted = st["total_submitted"]
            self.total_column_articles = st["total_column_articles"]
            self.frontend_question_id = st["frontend_question_id"]
            self.is_new_question = st["is_new_question"]

    class Difficulty:
        def __init__(self, dif):
            self.level = dif["level"]

    def __init__(self, obj):
        self.stat = self.Stat(obj["stat"])
        self.status = obj["status"]
        self.difficulty = self.Difficulty(obj["difficulty"])
        self.paid_only = obj["paid_only"]
        self.is_favor = obj["is_favor"]
        self.frequency = obj["frequency"]
        self.progress = obj["progress"]

    def __repr__(self):
        # return f"id:{self.stat.question_id}, slug: {self.stat.question__title_slug}"
        return str(dict(
            id=self.stat.question_id,
            slug=self.stat.question__title_slug
        ))
