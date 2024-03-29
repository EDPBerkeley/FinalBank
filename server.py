# Read env vars from .env file
from dotenv import load_dotenv
load_dotenv()

import base64
import os
import datetime
import plaid
import json
import time
import Utils as ut
import User as us
import pymongo
from pymongo import MongoClient
from flask import Flask, redirect, session
from flask import render_template
from flask import request
from flask import jsonify
from calendar import monthrange



app = Flask(__name__)
app.secret_key = b'O\xb2+h,\x96\xcb\xf3\x9a9\xbd*\x90W\x06\xca'



# Fill in your Plaid API keys - https://dashboard.plaid.com/account/keys
PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
# PLAID_PRODUCTS is a comma-separated list of products to use when initializing
# Link. Note that this list must contain 'assets' in order for the app to be
# able to create and retrieve asset reports.
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions').split(',')

# PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
# will be able to select institutions from.
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')


def empty_to_none(field):
  value = os.getenv(field)
  if value is None or len(value) == 0:
    return None
  return value


# Parameters used for the OAuth redirect Link flow.
#
# Set PLAID_REDIRECT_URI to 'http://localhost:8000/oauth-response.html'
# The OAuth redirect flow requires an endpoint on the developer's website
# that the bank website should redirect to. You will need to configure
# this redirect URI for your client ID through the Plaid developer dashboard
# at https://dashboard.plaid.com/team/api.
PLAID_REDIRECT_URI = empty_to_none('PLAID_REDIRECT_URI')

client = plaid.Client(client_id=PLAID_CLIENT_ID,
                      secret=PLAID_SECRET,
                      environment=PLAID_ENV,
                      api_version='2019-05-29')

#define global variables
currUser = None
userdataBase = None
access_token = None

@app.route('/', methods = ['GET', 'POST'])
def index():
  # return redirect("/signup")
  if (request.method == 'POST'):
    client = pymongo.MongoClient(
      "mongodb+srv://ErchisPatwardhan:WPxWoQsqwFlas3Qx@users.fszlz.mongodb.net/Users?retryWrites=true&w=majority")
    db = client.get_database('FinalBankUsers')
    global userdataBase
    userdataBase = db.Users

    email = request.form['email']
    password = request.form['password']

    signIn = us.User().signin(userDataBase=userdataBase, email=email, password=password)
    success = signIn[0]
    if (success):
      print("user succesfully signed in")

      global currUser
      currUser = signIn[1]

      us.User().start_session(currUser)
      return redirect("/analysis")



  return render_template(
    'signin.html',
  )

@app.route('/signup', methods = ["GET", "POST"])
def signup():


  client = pymongo.MongoClient(
    "mongodb+srv://ErchisPatwardhan:WPxWoQsqwFlas3Qx@users.fszlz.mongodb.net/Users?retryWrites=true&w=majority")
  db = client.get_database('FinalBankUsers')
  global userdataBase
  userdataBase = db.Users

  if (request.method == "POST"):
    email = request.form['email']
    password = request.form['password']

    user = us.User().signup(email=email, password=password)
    print(user)


    #Add the user to the mongoDB server
    if (userdataBase.insert_one(user)):

      global currUser
      currUser = user
      print("user succesfully added")

      # Start a session
      ses = us.User().start_session(user)
      print("session succesfully started")

      return redirect('/analysis')

    else:
      return redirect('/')




  return render_template(
    'signup.html',
  )

@app.route('/homepage', methods = ['GET', 'POST'])
def homepage():
  return render_template('index.html')


@app.route('/analysis')
def analysis():

  #Access the mongoDB user and extract the access token
  global access_token
  access_token = currUser["accesstoken"]

  #Fetch the transactions for 365 days
  transactionHistoryFullYear = get_transactions(days = 365).json['transactions']
  with open('Data/AMEXTransactions.json', 'w') as outfile:
    json.dump(transactionHistoryFullYear, outfile)


  #Get the transactions for the last 30 Days
  transactionHistory30Days = get_transactions(days = 30).json['transactions']

  #Get the data for the first chart
  chart1 = ch1(transactionHistory30Days)
  chart1JSON = json.dumps(chart1)
  print("Chart 1: " + chart1JSON + "\n")

  #Get the data for the second chart
  chart2 = ch2(transactionHistoryFullYear)
  chart2JSON = json.dumps(chart2)
  print("Chart 2: " + chart2JSON + "\n")

  #Get the data for the third chart
  chart3 = ch3(transactionHistoryFullYear)
  chart3JSON = json.dumps(chart3)
  print("Chart 3: " + chart3JSON + "\n")

  #Get the data for the fourth chart
  chart4 = ch4(transactionHistory30Days)
  chart4JSON = json.dumps(chart4)
  print("Chart 4: " + chart4JSON + "\n")

  #Get the data for the fifth chart
  chart5 = ch5(transactionHistoryFullYear)
  chart5JSON = json.dumps(chart5)
  print("Chart 5: " + chart5JSON + "\n")

  #Get the data for the sixth chart
  chart6 = ch6(transactionHistory30Days)
  chart6JSON = json.dumps(chart6)
  print("Chart 6: " + chart6JSON + "\n")

  return render_template(
    'analysis.html',
    chart1 = chart1,
    chart2 = chart2,
    chart3 = chart3,
    chart4 = chart4,
    chart5 = chart5,
    chart6 = chart6
  )



#Code for 1st chart
#Get the categorical spending of the last 30 Days
def ch1(transactionHistory):


  # Return a dictionary of the format {category: sum of goods purchased}
  parsed_transactions = ut.parseTransactions(transactionHistory)
  return parsed_transactions

#Code for 2nd chart
#Get the categorical spending of the last 12 months
def ch2(transactionHistory):

  # Return a dictionary of the format {category: sum of goods purchased}
  parsed_transactions = ut.parseTransactions(transactionHistory)
  return parsed_transactions

#Code for the 3rd chart
#Get the 5 Biggest Purchases of the last 12 months
def ch3(transactionHistory):

  transactionHistoryCopy = transactionHistory
  top5 = []

  #Add the first 5 transactions and remove them from the the copy of transactions
  for i in range(0,5):
    top5.append(transactionHistory[i])
    transactionHistoryCopy.pop(i)

  #Sort the transactions
  top5.sort(key=ut.amount)

  #Test if each element is less than the 1st
  #If the element is less than the first append it and sort the list
  for transaction in transactionHistoryCopy:
    if (transaction['amount'] > top5[0]['amount']):
      top5.pop(0)
      top5.append(transaction)
      top5.sort(key = ut.amount)

  #Loop through the array backwards and return a dict of formatted strings
  strings = [0 for _ in range(0,5)]
  index = 0
  for transaction in reversed(top5):
    strings[index] = transaction["name"] + " - $" + str(transaction['amount'])
    index += 1

  return strings

#Code for the 4th chart
#Get the total spending of the last 30 days
def ch4(transactionHistory):

  #Create a new dictionary to represent the total amounts
  totals = {}

  #Create all possible dates in the last 30 days and add them to the dict
  baseDate = datetime.datetime.today()
  for i in reversed(range(0,31)):
    newDate = baseDate - datetime.timedelta(days=i)
    totals[newDate.strftime("%Y") + "-" + newDate.strftime("%m") + "-" + newDate.strftime("%d")] = 0

  #Add the corresponding transaction to each date
  for transaction in transactionHistory:
    print("Name: " + transaction['name'] + "  Category: " + transaction['category'][0] + "  Amount: " + str(
      transaction['amount']))
    if ((len(transaction) < 1) or (len(transaction['category']) > 1 and transaction['category'][1] != "Credit")):
      totals[transaction['date']] += transaction['amount']



  #Create a new dictionary where each of the keys are changed to just the day
  modifiedTotals = {}
  index2 = 0
  for date in totals:
    modifiedTotals[index2] = round(totals[date], 2)
    index2 += 1

  #Return the reversed list
  return modifiedTotals
  # prevDate = (datetime.date.today() + datetime.timedelta(-30)).day
  # #Loop through the transactions in reverse so that dates increase
  # for transaction in reversed(transactionHistory):
  #   currDate = int(transaction['date'][8:10])
  #
  #   #Second condition should only apply to the start of the loop
  #   #If the current date is more than 1 bigger than the previous date append 0's
  #   if (currDate > prevDate + 1):
  #     totals += ([0] * (currDate - prevDate - 1))
  #
  #   else:
  #     totals.append(transaction['amount'])
  #
  #   prevDate = currDate
  #
  # return reversed(totals)

  # #Create a new array that represents the totals of the last 30 days
  # totals = []
  # for i in range (0, 30):
  #   totals.append(0)
  #
  # #Loop through the transactions and add the amounts to the totals
  # index = 30
  # for transaction in transactionHistory:
  #   totals[index] = transaction['amount']
  #   index -= 1

#Code for the 5th chart
#Get the total spending of the last 12 months
def ch5(transactionHistory):

  #Create a new dictionary to represent the total amounts
  totals = {}

  #   #Create a series of labels that correspond to the labels
  labels = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun", "07":"Jul", "08":"Aug", "09":"Sep", "10":"Oct", "11":"Nov", "12": "Dec"}

  #Create all possible dates in the last 12 months and add them to the dict
  baseDate = datetime.datetime.today()
  for i in range(365,0, -1):
    newDate = baseDate - datetime.timedelta(days=i)
    monthAndYear = newDate.strftime("%Y") + "-" + newDate.strftime("%m")
    if (monthAndYear not in totals):
      totals[monthAndYear] = 0

  #Add the corresponding transaction to each date
  for transaction in transactionHistory:
    if ((len(transaction) < 1) or (len(transaction['category']) > 1 and transaction['category'][1] != "Credit")):
      totals[transaction['date'][0:7]] += round(transaction['amount'], 2)
    print("Name: " + transaction['name'] + "  Category: " + transaction['category'][0] + "  Amount: " + str(
      transaction['amount']))


  #Create a new dictionary where each of the keys are changed to just the day
  modifiedTotals = []
  for month in totals:
    modifiedTotals.append([labels[month[5:7]],round(totals[month], 2)])

  #Return the reversed list
  return modifiedTotals

# def ch5():
#
#   # months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
#   #
#   # monthTotals = {"01":0,"02","03","04","05","06","07","08","09","10","11","12"}
#   #
#
#   #
#   # for transaction in transactionHistory:
#   #   transactionMonth = transactionHistory['date'][4:6]
#
#   #Create a series of labels that correspond to the labels
#   labels = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12: "Dec"}
#
#   #Create a new dictionary that represents the amounts and months
#   totalYearTransactions = {}
#
#   #Get the current month
#   j = datetime.datetime.now().month
#
#   #Iterate through all possible months and use i and j as a modulus to wrap around
#   for i in range(0,13):
#     #Get the current month + i to represent
#     rawMonth = i + j
#     month = rawMonth % 12
#
#     #Represents when the month should start wrapping
#     year = (j // 12) - 1
#
#
#     #Get the transactions for the given month and year
#     transactions = get_transactions(days=None, year=year, start_date=month).json['transactions']
#
#     #Assign a variable for the sum cost of transactions
#     totalForMonth = 0
#
#     # Loop through the transactions for the month and add the amounts to totalForMonth
#     for transaction in transactions:
#       totalForMonth += transaction['amount']
#
#     #Create a new key in the dictionary that corresponds to the month and add the value of totalForMonth
#     totalYearTransactions[labels[month]] = totalForMonth
#
#   return totalYearTransactions

#Code for the 6th chart
#Output a list of strings representing transactions of the last 30 days
def ch6(transactionHistory):
  transactions = [0 for _ in transactionHistory]

  #Loop through the transactions and add them to the dictionary
  i = 0
  for transaction in transactionHistory:
    transactions[i] = "Name" + ": " + transaction["name"] + "   Amount: $" + str(transaction['amount']) + "   Date: " + \
                     transaction['date']
    i += 1

  return transactions






# This is an endpoint defined for the OAuth flow to redirect to.
@app.route('/oauth-response.html')
def oauth_response():
  return render_template(
    'oauth-response.html',
  )

# We store the access_token in memory - in production, store it in a secure
# persistent data store.

# The payment_id is only relevant for the UK Payment Initiation product.
# We store the payment_id in memory - in production, store it in a secure
# persistent data store.
payment_id = None

item_id = None

@app.route('/api/info', methods=['POST'])
def info():
  global access_token
  global item_id
  return jsonify({
    'item_id': item_id,
    'access_token': access_token,
    'products': PLAID_PRODUCTS
  })

@app.route('/api/create_link_token_for_payment', methods=['POST'])
def create_link_token_for_payment():
  global payment_id
  try:
    create_recipient_response = client.PaymentInitiation.create_recipient(
      'Harry Potter',
      'GB33BUKB20201555555555',
      {
        'street':      ['4 Privet Drive'],
        'city':        'Little Whinging',
        'postal_code': '11111',
        'country':     'GB'
      },
    )
    recipient_id = create_recipient_response['recipient_id']

    create_payment_response = client.PaymentInitiation.create_payment(
      recipient_id,
      'payment_ref',
      {
        'value': 12.34,
        'currency': 'GBP'
      },
    )
    pretty_print_response(create_payment_response)
    payment_id = create_payment_response['payment_id']
    response = client.LinkToken.create(
      {
        'user': {
          # This should correspond to a unique id for the current user.
          'client_user_id': 'user-id',
        },
        'client_name': "Plaid Quickstart",
        'products': PLAID_PRODUCTS,
        'country_codes': PLAID_COUNTRY_CODES,
        'language': "en",
        'redirect_uri': PLAID_REDIRECT_URI,
        'payment_initiation': {
          'payment_id': payment_id
        }
      }
    )
    pretty_print_response(response)
    return jsonify(response)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))

@app.route('/api/create_link_token', methods=['POST'])
def create_link_token():
  try:
    response = client.LinkToken.create(
      {
        'user': {
          # This should correspond to a unique id for the current user.
          'client_user_id': 'user-id',
        },
        'client_name': "Plaid Quickstart",
        'products': PLAID_PRODUCTS,
        'country_codes': PLAID_COUNTRY_CODES,
        'language': "en",
        'redirect_uri': PLAID_REDIRECT_URI,
      }
    )
    pretty_print_response(response)
    return jsonify(response)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))

# Exchange token flow - exchange a Link public_token for
# an API access_token
# https://plaid.com/docs/#exchange-token-flow
@app.route('/api/set_access_token', methods=['POST'])
def get_access_token():
  global access_token
  global item_id
  public_token = request.form['public_token']
  try:
    exchange_response = client.Item.public_token.exchange(public_token)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))

  pretty_print_response(exchange_response)
  access_token = exchange_response['access_token']
  item_id = exchange_response['item_id']
  return jsonify(exchange_response)


# Bypass Link and create a public token
# @app.route('/sandbox/public_token/create', methods=['GET'])
# def get_link():
#   global res
#   res = client.Sandbox.public_token.create(
#           "ins_118923",
#           ['transactions']
#         )
#   pretty_print_response(res)




# Bypass Link and create a public token
# @app.route('/sandbox/public_token/create', methods=['GET'])
# def exchange_link_for_access():
#   # The generated public_token can now be
#   # exchanged for an access_token
#   global access_token
#   publicToken = res['public_token']
#   access_token = client.Item.public_token.exchange(publicToken)
#
#   #Reassign access_token the proper subfield of the access token
#   access_token = access_token['access_token']
#   pretty_print_response(access_token)

# Retrieve ACH or ETF account numbers for an Item
# https://plaid.com/docs/#auth
@app.route('/api/auth', methods=['GET'])
def get_auth():
  try:
    auth_response = client.Auth.get(access_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(auth_response)
  return jsonify(auth_response)

# Retrieve Transactions for an Item
# https://plaid.com/docs/#transactions
@app.route('/api/transactions', methods=['GET'])
def get_transactions(year = None, start_date = None, end_date = None, days = None):

    # Pull transactions for the last 30 days
    if (not start_date and not end_date and not year):
      start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-days))
      end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
    else:
      currYear = datetime.datetime.today().year + year
      month = start_date
      startingDay = 1
      endingDay = monthrange(year, month)[1]
      start_date = '{:%Y-%m-%d}'.format(datetime.datetime(currYear, month, startingDay))
      end_date = '{:%Y-%m-%d}'.format(datetime.datetime(currYear, month, endingDay))

    try:
      transactions_response = client.Transactions.get(access_token, start_date, end_date, count=500)
    except plaid.errors.PlaidError as e:
      return jsonify(format_error(e))
    pretty_print_response(transactions_response)
    return jsonify(transactions_response)

# Retrieve Transactions for an Item
# https://plaid.com/docs/#transactions
# @app.route('/api/transactions', methods=['GET'])
# def get_transactions(start_date = None, end_date = None, days = None):
#
#     # Pull transactions for the last 30 days
#     if (not start_date and not end_date and not year):
#       start_date = '{:%Y-%m-%d}'.format((datetime.datetime.now() + datetime.timedelta(-days)) - (datetime.datetime.now() + datetime.timedelta(-days)))
#       end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
#
#
#     try:
#       transactions_response = client.Transactions.get(access_token, start_date, end_date)
#     except plaid.errors.PlaidError as e:
#       return jsonify(format_error(e))
#     pretty_print_response(transactions_response)
#     return jsonify(transactions_response)


# Retrieve Identity data for an Item
# https://plaid.com/docs/#identity
@app.route('/api/identity', methods=['GET'])
def get_identity():
  try:
    identity_response = client.Identity.get(access_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(identity_response)
  return jsonify({'error': None, 'identity': identity_response['accounts']})

# Retrieve real-time balance data for each of an Item's accounts
# https://plaid.com/docs/#balance
@app.route('/api/balance', methods=['GET'])
def get_balance():
  try:
    balance_response = client.Accounts.balance.get(access_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(balance_response)
  return jsonify(balance_response)

# Retrieve an Item's accounts
# https://plaid.com/docs/#accounts
@app.route('/api/accounts', methods=['GET'])
def get_accounts():
  try:
    accounts_response = client.Accounts.get(access_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(accounts_response)
  return jsonify(accounts_response)

# Create and then retrieve an Asset Report for one or more Items. Note that an
# Asset Report can contain up to 100 items, but for simplicity we're only
# including one Item here.
# https://plaid.com/docs/#assets
@app.route('/api/assets', methods=['GET'])
def get_assets():
  try:
    asset_report_create_response = client.AssetReport.create([access_token], 10)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(asset_report_create_response)

  asset_report_token = asset_report_create_response['asset_report_token']

  # Poll for the completion of the Asset Report.
  num_retries_remaining = 20
  asset_report_json = None
  while num_retries_remaining > 0:
    try:
      asset_report_get_response = client.AssetReport.get(asset_report_token)
      asset_report_json = asset_report_get_response['report']
      break
    except plaid.errors.PlaidError as e:
      if e.code == 'PRODUCT_NOT_READY':
        num_retries_remaining -= 1
        time.sleep(1)
        continue
      return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })

  if asset_report_json == None:
    return jsonify({'error': {'display_message': 'Timed out when polling for Asset Report', 'error_code': '', 'error_type': '' } })

  asset_report_pdf = None
  try:
    asset_report_pdf = client.AssetReport.get_pdf(asset_report_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })

  return jsonify({
    'error': None,
    'json': asset_report_json,
    'pdf': base64.b64encode(asset_report_pdf).decode('utf-8'),
  })

# Retrieve investment holdings data for an Item
# https://plaid.com/docs/#investments
@app.route('/api/holdings', methods=['GET'])
def get_holdings():
  try:
    holdings_response = client.Holdings.get(access_token)
  except plaid.errors.PlaidError as e:
    return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
  pretty_print_response(holdings_response)
  return jsonify({'error': None, 'holdings': holdings_response})

# Retrieve Investment Transactions for an Item
# https://plaid.com/docs/#investments
@app.route('/api/investment_transactions', methods=['GET'])
def get_investment_transactions():
  # Pull transactions for the last 30 days
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
  try:
    investment_transactions_response = client.InvestmentTransactions.get(access_token,
                                                                         start_date,
                                                                         end_date)
  except plaid.errors.PlaidError as e:
    return jsonify(format_error(e))
  pretty_print_response(investment_transactions_response)
  return jsonify({'error': None, 'investment_transactions': investment_transactions_response})

# This functionality is only relevant for the UK Payment Initiation product.
# Retrieve Payment for a specified Payment ID
@app.route('/api/payment', methods=['GET'])
def payment():
  global payment_id
  payment_get_response = client.PaymentInitiation.get_payment(payment_id)
  pretty_print_response(payment_get_response)
  return jsonify({'error': None, 'payment': payment_get_response})

# Retrieve high-level information about an Item
# https://plaid.com/docs/#retrieve-item
@app.route('/api/item', methods=['GET'])
def item():
  global access_token
  item_response = client.Item.get(access_token)
  institution_response = client.Institutions.get_by_id(item_response['item']['institution_id'])
  pretty_print_response(item_response)
  pretty_print_response(institution_response)
  return jsonify({'error': None, 'item': item_response['item'], 'institution': institution_response['institution']})

def pretty_print_response(response):
  print(json.dumps(response, indent=2, sort_keys=True))

def format_error(e):
  return {'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type, 'error_message': e.message } }


# get_link()
# exchange_link_for_access()
# analysis()
# x = 10

if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))
