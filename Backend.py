import json as j


#A jsn class used to parse the JSON object
class jsn:
    def __init__(self, jsn):
        self.__dict__ = j.load(jsn)

def parseTransactions(transactions):
    #turn the JSON string into a JSON object
    parsedTransactions = jsn(transactions)



