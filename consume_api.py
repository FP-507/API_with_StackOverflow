import requests
import json

try:
    #we get the data from the API using requests library and a variable
    response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Store the response data to avoid multiple API calls
    response_data = response.json()
    
    # Check if the response has the expected structure
    if 'items' not in response_data:
        print("Error: Unexpected API response structure")
        exit()

    #we print the response in json format
    #print(response_data['items'])

    #With a loop through the items in the response and print the title of each item and analyze this data in so easy way
    for data in response_data['items']:
        print(f"Title: {data['title']}")
        print(f"Tags: {', '.join(data['tags'])}")
        print(f"Score: {data['score']}")
        print(f"View Count: {data['view_count']}")
        print(f"Link: {data['link']}")
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON response: {e}")
except KeyError as e:
    print(f"Error: Missing expected field in API response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
