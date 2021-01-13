import json as j


#A jsn class used to parse the JSON object
from datetime import datetime


class jsn:
    def __init__(self, jsn):
        self.__dict__ = j.load(jsn)

def parseTransactions(parsedTransactions):

    #Open the empty categories json file
    with open("Data/emptyCategories.json") as jsonFile:
        emptyCategories = j.load(jsonFile)

    fullCategories = emptyCategories
    # Open the empty categories json file
    with open("Data/categoryRelationships.json") as jsonFile:
        categoryRelationships = j.load(jsonFile)

    #Add the transactions to their relevant categories
    for transaction in parsedTransactions:
        #Find the original category of the transaction
        unmappedCategory = transaction['category'][0]

        #Map the raw category to the correct finished category
        mappedCategory = categoryRelationships[unmappedCategory]

        #Add the relevant amount
        fullCategories[mappedCategory] += transaction['amount']

    #Round each number to 2 decimal places
    for category in fullCategories:
        fullCategories[category] = round(fullCategories[category], 2)

    print(fullCategories)

    return fullCategories

#Key used to sort the transactions of the past 30 days
def amount(transaction):
    return transaction['amount'];

