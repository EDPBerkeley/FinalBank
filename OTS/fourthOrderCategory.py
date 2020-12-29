import json

with open("/Users/Erchis/PycharmProjects/FinalBank/Data/categories.json") as jsonFile:
    categ = json.load(jsonFile)

thirdOrderCategories = []

for category in categ:
    try:
        currThirdOrderCategory = category['hierarchy'][1]
        if (currThirdOrderCategory not in thirdOrderCategories):
            thirdOrderCategories.append(currThirdOrderCategory)
    except:
        "Do Nothing"



with open('../Data/thirdOrderCategories.txt', 'w') as f:
    for item in thirdOrderCategories:
        f.write("%s\n" % item)


