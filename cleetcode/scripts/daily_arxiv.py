import os
import re

import arxiv
import requests
import time
import datetime

from cleetcode.configs import cfg
__all__ = [
    "HandleArxiv"
]


def parse_paper(paper):
    return dict(
        id=paper["id"],
        pdf_url=paper["pdf_url"],
        title=paper["title"],
        authors=paper["authors"],
        summary=paper["summary"],
        updated=paper["updated"],
        updated_parsed=paper["updated_parsed"],
    )


def get_one_day_query(query, deday=0):
    max_ids = 50
    now_time_struct = time.struct_time(time.localtime())
    dest_mday = now_time_struct.tm_mday + deday

    while True:

        querys = arxiv.query(query, max_results=max_ids, sort_by="lastUpdatedDate")
        end_time_struct = querys[-1]["updated_parsed"]
        if end_time_struct.tm_mday == dest_mday:
            assert max_ids < 1000
            max_ids *= 2
            continue
        else:
            break
    is_equal = lambda a, b: a.tm_year == b.tm_year and a.tm_mon == b.tm_mon and a.tm_mday == b.tm_mday + deday

    return [parse_paper(paper) for paper in querys if is_equal(paper["updated_parsed"], now_time_struct)]


def write_markdown(papers, save_file, title="hello arxiv"):
    with open(save_file, "w") as f:
        data = list()
        data.append(f"## {title}\n")
        for i, paper in enumerate(papers, start=1):
            title = " ".join(re.split("[\n\t\ ]+", paper["title"]))
            data.append(f"- {i:02}-{title}")

        for i, paper in enumerate(papers, start=1):
            title = " ".join(re.split("[\n\t\ ]+", paper["title"]))
            data.append(f"## {i:02}-{title}  \n")
            data.append(f"- id     : {paper['id']}")
            data.append(f"- pdf_url: {paper['pdf_url']}")
            data.append(f"### authors  ")
            data.append(f"```\n{paper['authors']}\n```")

            data.append(f"### summary  ")
            data.append(f"```\n{paper['summary']}\n```")

            data.append(f"### {paper['updated']}")

        f.write("\n".join(data))



class HandleArxiv(object):
    def __init__(self):
        pass

    def add_daily_reading(self, query=None, deday=None, save_dir=None):
        query = "cs.CV" if query is None else query
        deday = -3 if deday is None else deday

        dt = datetime.datetime.now() + datetime.timedelta(deday)
        ymd_week = f"week_{dt.isocalendar()[1]:02}"
        ymd_day = f"day_{dt.year:02}{dt.month:02}{dt.day:02}{dt.hour:02}"
        path_dir = os.path.join(cfg.PATH_arxiv_daily_summary, ymd_week)
        os.makedirs(path_dir, exist_ok=True)
        save_dir = path_dir if not save_dir else save_dir
        a = get_one_day_query(query, deday)

        save_path = os.path.join(save_dir, f"{ymd_day}_{query}.md")
        write_markdown(a, save_path)
        print(f"save_path: {save_path}")
        

if __name__ == '__main__':
    ha = HandleArxiv()
    ha.add_daily_reading("destination")

if __name__ == '__main__asd':
    a = get_one_day_query("cs.CV", deday=0)
    # print(a)
    write_markdown(a, "b1.md")
