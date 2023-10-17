#!/usr/bin/env python3
"""Python fuvtion lists all docs - mongodb"""


def list_all(mongo_collection):
    """list all"""
    cursor = mongo_collection.find({})
    documents = [document for document in cursor]
    return documents
