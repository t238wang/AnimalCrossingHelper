from flask import request

# '/user/register/<swid>'
def register_user(swid):
    if not request:
        return 'i honestly dk...'
    req_data = request.get_json()
    name = req_data['name']
    island_name = req_data['island_name']
    hemisphere = req_data['hemisphere']
    return 'all good'