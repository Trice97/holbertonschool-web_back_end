10-update_topics.py
"""Python function that changes all the topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document"""
    mongo_collection.update_one(
        {"name": name},
        {'$set': {"topics": topics}},
    )
