from flask import Flask, jsonify
import re
import sqlite3

app = Flask(__name__)



def basic_sql(user_id, table_name):
    return f'(SELECT {table_name}.* FROM {table_name} NATURAL JOIN Entitlement{table_name} WHERE User = {user_id})'

QUERIES = {
    'all_events': 'SELECT * FROM {{ Events }}',
    'foo_count': 'SELECT SUM(foo) AS "foo_count" FROM {{ Timeseries }}',
    'all_files': 'SELECT * FROM {{ Datalake }}'
}

def safe_query(query_id, user_id):
    query = QUERIES[query_id]

    find_table_name = r"{{\s+(\S+)\s+}}"
    match = re.search(find_table_name, query)

    full_match, table_name = match.group(0), match.group(1)
    replacement = basic_sql(user_id, table_name)
    
    return query.replace(full_match, replacement)


@app.route('/query/<string:query_id>')
def query_data(query_id):
    user_id = 2

    q = safe_query(query_id, user_id)

    conn = sqlite3.connect('_data/db.sqlite')
    c = conn.cursor()

    print(q)
    
    result = [row for row in c.execute(q)]

    return jsonify(result)
