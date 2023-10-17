#!/usr/bin/env python3
"""List of school"""


def schools_by_topic(mongo_collection, topic):
    """List of school having spec topic"""
    cursor = mongo_collection.find({"topics": topic})
    documents = [document for document in cursor]
    return documents
