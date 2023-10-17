#!/usr/bin/env python3
"""Insert function"""


def insert_school(mongo_collection, **kwargs):
    """Insert"""
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
