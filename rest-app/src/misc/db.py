from src.factory.db import MongoHandler

from src.misc.cast import safe_json_loads


def get_collections(mongo_handler: MongoHandler, db_name: str, collection_name: str):
    return mongo_handler.client[db_name][collection_name]


def get_data_from_cursor(cursor):
    return [{**result, "_id": str(result.get("_id"))} for result in cursor]


def get_mongo_query_from_query_string(query_string: str):
    query_json = safe_json_loads(query_string)
    query_list = [{key: value} for key, value in query_json.items()]

    if len(query_list) == 0:
        return {}
    
    return {"$and": query_list}
