from flask import Flask, request, render_template
from database import init_db, add_transaction
from datetime import date as date_notime

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transactions")
def transactions():
    return "Transactions will live here"

@app.route("/transactions", methods=['POST'])
def post_transaction():
    
    type_data = {"description":str, "amount":float, "category":str }
    error_flag = False

    data = request.get_json()

    
    if len(data) != 4:
        return "Missing Data", 400
 
    description = data.get("description")
    amount = data.get("amount")
    category = data.get("category")
    # separate date validation cause str in not date obj
    try:
        date = date_notime.fromisoformat(data.get("date"))
    except ValueError:
        return "Invalid Date Format", 400

    # if a field/key in request is invalid, loop catches it as .get returns None, and types don't match
    for key in type_data.keys():
        if  type_data.get(f"{key}") != type(data.get(f"{key}")):
            error_flag = True
    
    if error_flag: 
        return "Invalid Input", 400
    else:
        add_transaction(description, amount, date, category)
        return "Successful transaction input", 201


    

if __name__ == "__main__":
    app.run(debug=True)


