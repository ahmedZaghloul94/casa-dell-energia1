
from fastapi import FastAPI
import read,delete,CUD
import psycopg2
import station,resource_model,position,resource,rent
import datetime
from abbrevationdictionary import *
router = FastAPI()
@router.get("/get_stations/{id}")
def get_station(st_id: int):
    try:
        results = read.call_get_station(st_id)
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

@router.get("/get_all_stations/")
def get_all_stations():
    try:
        results = read.call_get_all_station()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_model_resources/{id}")
def get_model_resources(MR_id: int):
    try:
        results = read.call_get_model_resources(MR_id)
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_model_resources/")
def get_all_model_resources():
    try:
        results = read.call_get_all_model_resources()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_rents/{id}")
def get_rents(R_id: int):
    try:
        results = read.call_get_rents(R_id)
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_all_rents/")
def get_all_rents():
    try:
        results = read.call_get_all_rents()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_resources/{id}")
def get_resources(RE_id: int):
    try:
        results = read.call_get_resources(RE_id)
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.get("/get_all_resources/")
def get_all_resources():
    try:
        results = read.call_get_all_resources()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.put("/update_or_insert_stations/")
def insert_or_update_station(station_id: int, station_data: station.Station):
    try:
        results=CUD.insert_or_update_station(station_id,station_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

        
@router.post("/update_or_insert_stations/")
def insert_or_update_station(station_id: int, station_data: station.Station):
    try:
        results=CUD.insert_or_update_station(station_id,station_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.put("/update_or_insert_model_resource/")
def insert_or_update_model_resource(model_resources_id: int, model_resource_data: resource_model.ResourceModel):
    try:
        results=CUD.insert_or_update_model_resource(model_resources_id,model_resource_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

@router.post("/update_or_insert_model_resource/")
def insert_or_update_model_resource(model_resources_id: int, model_resource_data: resource_model.ResourceModel):
    try:
        results=CUD.insert_or_update_model_resource(model_resources_id,model_resource_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@router.put("/update_or_insert_resource/")
def insert_or_update_resource(resources_id: int,st_id :int,MR_id :int,resource_data: resource.Resource):
    try:
        results=CUD.insert_or_update_resource(resources_id,st_id,MR_id,resource_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

@router.post("/update_or_insert_resource/")
def insert_or_update_resource(resources_id: int,st_id: int,MR_id :int, resource_data: resource.Resource):
    try:
        results=CUD.insert_or_update_resource(resources_id,st_id,MR_id,resource_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)        


@router.post("/update_or_insert_rent/")
def insert_or_update_resource(rent_data: rent.Rent):
    try:
        print("ok")
        results=CUD.insert_or_update_rent(rent_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 

@router.put("/update_or_insert_rent/")
def insert_or_update_resource(rent_data: rent.Rent):
    try:
        print("ok")
        results=CUD.insert_or_update_rent(rent_data)
        return {S_M}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  


@router.delete('/stations/{station_id}')
def delete_station(station_id: int):
    results=delete.call_delete_station(station_id)
    return {S_M}

@router.delete('/model_resources/{model_resources_id}')
def delete_station(model_resources_id: int):
    results=delete.call_delete_model_resources(model_resources_id)
    return {S_M}

@router.delete('/resources/{resources_id}')
def delete_station(resources_id: int):
    results=delete.call_delete_resources(resources_id)
    return {S_M}
@router.delete('/rent/{rent_id}')
def delete_station(rent_id: int):
    results=delete.call_delete_rent(rent_id)
    return {S_M}       
