from replit import db

resources = [
    'users'
]

try:
    for resource in resources:
        db[resource] = db.get(resource, [])
except:
    db = {}
    for resource in resources:
        db[resource] = []
