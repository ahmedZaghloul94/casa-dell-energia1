
from datetime import datetime
import station,resource_model,position,rent
from abbrevationdictionary import *
from Connect_TO_DB import Connect_TO_DB

def call_get_station(st_id: int):
    select_Query = "select * from get_station_data_by_id(%s);"
    res = Connect_TO_DB(select_Query, (st_id,))
    print((res[0])[RE_ID])
    resources_results = []
    for x in range(0, len(res)):
        resources_results.append({RE_ID: ((res[x])[RE_ID]), RE_D: (
            (res[x])[RE_D]), MR_ID: ((res[x])[MR_ID]), MR_D: ((res[x])[MR_D])})

    return {ST_ID: ((res[0])[ST_ID]), D: ((res[0])[D]), "Resources": resources_results}

def call_get_all_station():
    select_Query = "select * from get_all_station_ids();"
    res = Connect_TO_DB(select_Query)
    F_results = []  # final results
    for x in range(0, len(res)):
        results = call_get_station((res[x])[ST_ID])
        F_results.append(results)

    return {"stations": F_results}

def call_get_model_resources(MR_Id: int):
    select_Query = "select * from get_model_resources_data(%s);"
    res = Connect_TO_DB(select_Query, (MR_Id,))
    return {MR_ID: ((res[0])[MR_ID]), D: ((res[0])[D])}


def call_get_all_model_resources():
    select_Query = "select * from get_all_model_resources_ids();"
    res = Connect_TO_DB(select_Query)
    F_results = []  # final results
    for x in range(0, len(res)):
        results = call_get_model_resources((res[x])[MR_ID])
        F_results.append(results)
    return {"model_resources": F_results}

def call_get_rents(R_id: int):
    select_Query = "select * from get_rent_data(%s);"
    res = Connect_TO_DB(select_Query, (R_id,))
    if (((res[0])[D_DT]) != None):
        start_time = datetime.fromtimestamp(
            ((res[0])[D_DT]) // 1000)
    else:
        start_time = 'Null'

    if (((res[0])[A_DT]) != None):
        end_time = datetime.fromtimestamp(
            ((res[0])[A_DT]) // 1000)

    else:
        end_time = 'Null'

    return {R_ID: ((res[0])[R_ID]), D_ST_ID: ((res[0])[D_ST_ID]), D_ST_D: ((res[0])[D_ST_D]),
            A_ST_ID: ((res[0])[A_ST_ID]), A_ST_D: ((res[0])[A_ST_D]), R_D: ((res[0])[R_D]), D_DT:
            start_time, A_DT: end_time, RE_ID: ((res[0])[RE_ID]), R_M_R_ID: ((res[0])[R_M_R_ID]),
            R_R_D: ((res[0])[R_R_D]), C_ST_ID: ((res[0])[C_ST_ID]), C_ST_D: ((res[0])[C_ST_D]),
            U_ID: ((res[0])[U_ID])}

def call_get_all_rents():
    select_Query = "select * from get_all_rents_ids();"
    res = Connect_TO_DB(select_Query)
    F_results = []  # final results
    for x in range(0, len(res)):
        results = call_get_rents((res[x])[R_ID])
        F_results.append(results)

    return {"Rents": F_results}

def call_get_resources(RE_id: int):
    select_Query = "select * from get_resources_data(%s);"
    res = Connect_TO_DB(select_Query, (RE_id,))
    # return the results of get_recent_rents
    results2 = get_recent_rents(RE_id)
    return {RE_ID: ((res[0])[RE_ID]), RE_D: ((res[0])[RE_D]), MR_ID: ((res[0])[MR_ID]), MR_D: ((res[0])[MR_D]),
            C_ST_ID: ((res[0])[ST_ID]), C_ST_D: ((res[0])[ST_D]), L_R: results2}

def call_get_all_resources():
    select_Query = "select * from get_all_resources_ids();"
    res = Connect_TO_DB(select_Query)
    F_results = []  # final results
    for x in range(0, len(res)):
        results = call_get_resources((res[x])[RE_ID])
        F_results.append(results)

    return {"Resources": F_results}

def get_recent_rents(resources_id: int):
     select_Query = "select * from get_recent_rents_data(%s);"
     res1 = Connect_TO_DB(select_Query, (resources_id,))
     res3=[]
     for x in range(0, len(res1)):
        if (((res1[x])[D_DT]) != None):
            start_time = datetime.fromtimestamp(
                    ((res1[x])[D_DT]) // 1000)
        else:
             start_time = 'Null'
        if (((res1[x])[A_DT]) != None):
                end_time = datetime.fromtimestamp(
                    ((res1[x])[A_DT]) // 1000)
        else:
                end_time = 'null'

        res3.append({R_ID: ((res1[x])[R_ID]),
                    D_DT: start_time,
                    A_DT: end_time, U_ID: ((res1[x])[U_ID]), R_D: ((res1[x])[R_D]),
                    D_ST_ID: ((res1[x])[D_ST_ID]), D_ST_D: ((res1[x])[D_ST_D]),
                    A_ST_ID: ((res1[x])[A_ST_ID]), A_ST_D: ((res1[x])[A_ST_D])})
     return res3
