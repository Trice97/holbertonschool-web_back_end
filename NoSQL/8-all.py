#!/usr/bin/env python3

def list_all(mongo_collection):
    """return a list of all the documents in a MONGODB collection"""
    return list(mongo_collection.find())
