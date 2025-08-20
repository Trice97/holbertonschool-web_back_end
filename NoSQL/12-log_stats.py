#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Connexion à MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    # Nombre total de logs
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))
    
    # Méthodes
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    
    # Status check (GET + path=/status)
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
