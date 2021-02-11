from django.shortcuts import render

import requests

# This file contains view methods that are responsible for rendering the HTML templates. 
# The table_view renders the data table used on the main page of the website. 
# The blank_view was used for testing the 'Fetch Data' button.
def table_view(request):
	response = requests.get('https://api.usaspending.gov/api/v2/references/toptier_agencies/').json()["results"]
	key_headers = response[0].keys()
	values = [agency.values() for agency in response]
	context = {
		'response':response, 
		'key_headers':key_headers,
		'values':values
	}
	return render(request, 'table.html', context)

def blank_view(request):
	return render(request, 'blank.html', {})
