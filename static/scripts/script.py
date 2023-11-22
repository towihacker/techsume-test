from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make an API request
    api_url = 'https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}'
    response = requests.get(https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314})

    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', data=data)
    else:
        return 'API request failed'

if __name__ == '__main__':
    app.run(debug=True)

import requests 
response =
request.get('https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}')

if response.status_code==200:
    print("Succesful connection with API.")
    print('--------------------------------')
    data = response.json()
    print(data)
elif response.status_code==404:
  print("unable to reach URL.")
else:
  print("Unable to connect to API or retrieve data.")
  print("Error code: ", response.status_code)
  
import requests
response = requests.get('https://api.adzuna.com/v1/api/jobs/gb/search/1', params={'id' :"4e236f34-b981-41c3-8c65-f8c9000b94e7"})

if response.status_code == 200:
    print("Successful connection with API.")
    print('-------------------------------')
    data = response.json()
elif response.status_code == 404:
      print("Unable to reach URL.")
else:
    print("Unable to connect API or retrieve data.")
for record in data:
       print("Title: {},\n Release_Date: {},\n Director: {},\n".format(record['title'] , record['release_date'],record['director']))

import requests
# Define API endpoint and parameters
api_url = "https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}
"
params = {"job_type": "software_engineer"}

# Make the GET request
response = requests.get(https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}, params=params)

if response.status_code == 200:
    # Process the job listings in response.json()
    job_listings = response.json()
    for job in job_listings:
        print(job['title'])
else:
    print(f"API request failed with status code {response.status_code}")


