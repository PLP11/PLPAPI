import requests

from django.shortcuts import render
# weather/views.py


def home(request):
  # USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["repo"]

  # Example 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2["message"]

  response3 = requests.get('https://freetestapi.com/api/v1/students') # Use this API
  data3 = response3.json()
  name = data3[0]['name']

  return render(request, 'templates/index.html', {
      'result': result,
      'result2': result2,
      'name': name
  })
