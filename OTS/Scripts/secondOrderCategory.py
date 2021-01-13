import json

with open("/Users/Erchis/PycharmProjects/FinalBank/Data/categories.json") as jsonFile:
    categ = json.load(jsonFile)

firstOrderCategories = []

for category in categ:
    currFirstOrderCategory = category['hierarchy'][0]
    if (currFirstOrderCategory not in firstOrderCategories):
        firstOrderCategories.append(currFirstOrderCategory)

with open('../Data/firstOrderCategories.txt', 'w') as f:
    for item in firstOrderCategories:
        f.write("%s\n" % item)


