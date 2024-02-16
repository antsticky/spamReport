from typing import Dict, Annotated
from fastapi import APIRouter, Query, HTTPException

from src.factory import MongoHandler

from src.schemes.body import TicketStateUpdate
from src.misc.db import get_collections, get_data_from_cursor, get_mongo_query_from_query_string


router = APIRouter()

spams_collection = get_collections(MongoHandler.from_envvar(), "reports", "spams")



@router.get("")
def endpoint_get_reports(q: Annotated[str | None, Query()] = None, page: int = 1, page_size: int = 10, sort_by: str = None, sort_direction: int = 1):
    """
    Endpoint to retrieve reports with optional filtering, pagination, and sorting.

    Args:
        q (str, optional): Optional query string for filtering results.
        page (int, optional): Page number for pagination (default: 1).
        page_size (int, optional): Number of items per page (default: 10).
        sort_by (str, optional): Field to sort results by.
        sort_direction (int, optional): Sort direction: 1 (ascending) or -1 (descending).

    Returns:
        dict: A JSON response containing the filtered, paginated, and sorted results.
    """    

    skip = (page - 1) * page_size
    mongo_q = get_mongo_query_from_query_string(q)

    if sort_by is None:
        results = spams_collection.find(mongo_q).skip(skip).limit(page_size)
    else:
        results = spams_collection.find(mongo_q).sort(sort_by, sort_direction).skip(skip).limit(page_size)

    result_list = get_data_from_cursor(results)

    return {"results": list(result_list)}




@router.put("/{item_id}")
def endpoint_change_ticket_state(item_id: str, status_update: TicketStateUpdate):   
    """
    Endpoint to change the state of a ticket identified by its ID.

    Args:
        item_id (str): The ID of the ticket to update.
        status_update (TicketStateUpdate): Object containing the new state of the ticket.

    Returns:
        dict: A JSON response indicating the success of the operation.

    Raises:
        HTTPException: If the document is not found or no modifications were made.
    """
    
    filter_criteria = {"id": item_id}
    update_operation = {"$set": {"state": status_update.ticketState}}

    result = spams_collection.update_one(filter_criteria, update_operation)

    if result.modified_count == 1:
        return {"message": "Ticket state updated successfully."}
    
    raise HTTPException(status_code=400, detail="Document not found or no modifications were made.")

