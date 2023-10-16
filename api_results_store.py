""" Stores all API results, probably on a temporary basis
Consider including time saved so can ignore old results """

from uuid import uuid4  # this library generates unique ID values
# you can also use the generated ID values in SQLite 

all_results = {}  # replace with db  

def save_api_result(search_term, result):
    unique_id = str(uuid4())
    all_results[unique_id] = { 'search_term': search_term, 'result': result }
    return unique_id

def fetch_stored_api_result(id):
    print(all_results)
    return all_results.get(id)  # None if not found