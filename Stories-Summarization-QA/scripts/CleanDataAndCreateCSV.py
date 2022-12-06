import json
import re
import csv

with open('./data/bedtimestories.jsonl', 'r') as json_file:
    json_list = list(json_file)

csvEntries = []
for json_str in json_list:
    result = json.loads(json_str)

    title = result['title']
    story = str(result['story'])

    if story == '' or title == '':
      continue

    # Remove \n
    story = re.sub('\n', '', story)

    # Replace \' with '
    story = story.replace('\'', "'")

    # Trim
    story = story.strip()

    # Replace unicode characters
    storyEncode = story.encode("ascii", "ignore")
    story = storyEncode.decode()

    csvEntry = [title, story]
    csvEntries.append(csvEntry)

header = ["title", "story"]
with open('./data/bedtimestories.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    # writer.writerow(header)
    writer.writerows(csvEntries)