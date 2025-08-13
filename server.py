from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from activities import *
from budget import * 


# Initializing flask app
app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

B = Budget()
A = Activities()

## activities/ transactions management
@app.route('/getactivity')
def getActivity(): 
    return A.activity

@app.route('/setactivity', methods=['POST'])
def setActivity(): 
    if request.is_json: 
        data = request.get_json()
        print(data)
        A.activity = data
    return jsonify({"message": "Acvitivies transmitted"}), 200

## budget management
@app.route('/setcategories', methods=['POST'])
def setCategories():
    if request.is_json: 
        data = request.get_json()
        for cat in data: 
            activity = A.getFromCategory(cat['name'])
            if activity: 
                cat['activity'] = activity
            else: 
                cat['activity'] = []
        B.setCategories(data)
        print(B.getCategories())
        return jsonify({"message" : "Categories transmitted"})
    
@app.route('/getcategories')
def getCategories(): 
    return B.getCategories()

## add a budgeting category
# categories start with just "other" (not editable or deletable)





# Running app
if __name__ == '__main__':
    app.run(debug=True)

