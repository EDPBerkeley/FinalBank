import json as j


#A jsn class used to parse the JSON object
class jsn:
    def __init__(self, jsn):
        self.__dict__ = j.load(jsn)

def parseTransactions(transactions):
    #assign a variable to represent the transactions
    parsedTransactions = transactions.json['transactions']

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

    print(fullCategories)

    return fullCategories

#Extract past 30 days of transactions from 365 days
def getPast30Days(transactionHistory):
    return transactionHistory
