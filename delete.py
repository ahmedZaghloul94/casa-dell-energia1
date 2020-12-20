from Connect_TO_DB import Connect_TO_DB

def call_delete_station(ST_id :int):
    select_Query="select * from delete_station(%s);"
    res=Connect_TO_DB(select_Query,(ST_id,))
    return res

def call_delete_model_resources(MR_id: int):
    select_Query="select * from delete_model_resources(%s);"
    res=Connect_TO_DB(select_Query,(MR_id,))
    return res


def call_delete_resources(RE_id: int):
    select_Query="select * from delete_resources(%s);"
    res=Connect_TO_DB(select_Query,(RE_id,))
    return res

def call_delete_rent(R_id: int):
    select_Query="select * from delete_rent(%s);"
    res=Connect_TO_DB(select_Query,(R_id,))
    return res