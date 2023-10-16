"""
Real app this would make API calls 
and return data. In this app, it just 
returns random things. 
"""


import random 


def search(search_term):

    return {
        'api_1_result': len(search_term),   # length of search term
        'api_2_result': random.random() * 100,  # random float between 0-100
        'api_3_result': ''.join([ chr(random.randint(65, 65+24)) for _ in range(5)])  # string of 5 random letters
    }