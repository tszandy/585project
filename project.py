import csv
csvfile=open('replacelist.csv','r')
replacecsv=csv.reader(csvfile,delimiter=',')
replacelist=[]
for row in replacecsv:
    replacelist+=[(row[0],row[1])]


def replacestr(string):
    for (fromstr,targetstr) in replacelist:
        string=replaceeach(string,fromstr,targetstr)
    return string

def replaceeach(string,fromstr,targetstr):
    return string.replace(fromstr,targetstr,string.count(fromstr))


# import json
# allgames=open('amazondataset/Video_Games_5.json', 'r')
# games=[]
# for game in allgames:
#     games.append(json.loads(game))
#
# print(games)
