from pymongo import MongoClient  
from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
    
    
myclient = MongoClient("mongodb://localhost:27017/") 
# database  
db = myclient["innov"] 
    
# Created or Switched to collection  
# names: College 
collection = db["class"] 


    
classlist = [ 
    {"name": "Ankit", "age": "22"},
    {"name": "Preet", "age": "23"},
    {"name": "Venkat", "age": "21"}
] 

@app.route('/class/')
def studentView():
    data = collection.find_one()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)



# Inseting the entire list in the collection 
# collection.insert_many(classlist)
