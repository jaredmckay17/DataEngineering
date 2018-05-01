'''
Utilizing functional programming pipeline tasks to ulilize performance in the data pipeline
'''

from pipeline import Pipeline
import json
import io
from datetime import datetime
import csv
import string
import re
from nltk.corpus import stopwords
import itertools


def build_csv(lines, header=None, file=None):
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.seek(0)
    return file

@pipeline.task()
def file_to_json():
    with open('hn_stories_2014.json', 'r') as file:
        json_data = json.load(file)
        stories = json_data['stories']

    return stories


@pipeline.task(depends_on=file_to_json)
def filter_stories(stories):
    def most_pop(story):
        return story['points'] > 50 and story['num_comments'] > 1 and not story['title'].startswith('Ask HN')

    return (s for s in stories if most_pop(s))


@pipeline.task(depends_on=filter_stories)
def json_to_csv(stories):
    header = ['objectID', 'created_at', 'url', 'points', 'title']
    story_list = []

    for s in stories:
        story_list.append([s['objectID'], datetime.strptime(s['created_at'], "%Y-%m-%dT%H:%M:%SZ"), \
                           s['url'], s['points'], s['title']])

    return build_csv(story_list, header=header, file=io.StringIO())


@pipeline.task(depends_on=json_to_csv)
def extract_titles(file_obj):
    reader = csv.reader(file_obj)
    header = next(reader)

    i = header.index('title')

    return (line[i] for line in reader)


@pipeline.task(depends_on=extract_titles)
def clean_titles(titles):
    for title in titles:
        title = title.lower()
        title = re.sub('[^A-Za-z]', ' ', title)
        yield title


@pipeline.task(depends_on=clean_titles)
def build_keyword_dictionary(titles):
    word_dict = {}
    stop = set(stopwords.words('english'))

    for title in titles:
        for word in title.split(" "):
            if word and word not in stop:
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1

    return word_dict


@pipeline.task(depends_on=build_keyword_dictionary)
def top_keywords(word_freq):
    res = sorted(word_freq.items(), key=lambda x: (x[1]), reverse=True)
    return res[:100]


pipeline = Pipeline()
res = pipeline.run()
print(res[top_keywords])

'''
[('hn', 211), ('google', 194), ('show', 192), ('new', 188), ('open', 126), ('bitcoin', 106), ('web', 99),
 ('programming', 91), ('c', 88), ('data', 87), ('source', 86), ('facebook', 84), ('python', 81), ('video', 81),
 ('code', 75), ('using', 72), ('free', 72), ('released', 71), ('js', 71), ('app', 68), ('internet', 67),
 ('javascript', 66), ('game', 66), ('one', 66), ('world', 65), ('time', 64), ('go', 64), ('first', 63), ('linux', 62),
 ('apple', 61), ('microsoft', 60), ('us', 58), ('pdf', 57), ('language', 57), ('work', 55), ('software', 52),
 ('use', 52), ('year', 52), ('like', 52), ('startup', 51), ('make', 51), ('yc', 50), ('github', 49), ('x', 48),
 ('security', 48), ('get', 46), ('system', 44), ('windows', 44), ('nsa', 44), ('based', 43), ('u', 41),
 ('computer', 41), ('way', 41), ('heartbleed', 41), ('project', 40), ('ios', 40), ('twitter', 39), ('life', 39),
 ('git', 38), ('back', 38), ('amazon', 38), ('day', 38), ('users', 37), ('developer', 37), ('design', 37), ('gox', 37),
 ('mozilla', 37), ('man', 36), ('android', 36), ('os', 36), ('ceo', 36), ('mt', 36), ('vs', 36), ('big', 36),
 ('online', 35), ('made', 34), ('simple', 34), ('server', 33), ('years', 33), ('firefox', 33), ('court', 33),
 ('browser', 33), ('mobile', 32), ('guide', 32), ('learning', 32), ('fast', 32), ('built', 32), ('b', 32), ('api', 32),
 ('says', 32), ('apps', 32), ('billion', 31), ('tech', 31), ('k', 31), ('problem', 31), ('engine', 31), ('people', 31),
 ('chrome', 31), ('site', 31), ('introducing', 30)]
'''
