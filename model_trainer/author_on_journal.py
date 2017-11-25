#!/usr/bin/env python
# encoding: utf-8
import os
import sys

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
sys.path.append("../")
import util
import json
from collections import Counter
import config


def get_author_on_item(paper_path, paper_author_path, to_file, itemname):
    paper_author_data = util.read_dict_from_csv(paper_author_path)
    paper_data = util.read_dict_from_csv(paper_path)

    paper_to_itemId = {}
    for paper in paper_data:
        paperId = int(paper["Id"])
        itemId = int(paper[itemname])
        if itemId != 0:  # 0 is not allowed in itemId
            paper_to_itemId[paperId] = itemId

    dict_author_to_items = {}
    pa_cur = 0
    pa_total = len(paper_author_data)
    for paper_author in paper_author_data:
        paperId = int(paper_author["PaperId"])
        itemId = paper_to_itemId.get(paperId, 0)
        pa_cur += 1
        if itemId == 0:
            continue
        authorId = int(paper_author["AuthorId"])

        # dict_author_to_items.setdefault(authorId, Counter())
        dict_author_to_items.setdefault(authorId, {})
        dict_author_to_items[authorId].setdefault(itemId, 0)
        dict_author_to_items[authorId][itemId] += 1

        if pa_cur % 100000 == 0:
            print("Paper_Author: %d/%d (%.2f%%)" % (pa_cur, pa_total, 100.0 * pa_cur / pa_total))

    json.dump(dict_author_to_items, open(to_file, "w"))


def get_author_on_journal(paper_path, paper_author_path, to_file):
    get_author_on_item(paper_path, paper_author_path, to_file, "JournalId")


def get_author_on_conference(paper_path, paper_author_path, to_file):
    get_author_on_item(paper_path, paper_author_path, to_file, "ConferenceId")


if __name__ == "__main__":
    get_author_on_conference(paper_path=config.PAPER_FILE,
                             paper_author_path=config.PAPERAUTHOR_FILE,
                             to_file=config.AUTHOR_ON_CONFERENCE_FILE)
