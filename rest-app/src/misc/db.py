from src.factory.db import MongoHandler

from src.misc.cast import safe_json_loads


def get_collections(mongo_handler: MongoHandler, db_name: str, collection_name: str):
    """
    Retrieve a MongoDB collection from a specified database.

    Args:
        mongo_handler (MongoHandler): An instance of MongoHandler for handling MongoDB connections.
        db_name (str): The name of the database containing the collection.
        collection_name (str): The name of the collection to retrieve.

    Returns:
        Collection: The MongoDB collection.
    """

    return mongo_handler.client[db_name][collection_name]


def get_data_from_cursor(cursor):
    """
    Extract data from a MongoDB cursor, converting ObjectId to string.

    Args:
        cursor (pymongo.cursor.Cursor): The MongoDB cursor.

    Returns:
        list: A list of dictionaries containing the extracted data, with ObjectId converted to string.
    """

    return [{**result, "_id": str(result.get("_id"))} for result in cursor]


def get_mongo_query_from_query_string(query_string: str):
    """
    Convert a JSON query string to a MongoDB query.

    Args:
        query_string (str): A JSON-formatted string representing a MongoDB query.

    Returns:
        dict: The MongoDB query dictionary.
    """
    
    query_json = safe_json_loads(query_string)
    query_list = [{key: value} for key, value in query_json.items()]

    if len(query_list) == 0:
        return {}
    
    return {"$and": query_list}
