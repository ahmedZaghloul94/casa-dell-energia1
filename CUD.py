from Connect_TO_DB import Connect_TO_DB
import datetime
import station,rent,resource_model,position,resource
import json
from abbrevationdictionary import *
    
def insert_or_update_station(ST_id: int, station_data: station.Station):
    select_Query="select from create_or_update_station(%s,%s);"
    station_data = str(json.dumps(station_data.dict()))
    data=(ST_id,station_data,)
    res=Connect_TO_DB(select_Query,data)
    return {}

def insert_or_update_model_resource(MR_id: int, model_resource_data: resource_model.ResourceModel):
    select_Query="select from create_or_update_model_resources(%s,%s);"
    model_resource_data = str(json.dumps(model_resource_data.dict()))
    data=(MR_id, model_resource_data,)
    res=Connect_TO_DB(select_Query,data)
    return {}

def insert_or_update_resource(RE_id: int, ST_id: int, MR_id: int, resource_data: resource.Resource):
    resource_data = str(json.dumps(resource_data.dict()))
    select_Query="select from create_or_update_resources(%s,%s,%s,%s);"
    data=(RE_id, ST_id, MR_id, resource_data,)
    res=Connect_TO_DB(select_Query,data)
    return {}

def insert_or_update_rent(rent_data: rent.Rent):
    rent_data = rent_data.dict()
    rent_id = rent_data['rent_id']
    resource_id = rent_data['resource_id']
    User_id = rent_data['user_id']
    if(User_id == 0):
        User_id = None
    StartStation_id = rent_data['StartStation_id']
    EndStation_id = rent_data['EndStation_id']
    if(EndStation_id == 0):
        EndStation_id = None
    Departure_station_time = rent_data['StartTime']
    Departure_station_time = Departure_station_time.replace(tzinfo=None)
    Departure_station_time = int(
        (Departure_station_time - epoch).total_seconds() * 1000.0)
    Arrival_station_time = rent_data['EndTime']
    if(Arrival_station_time != "string"):
        Arrival_station_time=datetime.datetime.strptime(Arrival_station_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        Arrival_station_time = Arrival_station_time.replace(tzinfo=None)
        Arrival_station_time = int((Arrival_station_time -
                                epoch).total_seconds() * 1000.0)
    else:
        Arrival_station_time = None
    rent_data = str(json.dumps({"Cost": rent_data['rentCost']}))
    select_Query="select from create_or_update_rents(%s,%s,%s,%s,%s,%s,%s,%s);"
    data=(rent_id, StartStation_id, Departure_station_time, resource_id,
                    rent_data, User_id, EndStation_id, Arrival_station_time,)

    res=Connect_TO_DB(select_Query,data)                
    return {}
