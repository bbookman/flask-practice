import os, pdb
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome_view():
    return 'Welcome to our Flask Practice!'


@app.route('/sum/<int:first_number>/<int:second_number>')
def sum_of_two_numbers(first_number, second_number):
    """Implement a view that receives two numbers and returns the sum of them"""
    total = first_number + second_number
    return 'The sum of {} and {} is: {}'.format(first_number, second_number, total)

@app.route('/username/<first_name>/<last_name>')
def build_username(first_name, last_name):
    """
        Implement a view that receives user's first name and last name,
        and returns its username built with first letter of the first name,
        concatenated with the last name.

        i.e: username for "Elon Musk" would be "emusk"
    """
    return first_name[0].lower() + last_name.lower()

@app.route('/user')
def search_user():
    users = ['Jack', 'Morgan', 'Moe', 'Steve']
    search_param = request.args.get('search')
    pdb.set_trace()
    count = 0
    for user in users:
        if search_param.lower() in user.lower():
            count += 1
    return 'Found {count} users that match with search "{search_param}'.format(count = count, search = search_param)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
