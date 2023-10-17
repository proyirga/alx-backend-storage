#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection):
    """find top students"""
    cursor = mongo_collection.aggregate([
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}, "name": {"$first": "$name"}}},
        {"$sort": {"averageScore": -1}}
    ])
    documents = [document for document in cursor]
    return documents
