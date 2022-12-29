import json

def fetch_user_data():
    
    jsonFile = open("user_data.json","r")
        
    try:
        data = json.load(jsonFile)
    except Exception as e:
        data = []
    jsonFile.close()
    return data

def update_user_data(data):
    jsonFile = open("user_data.json","w")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
    
    
# ORm - object relational mapper

# define table into classes

# makemigrations -- convert all classes into specific db quries
#migrate - Execute db quries made by makemigration