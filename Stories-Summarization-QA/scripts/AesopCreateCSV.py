import json
import re
import csv

with open('./data/aesopfables.jsonl', 'r') as json_file:
    json_list = list(json_file)

csvEntries = []
for json_str in json_list:
    result = json.loads(json_str)

    title = str(result['title'])
    story = str(result['story'])
    moral = str(result['moral'])

    # Remove \n
    story = re.sub('\n', '', story)

    # Replace \' with '
    story = story.replace('\'', "'")

    # Trim
    story = story.strip()

    # Replace unicode characters
    storyEncode = story.encode("ascii", "ignore")
    story = storyEncode.decode()

    story += moral

    csvEntry = [title, story, moral]
    csvEntries.append(csvEntry)

with open('./data/aesopfables.csv', 'w', newline = '') as file:
  writer = csv.writer(file)
  writer.writerows(csvEntries)