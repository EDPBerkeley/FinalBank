import plaid
import json
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)
client = plaid.Client(client_id=PLAID_CLIENT_ID,
                      secret=PLAID_SECRET,
                      environment=PLAID_ENV,
                      api_version='2019-05-29')
@app.route('/create_link_token')
  # 1. Grab the client_user_id by searching for the current user in your database
  user = User.find(...)
  client_user_id = user.id
  # 2. Create a link_token for the given user
  response = client.LinkToken.create({
    'user': {
      'client_user_id': client_user_id,
    },
    'products': ["transactions"],
    'client_name': "My App",
    'country_codes': ['US'],
    'language': 'en',
    'webhook': 'https://sample.webhook.com',
  })
  link_token = response['link_token']
  # 3. Send the data to the client
  return jsonify(response)

if __name__ == '__main__':
  app.run(port=3000)