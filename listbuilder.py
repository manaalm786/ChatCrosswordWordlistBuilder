import json
import nltk
import re
import argparse

parser = argparse.ArgumentParser(description='Perform letter, word and n-tuple frequency analysis on text files.')
parser.add_argument('--filename', '-f', dest='inputFile', required=True, help='Text file to parse.')
args = parser.parse_args()


all_words = []

chat_history = open(args.inputFile, 'r')
chat_dict = json.load(chat_history)

# set of most common words
most_common = set()
with open("1000.txt") as file:
    temp = file.read().splitlines()
    for word in temp:
        most_common.add(word)


for message in chat_dict["messages"]:
    words = re.findall(r'\w+', message["content"].lower())
    for word in words:
        all_words.append(word)



fdist = nltk.FreqDist(all_words)

output_file = open('chat_wordlist.txt', 'w')

for word, freq in fdist.most_common():
    if freq != 1 and len(word) > 2 and word not in most_common:
        print(str(str(word) + ';' + '60'), file=output_file)
