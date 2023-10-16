import pretend_database
import pretend_api_manager
import api_results_store

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/search')
def api_search():
    search_term = request.args.get('search_term')
    results = pretend_api_manager.search(search_term)
    # save results in temporary store in case user wants to bookmark them later
    # generate some unique value that can be used to look up the results later
    api_result_id = api_results_store.save_api_result(search_term, results)
    # include the api_result_id in the data sent to the template 
    return render_template('search_result.html', search_term=search_term, results=results, result_id=api_result_id)


@app.route('/save_bookmark', methods=['POST'])
def save_bookmark():
    result_id = request.form.get('result_id')
    # Get stored result from api result store, look up by id
    results_and_id = api_results_store.fetch_stored_api_result(result_id)
    # save results to real bookmark database 
    results = results_and_id['results']
    pretend_database.add_new_bookmark(results)
    # fetch all the bookmarks
    all_bookmarks = pretend_database.get_all_bookmarks()
    # render in template
    return render_template('bookmarks.html', bookmarks=all_bookmarks)


if __name__ == '__main__':
    app.run()

