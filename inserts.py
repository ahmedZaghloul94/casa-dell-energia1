import psycopg2
import psycopg2.extras
import datetime
import station
import resource_model
import position
import resource
import json
import rent
import abbrevationdictionary
epoch = datetime.datetime.utcfromtimestamp(0)


def insert_or_update_station(ST_id: int, station_data: station.Station):
    con = psycopg2.connect(dbname=DB_name, user=DB_user,
                           password=DB_pass, host=DB_Host)
    cur = con.cursor()
    station_data = str(json.dumps(station_data.dict()))

    print(station_data)
    cur.execute('show search_path; set search_path to casa_della_energia ;select from create_or_update_station(%s,%s);',
                (ST_id, station_data))

    res = cur.fetchall()
    con.commit()
    cur.close()
    print(res)
    if con is not None:
        con.close()
    return {}


def insert_or_update_model_resource(MR_id: int, model_resource_data: resource_model.ResourceModel):
    con = psycopg2.connect(dbname=DB_name, user=DB_user,
                           password=DB_pass, host=DB_Host)
    cur = con.cursor()
    model_resource_data = str(json.dumps(model_resource_data.dict()))

    cur.execute('show search_path; set search_path to casa_della_energia ;select from create_or_update_model_resources(%s,%s);',
                (MR_id, model_resource_data))

    res = cur.fetchall()
    con.commit()
    cur.close()
    print(res)
    if con is not None:
        con.close()
    return {}


def insert_or_update_resource(RE_id: int, ST_id: int, MR_id: int, resource_data: resource.Resource):
    con = psycopg2.connect(dbname=DB_name, user=DB_user,
                           password=DB_pass, host=DB_Host)
    cur = con.cursor()
    resource_data = str(json.dumps(resource_data.dict()))

    cur.execute('show search_path; set search_path to casa_della_energia ;select from create_or_update_resources(%s,%s,%s,%s);',
                (RE_id, ST_id, MR_id, resource_data))

    res = cur.fetchall()
    con.commit()
    cur.close()
    print(res)
    if con is not None:
        con.close()
    return {}


def insert_or_update_rent(rent_data: rent.Rent):
    con = psycopg2.connect(dbname=DB_name, user=DB_user,
                           password=DB_pass, host=DB_Host)
    cur = con.cursor()

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
        Arrival_station_time = Arrival_station_time.replace(tzinfo=None)
        Arrival_station_time = (Arrival_station_time -
                                epoch).total_seconds() * 1000.0
    else:
        Arrival_station_time = None
    rent_data = str(json.dumps({"Cost": rent_data['rentCost']}))
    print(EndStation_id)
    print(Departure_station_time)
    print(Arrival_station_time)
    print(rent_data)
    cur.execute('show search_path; set search_path to casa_della_energia ;select from create_or_update_rents(%s,%s,%s,%s,%s,%s,%s,%s);',
                (rent_id, StartStation_id, Departure_station_time, resource_id,
                    rent_data, User_id, EndStation_id, Arrival_station_time))
    res = cur.fetchall()
    con.commit()
    cur.close()
    print(res)
    if con is not None:
        con.close()
    return {}
