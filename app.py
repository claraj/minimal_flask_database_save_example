import pretend_database
import pretend_api_manager

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/search')
def api_search():
    search_term = request.args.get('search_term')
    results = pretend_api_manager.search(search_term)
    return render_template('search_result.html', search_term=search_term, results=results)


@app.route('/save_bookmark', methods=['POST'])
def save_bookmark():
    save_request_data = request.form.to_dict()
    print(save_request_data)
    pretend_database.add_new_bookmark(save_request_data)
    all_bookmarks = pretend_database.get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=all_bookmarks)



if __name__ == '__main__':
    app.run()

