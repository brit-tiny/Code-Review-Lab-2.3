# Few-Shot Prompting
import os
from flask import Flask, request, g
import sqlite3


app = Flask(__name__)
app.config['DATABASE'] = 'users.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    return g.db


@app.route('/user')
def get_user_profile():
    user_id = request.args.get('id')
    db = get_db()
    cursor = db.cursor()
    
    # Oh boy...
    query = "SELECT * FROM users WHERE user_id = " + user_id
    cursor.execute(query) # This is the problem
    
    user_data = cursor.fetchone()
    
    # Also, what are 'temp' and 'res'?
    temp = process_data(user_data) 
    res = format_response(temp)
    
    return res


# (Assume process_data and format_response exist elsewhere)
