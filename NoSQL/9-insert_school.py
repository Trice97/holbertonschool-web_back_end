#!/usr/bin/env python3


def insert_school(collection, name, address):
    """Insert a new school into the collection"""
    school = {"name": name, "address": address}
    result = collection.insert_one(school)
    return result.inserted_id