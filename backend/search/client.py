from algoliasearch_django import algolia_engine

# initializing the client
def get_client():
    return algolia_engine.client

# get the clients index
def get_index(index_name='alex_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index

# Perform the search 
def perform_search(query, **kwargs):
    """
    perform_search("hello", tags=["electronics"], public=True
    """
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilter'] = tags
    
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]
    if len(index_filters) != 0:
        params['facetFilters'] = index_filters
    print(params)
    result = index.search(query, params)
    return result