#!/usr/bin/env python3
"""Update topic"""


def update_topics(mongo_collection, name, topics):
    """Update topic"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(query, new_values)
    return result.modified_count
