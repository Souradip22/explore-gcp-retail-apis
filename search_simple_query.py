import os
from google.cloud.retail import SearchRequest, SearchServiceClient

# Uncomment this line
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = <PATH_TO_YOUR_API_KEY> 

project_id = "explore-retail-search-api"


# get search service request:
def get_search_request(query: str):
    default_search_placement = (
        "projects/"
        + project_id
        + "/locations/global/catalogs/default_catalog/placements/default_search"
    )

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # the Serving Config name.
    search_request.query = query
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.page_size = 10

    print("---search request:---")
    print(search_request)

    return search_request


# call the Retail Search:
def search():
    # TRY DIFFERENT QUERY PHRASES HERE:
    query_phrase = "tshirts"

    search_request = get_search_request(query_phrase)
    search_response = SearchServiceClient().search(search_request)

    print("---search response---")
    if not search_response.results:
        print("The search operation returned no matching results.")
    else:
        print(search_response)
    return search_response


search()
