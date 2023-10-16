"""

Replace this with calls to update and query a real database.

"""

pretend_bookmarks = []

def add_new_bookmark(bookmark_data):
    # bookmark_data might be an object, or a dictionary, or you might have 
    # multiple arguments to  this function
    # real app saves to a database, checks for duplicates, does error handling
    pretend_bookmarks.append(bookmark_data)


def get_all_bookmarks():
    # real app queries database, does error handling
    return pretend_bookmarks