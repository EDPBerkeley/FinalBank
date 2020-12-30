import json

with open("/Users/Erchis/PycharmProjects/FinalBank/Data/categories.json") as jsonFile:
    categ = json.load(jsonFile)

secondOrderCategories = []

for category in categ:
    try:
        currSecondOrderCategory = category['hierarchy'][1]
        if (currSecondOrderCategory not in secondOrderCategories):
            secondOrderCategories.append(currSecondOrderCategory)
    except:
        "Do Nothing"



with open('../Data/secondOrderCategories.txt', 'w') as f:
    for item in secondOrderCategories:
        f.write("%s\n" % item)


