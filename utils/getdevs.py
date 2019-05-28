#!/usr/bin/python3

import requests

#headers = {"Authorization": "Bearer YOUR API KEY"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('http://argos-graph-ingress.argos.192.116.82.73.xip.io/graphql', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
{
    devices {
       id
       name
       type
       properties{
           key
           val
        }
     }
}
"""

result = run_query(query) # Execute the query
print(result['data'])
