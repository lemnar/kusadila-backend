from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from activities import *


# Initializing flask app
app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})


A = Activities()

## activities/ transactions management
@app.route('/getactivities')
def get_activities(): 
    return A.get()

@app.route('/setactivities', methods=['POST'])
def set_activities(): 
    if request.is_json: 
        data = request.get_json()
        print(data)
        A.set(activities=data)
    return jsonify({"message": "Acvitivies transmitted"}), 200

## budget management


## add a budgeting category
# categories start with just "other" (not editable or deletable)


# @app.route('/getbudgets')



# Running app
if __name__ == '__main__':
    app.run(debug=True)

