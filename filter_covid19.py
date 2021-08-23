
# coding: utf-8

import pandas as pd
import numpy as np
import json, io
import os, sys, time, datetime, getopt, argparse
import urllib
##確認中文編碼可執行
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import cx_Oracle
import pyodbc
import pymysql
import warnings
import sqlalchemy
warnings.filterwarnings("ignore")

from sqlalchemy import create_engine,text
from pandas.core.frame import DataFrame
from datetime import timedelta, date, datetime
from sqlalchemy import create_engine, text


# # Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument('--work_id', type=str, default="")
parser.add_argument('--file_name', type=str, default="")
parser.add_argument('--start_time', type=str, default="")
parser.add_argument('--end_time', type=str, default="")
parser.add_argument('--time_range', type=int, default="")
parser.add_argument('--area_range', type=str, default="")

# Read arguments from command line
args = parser.parse_args()

work_id = args.work_id
file_name = args.file_name
start_time = args.start_time
end_time = args.end_time
time_range = args.time_range
area_range = args.area_range

appear_time_list = []
range_of_time = []

appear_fabtime_list = []
range_of_fabtime = []

appear_bustime_list = []

appear_dortime_list = []
range_of_dortime = []

appear_tridoortime_list = []
range_of_tridoortime = []

# ## 辦公室



server = '10.96.48.5' #IP:port
DBuser = 'hid_record'
password = 'hid_record$dss0'
database = 'hid_record_db'
port = '3306'

conn_str = r'mysql+pymysql://'+DBuser+':'+password+'@'+server+':'+port+'/'+database #sql server帳號驗證
engine = create_engine(conn_str)

# 開啟連線
with engine.begin() as conn:
    sql = """select * FROM hid_record_db.summary_record WHERE entry_time BETWEEN 
    '"""+ start_time + """' And '"""+ end_time + """' ORDER BY entry_time;
    """
 
    result = conn.execute(text(sql))
    #欄位名稱
    columns = result.keys()
    data = result.fetchall()
    df_office = pd.DataFrame(data,columns=columns) # 爬出當天出勤人數




# show infected's entry_time
df_office_infected = df_office[df_office['WORKERID'] == work_id].reset_index(drop=True)
infected_location = []
for i in range(len(df_office_infected)):
    infected_location.append(df_office_infected['location_number'].get(i)[:2])



# 匡列辦公室

def connect_db(index):
    with engine.begin() as conn:
        sql = """select NAME, WORKERID, entry_time,  location_number, DEPARTMENT FROM hid_record_db.summary_record WHERE (entry_time BETWEEN 
        '"""+ str(appear_time_list[index]) + """' And '"""+ str(range_of_time[index]) + """') and location_number LIKE '"""  + infected_location[index] + """%';
        """
        result = conn.execute(text(sql))
        #欄位名稱
        columns = ['name', 'work_id', 'clock_in_time', 'postition', 'area']

        data = result.fetchall()
        return data, columns



def output_potential_people():
    # if didn't appear in the office
    if len(df_office_infected) == 0:
        print('Did not appear in the office.')
        return
    
    appear_time_index = df_office_infected['entry_time'].index
    for i in appear_time_index:
        appear_time_list.append(df_office_infected['entry_time'][i])

    # add time_range => new list of entry_time to filter people who entry after infected. 
    for item in appear_time_list:
        range_of_time.append(item + timedelta(seconds=time_range))
    
    potential, col = [], connect_db(0)[1]
    
    for i in range(0, len(appear_time_list)):
        potential.append(connect_db(i)[0])

    # flat list 
    flat_list = sum(potential, [])

    df_potential = pd.DataFrame(flat_list, columns=col)
    df_potential = df_potential[df_potential['work_id'] != work_id]
    df_potential['clock_out_time'] = ""
    
    new_index = ['name', 'work_id', 'clock_in_time', 'clock_out_time', 'postition', 'area']
    df = df_potential.reindex(new_index, axis="columns")
    return df.reset_index(drop=True)


# FAB 匡列


##前段即時門禁資料##
try:
    temp_IN_data = pd.DataFrame()
    conn = cx_Oracle.connect('L6ACEL_AP','L6ACEL$AP','l6adoor1/L6ADOOR.CORPNET.AUO.COM')
 
    sqlquery =  """
        select distinct WORKID, INTIME, INDOOR, OUTTIME
        FROM DOORCTL.T_CRHISTORY
        where INTIME between  TO_DATE('"""+ start_time +"""','YYYY-MM-DD HH24:MI:SS')
        and TO_DATE('"""+ end_time +"""','YYYY-MM-DD HH24:MI:SS')
         """
    
    temp_IN_data = pd.read_sql(sqlquery,conn)
    conn.close()
except IndexError as e:
    print(type(e), str(e),'SQL Link Error')




##後段即時門禁資料##

try:
    
    temp_INL2_data = pd.DataFrame()
    conn = cx_Oracle.connect('L6ACEL_AP','L6ACEL$AP','10.96.176.17/M10DOOR.CORPNET.AUO.COM')

 
    sqlquery ="""
        select distinct WORKID, INTIME, INDOOR, OUTTIME
        FROM DOORCTL.T_CRHISTORY
        where INTIME between  TO_DATE('"""+ start_time +"""','YYYY-MM-DD HH24:MI:SS')
        and TO_DATE('"""+ end_time +"""','YYYY-MM-DD HH24:MI:SS')
         """

    temp_INL2_data = pd.read_sql(sqlquery,conn)
    conn.close()
except IndexError as e:
    print(type(e), str(e),'SQL Link Error')




#歷史門禁資料##

try:
    temp_INHIS_data = pd.DataFrame()
    conn = cx_Oracle.connect('L6ACEL_AP','L6ACEL$AP','TCDOR001/TCDOORS.CORPNET.AUO.COM')
  
    sqlquery = """
        select distinct WORKID, INTIME, INDOOR, OUTTIME
        FROM DOORCTL.T_CRHISTORY
        where INTIME between  TO_DATE('"""+ start_time +"""','YYYY-MM-DD HH24:MI:SS')
        and TO_DATE('"""+ end_time +"""','YYYY-MM-DD HH24:MI:SS')
    """

    temp_INHIS_data = pd.read_sql(sqlquery,conn)
    conn.close()
except IndexError as e:
    print(type(e), str(e),'SQL Link Error')




# merge front and back door 

temp_ALL_data= temp_INHIS_data.append(temp_IN_data, ignore_index=True)
temp_ALL_data= temp_ALL_data.append(temp_INL2_data, ignore_index=True)
df_fab_record = temp_ALL_data.drop_duplicates(subset = "WORKID")
df_fab_record = df_fab_record.reset_index(drop= True)




df_fab_infected = df_fab_record[df_fab_record['WORKID'] == work_id].reset_index(drop=True)
location = []
for i in range(len(df_fab_infected)):
    location.append(df_fab_infected['INDOOR'].get(i))




# 匡列感染者時間範圍內，出現的人群

def connect_fab_db(index):

    try:
        conn = cx_Oracle.connect('L6ACEL_AP','L6ACEL$AP','TCDOR001/TCDOORS.CORPNET.AUO.COM')
        sql_catch = """
            select *
            from (select a.workid,a.name,a.adtdepartment FROM DOORCTL.T_ENTRANT a 
            where a.adtdepartment like 'ML6A%' AND a.COMPANY = 'AUO友達') DEP_LIST 
            RIGHT JOIN
            (select b.WORKID,b.INTIME,INDOOR,b.OUTTIME
            FROM DOORCTL.T_CRHISTORY b
            where (INTIME between  TO_DATE('"""+ str(appear_fabtime_list[index]) +"""','YYYY-MM-DD HH24:MI:SS') 
            and TO_DATE('"""+ str(range_of_fabtime[index]) +"""','YYYY-MM-DD HH24:MI:SS')) and INDOOR = 
            '""" + location[index] + """') INDOR ON DEP_LIST.WORKID = INDOR.WORKID
            """
        
        oracleCursor = conn.cursor()
        oracleCursor.execute(sql_catch)
        
        data = oracleCursor.fetchall()

        oracleCursor.close()
        conn.close()
    except IndexError as e:
        return
    
    return data




def output_fab_potential_people():
    
    # if didn't appear in the fab
    if len(df_fab_infected) == 0:
        print('Did not appear in the fab.')
        return
    
    fab_appear_time_index = df_fab_infected['INTIME'].index
    for i in fab_appear_time_index:
        appear_fabtime_list.append(df_fab_infected['INTIME'][i])

    # add time_range => new list of entry_time to filter people who entry after infected. 
    for item in appear_fabtime_list:
        range_of_fabtime.append(item + timedelta(seconds=time_range))
    
    fab_potential, fab_col = [], ['work_id' ,'name', 'area','work_id1', 'clock_in_time', 'postition', 'clock_out_time']
    for i in range(len(appear_fabtime_list)):
        fab_potential.append(connect_fab_db(i))

    fab_potential = list(filter(None, fab_potential))
    # flat list 
    flat_fab_list = sum(fab_potential, [])

    df_fab_potential = pd.DataFrame(flat_fab_list, columns=fab_col)
    df_fab_potential = df_fab_potential[df_fab_potential['work_id'] != work_id]
    del df_fab_potential['work_id1']
    df = df_fab_potential[['name', 'work_id', 'clock_in_time', 'clock_out_time', 'postition', 'area']]
    
    return df




re_col = ['name', 'work_id', 'clock_in_time', 'clock_out_time', 'postition', 'area']
re_fab_col = ['name', 'work_id', 'clock_in_time', 'clock_out_time', 'postition', 'area']

df_reformat_office = pd.DataFrame(columns = re_col)
df_reformat_fab = pd.DataFrame(columns = re_fab_col)


# ##交通車
# 05:000-10:00 and 17:00-22:00



bus_server = '10.96.48.148' #IP:port
bus_DBuser = 'ml6a01'
bus_password = '$$ml6a01$$'
bus_database = 'covid19_working_group'
port = '3306'

conn_bus = r'mysql+pymysql://'+bus_DBuser+':'+bus_password+'@'+bus_server+':'+port+'/'+bus_database #sql server帳號驗證
bus_engine = create_engine(conn_bus)

#開啟連線
with bus_engine.begin() as conn:
    sql = """select * from covid19_working_group.tc_bus_record WHERE clock_in_time BETWEEN 
    '"""+ start_time + """' And '"""+ end_time + """' ORDER BY clock_in_time;
    """

    result = conn.execute(text(sql))
    columns = result.keys()        
    data = result.fetchall()
    df_bus = pd.DataFrame(data, columns=columns)
    df_bus.drop('hid', axis=1, inplace=True)



df_bus_infected = df_bus[df_bus['work_id'] == work_id].reset_index(drop=True)
df_bus_infected['clock_out_time'] = ""
infected_bus_area = []
for i in range(len(df_bus_infected)):
    infected_bus_area.append(df_bus_infected['area'].get(i))
df_bus_infected


def connect_bus_db(index):
    # determine morning or afternoon bus
    morning_start = datetime.strptime(str(appear_bustime_list[index].date())+'05:00', '%Y-%m-%d%H:%M')
    morning_end =  datetime.strptime(str(appear_bustime_list[index].date())+'10:00', '%Y-%m-%d%H:%M')
    afternoon_start = datetime.strptime(str(appear_bustime_list[index].date())+'17:00', '%Y-%m-%d%H:%M')
    afternoon_end =  datetime.strptime(str(appear_bustime_list[index].date())+'22:00', '%Y-%m-%d%H:%M')
    
    with bus_engine.begin() as conn:
        if appear_bustime_list[index] > morning_start and appear_bustime_list[index] < morning_end:
            sql = """select * from covid19_working_group.tc_bus_record WHERE (clock_in_time BETWEEN 
            '"""+ str(morning_start) + """' And '"""+ str(morning_end) + """') and area = '"""  + infected_bus_area[index] + """';
            """
        elif appear_bustime_list[index] > afternoon_start and appear_bustime_list[index] < afternoon_end:
            sql = """select * from covid19_working_group.tc_bus_record WHERE (clock_in_time BETWEEN 
            '"""+ str(afternoon_start) + """' And '"""+ str(afternoon_end) + """') and area = '"""  + infected_bus_area[index] + """';
            """
            
        result = conn.execute(text(sql))
        #欄位名稱
        columns = result.keys()

        data = result.fetchall()
        return data, columns




def output_bus_potential_people():
    # if didn't appear in the office
    if len(df_bus_infected) == 0:
        print('Did not appear on the bus')
        return
    
    appear_time_index = df_bus_infected['clock_in_time'].index
    for i in appear_time_index:
        appear_bustime_list.append(df_bus_infected['clock_in_time'][i])

    
    potential, col = [], connect_bus_db(0)[1]
    
    for i in range(0, len(appear_bustime_list)):
        potential.append(connect_bus_db(i)[0])
    # flat list 
    flat_list = sum(potential, [])

    df_potential = pd.DataFrame(flat_list, columns=col)
    df_potential = df_potential[df_potential['work_id'] != work_id]
    df_potential['clock_out_time'] = ""
    
    new_index = ['name', 'work_id', 'clock_in_time', 'clock_out_time', 'postition', 'area']
    df = df_potential.reindex(new_index, axis="columns")
    return df.reset_index(drop=True)


# 宿舍(1,2: 大廳, 7,8: 停車場)
dormitory_server = '10.96.48.148' #IP:port
dormitory_DBuser = 'ml6a01'
dormitory_password = '$$ml6a01$$'
dormitory_database = 'covid19_working_group'
port = '3306'

conn_dormitory = r'mysql+pymysql://'+bus_DBuser+':'+bus_password+'@'+bus_server+':'+port+'/'+bus_database #sql server帳號驗證
dormitory_engine = create_engine(conn_bus)

#開啟連線
with dormitory_engine.begin() as conn:
    sql = """select * from covid19_working_group.tc_dormitory_record WHERE clock_in_time BETWEEN 
    '"""+ start_time + """' And '"""+ end_time + """' ORDER BY clock_in_time;
    """

    result = conn.execute(text(sql))
    columns = result.keys()        
    data = result.fetchall()
    df_dormitory = pd.DataFrame(data, columns=columns)
    df_dormitory.drop('hid', axis=1, inplace=True)  



df_dormitory['clock_out_time'] = ""
df_dormitory_infected = df_dormitory[df_dormitory['work_id'] == work_id].reset_index(drop=True)

infected_dormitory_area = []
for i in range(len(df_dormitory_infected)):
    infected_dormitory_area.append(df_dormitory_infected['postition'].get(i))

df_dormitory_infected

# 匡列宿舍
def connect_dor_db(index):
    with dormitory_engine.begin() as conn:
        if infected_dormitory_area[index] == 'TC_DR_IN_007' or infected_dormitory_area[index] == 'TC_DR_OUT_008':
            sql = """select * FROM covid19_working_group.tc_dormitory_record WHERE (clock_in_time BETWEEN 
            '"""+ str(appear_dortime_list[index]) + """' And '"""+ str(range_of_dortime[index]) + """')  
            AND (postition = 'TC_DR_IN_007' OR postition = 'TC_DR_OUT_008');
            """
        elif infected_dormitory_area[index] == 'TC_DR_IN_003' or infected_dormitory_area[index] == 'TC_DR_OUT_004':
            sql = """select * FROM covid19_working_group.tc_dormitory_record WHERE (clock_in_time BETWEEN 
            '"""+ str(appear_dortime_list[index]) + """' And '"""+ str(range_of_dortime[index]) + """')  
            AND (postition = 'TC_DR_IN_003' OR postition = 'TC_DR_OUT_004');
            """
        elif infected_dormitory_area[index] == 'TC_DR_IN_001' or infected_dormitory_area[index] == 'TC_DR_OUT_002':
            sql = """select * FROM covid19_working_group.tc_dormitory_record WHERE (clock_in_time BETWEEN 
            '"""+ str(appear_dortime_list[index]) + """' And '"""+ str(range_of_dortime[index]) + """')  
            AND (postition = 'TC_DR_IN_001' OR postition = 'TC_DR_OUT_002');
            """
        else:
            return
            
        result = conn.execute(text(sql))
        columns = result.keys()
        data = result.fetchall()
        
        return data, columns

def output_dor_potential_people():
    # if didn't appear in the dormitory
    if len(df_dormitory_infected) == 0:
        print('Did not appear in the dormitory.')
        return
    
    appear_time_index = df_dormitory_infected['clock_in_time'].index
    for i in appear_time_index:
        appear_dortime_list.append(df_dormitory_infected['clock_in_time'][i])

    # add time_range => new list of entry_time to filter people who entry after infected. 
    for item in appear_dortime_list:
        range_of_dortime.append(item + timedelta(seconds=time_range))
    
    potential, col = [], connect_dor_db(0)[1]
    
    for i in range(0, len(appear_dortime_list)):
        potential.append(connect_dor_db(i)[0])
    # flat list 
    flat_list = sum(potential, [])

    df_potential = pd.DataFrame(flat_list, columns=col)
    df_potential = df_potential[df_potential['work_id'] != work_id]
    df_potential['clock_out_time'] = ""
    
    df_potential.drop('hid', axis=1, inplace=True)  
    return df_potential.reset_index(drop=True)
 
# 三叉門
tridoor_server = '10.96.48.148' #IP:port
tridoor_DBuser = 'ml6a01'
tridoor_password = '$$ml6a01$$'
tridoor_database = 'covid19_working_group'
port = '3306'

conn_tridoor = r'mysql+pymysql://'+tridoor_DBuser+':'+tridoor_password+'@'+tridoor_server+':'+port+'/'+tridoor_database #sql server帳號驗證
tridoor_engine = create_engine(conn_tridoor)

#開啟連線
with tridoor_engine.begin() as conn:
    sql = """select * from covid19_working_group.trigeminal_door_record WHERE clock_in_time BETWEEN 
    '"""+ start_time + """' And '"""+ end_time + """' ORDER BY clock_in_time;
    """

    result = conn.execute(text(sql))
    columns = result.keys()        
    data = result.fetchall()
    df_tridoor = pd.DataFrame(data, columns=columns)

df_tridoor_infected = df_tridoor[df_tridoor['work_id'] == work_id].reset_index(drop=True)

# 匡列三叉門
def connect_tridoor_db(index):
    # determine morning or afternoon bus
    
    with tridoor_engine.begin() as conn:
        sql = """select * from covid19_working_group.trigeminal_door_record WHERE (clock_in_time BETWEEN 
        '"""+ str(appear_tridoortime_list[index]) + """' And '"""+ str(range_of_tridoortime[index]) + """');
        """
            
        result = conn.execute(text(sql))
        #欄位名稱
        columns = result.keys()

        data = result.fetchall()
        return data, columns

def output_tridoor_potential_people():
    # if didn't appear in the 三叉門
    if len(df_tridoor_infected) == 0:
        print('Did not appear in the Tridoor.')
        return
    
    appear_time_index = df_tridoor_infected['clock_in_time'].index
    for i in appear_time_index:
        appear_tridoortime_list.append(df_tridoor_infected['clock_in_time'][i])
        
    # add time_range => new list of entry_time to filter people who entry after infected. 
    for item in appear_tridoortime_list:
        range_of_tridoortime.append(item + timedelta(seconds=time_range))
    
    potential, col = [], connect_tridoor_db(0)[1]
    
    for i in range(0, len(appear_tridoortime_list)):
        potential.append(connect_tridoor_db(i)[0])
    # flat list 
    flat_list = sum(potential, [])

    df_potential = pd.DataFrame(flat_list, columns=col)
    df_potential = df_potential[df_potential['work_id'] != work_id]
    return df_potential.reset_index(drop=True)



# 進行timstamp to json 轉換
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj)

# 整合並輸出json
if __name__ == '__main__': 
            
    office = output_potential_people() #匡列辦公室
    fab = output_fab_potential_people() #匡列Fab
    shuttle_bus = output_bus_potential_people() # 匡列交通車
    dorm = output_dor_potential_people()
    tridoor = output_tridoor_potential_people() # 匡列三叉門
    
    dit = {"footprint": [], "potential": []}
    
    if len(df_bus_infected) == 0 and len(df_office_infected) == 0 and len(df_fab_infected) == 0 and len(df_dormitory_infected) == 0 and len(df_tridoor_infected) == 0:
        dic_no_appear = {"footprint": [], "potential": []}
        
        with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dic_no_appear,ensure_ascii=False ,cls=DateEncoder))  
                
    elif len(df_office_infected) == 0 and len(df_fab_infected) == 0 and len(df_bus_infected) != 0:
        df_merge_infected = df_bus_infected
        df_merge_potential = shuttle_bus

        # 沒有匡列到人
        if len(df_merge_potential) == 0:
            df_merge_infected = df_merge_infected.to_dict(orient="records")
            dit = {"footprint" : df_merge_infected, "potential": []}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False ,cls=DateEncoder))
                
         # 有匡列到人
        df_merge_infected = df_merge_infected.to_dict(orient="records")
        df_merge_potential = df_merge_potential.to_dict(orient="records")
        dit = {"footprint" : df_merge_infected, "potential": df_merge_potential}

        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(json.dumps(dit,ensure_ascii=False, cls=DateEncoder))
    elif len(df_office_infected) == 0 and len(df_dormitory_infected) == 0 and len(df_fab_infected) != 0: # 出現在fab和交通車

        df_reformat_fab['name'] = str(df_bus_infected['name'][0])
        df_reformat_fab['work_id'] = df_fab_infected['WORKID']
        df_reformat_fab['clock_in_time'] = df_fab_infected['INTIME']
        df_reformat_fab['clock_out_time'] = df_fab_infected['OUTTIME']
        df_reformat_fab['postition'] = df_fab_infected['INDOOR']
        df_reformat_fab['area'] = ""
        df_reformat_fab['name'] = str(df_bus_infected['name'][0])
        
        # 感染者出現在Fab + bus:
        df_merge_infected = df_bus_infected.append(df_reformat_fab).reset_index(drop=True)
        
         # 匡列Fab + bus:
        df_merge_potential = shuttle_bus.append(fab).reset_index(drop=True)
        
         # 有匡列到人
        if len(df_merge_infected) != 0 and len(df_merge_potential) != 0:
            for i in range(len(df_merge_infected['clock_out_time'])):
                df_merge_infected['clock_in_time'][i] =  df_merge_infected['clock_in_time'][i].strftime("%Y-%m-%d %H:%M:%S")
                if df_merge_infected['clock_out_time'][i] != "":
                    df_merge_infected['clock_out_time'][i] = df_merge_infected['clock_out_time'][i].strftime("%Y-%m-%d %H:%M:%S")

            df_merge_infected = df_merge_infected.to_dict(orient="records")
            df_merge_potential = df_merge_potential.to_dict(orient="records")
            dit = {"footprint" : df_merge_infected, "potential": df_merge_potential}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False, cls=DateEncoder))

        # 沒有匡列到人
        if len(df_merge_potential) == 0:
            for i in range(len(df_merge_infected['clock_out_time'])):
                df_merge_infected['clock_in_time'][i] =  df_merge_infected['clock_in_time'][i].strftime("%Y-%m-%d %H:%M:%S")
                if df_merge_infected['clock_out_time'][i] != "":
                    df_merge_infected['clock_out_time'][i] = df_merge_infected['clock_out_time'][i].strftime("%Y-%m-%d %H:%M:%S")

            df_merge_infected = df_merge_infected.to_dict(orient="records")

            dit = {"footprint" : df_merge_infected, "potential": []}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False ,cls=DateEncoder))
                
    elif len(df_bus_infected) == 0 and len(df_office_infected) == 0 and len(df_fab_infected) == 0 and len(df_dormitory_infected) == 0:
        df_merge_infected = df_tridoor_infected
        df_merge_potential = tridoor

        # 沒有匡列到人
        if len(df_merge_potential) == 0:
            df_merge_infected = df_merge_infected.to_dict(orient="records")
            dit = {"footprint" : df_merge_infected, "potential": []}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False ,cls=DateEncoder))
        else:      
            # 有匡列到人
            df_merge_infected = df_merge_infected.to_dict(orient="records")
            df_merge_potential = df_merge_potential.to_dict(orient="records")
            dit = {"footprint" : df_merge_infected, "potential": df_merge_potential}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False, cls=DateEncoder))
    
    else:
        df_reformat_office['name'] = df_office_infected['NAME']
        df_reformat_office['work_id'] = df_office_infected['WORKERID']
        df_reformat_office['clock_in_time'] = df_office_infected['entry_time']
        df_reformat_office['clock_out_time'] = ""
        df_reformat_office['postition'] = df_office_infected['location_number']
        df_reformat_office['area'] = df_office_infected['DEPARTMENT']

        df_reformat_fab['name'] = str(df_office_infected['NAME'][0])
        df_reformat_fab['work_id'] = df_fab_infected['WORKID']
        df_reformat_fab['clock_in_time'] = df_fab_infected['INTIME']
        df_reformat_fab['clock_out_time'] = df_fab_infected['OUTTIME']
        df_reformat_fab['postition'] = df_fab_infected['INDOOR']
        df_reformat_fab['area'] = ""
        df_reformat_fab['name'] = str(df_office_infected['NAME'][0])

        # append infected person together:
        df_merge_infected = df_reformat_office.append(df_reformat_fab).reset_index(drop=True)
        df_merge_infected = df_merge_infected.append(df_bus_infected).reset_index(drop=True)
        df_merge_infected = df_merge_infected.append(df_dormitory_infected).reset_index(drop=True)
        df_merge_infected = df_merge_infected.append(df_tridoor_infected).reset_index(drop=True)  
        df_merge_infected = df_merge_infected[["name", "work_id", "clock_in_time", 'clock_out_time','area', 'postition']]
        
        # 匡列辦公室 + Fab + bus:
        df_merge_potential = office.append(fab).reset_index(drop=True)
        df_merge_potential = df_merge_potential.append(shuttle_bus).reset_index(drop=True)
        df_merge_potential = df_merge_potential.append(dorm).reset_index(drop=True)  
        df_merge_potential = df_merge_potential.append(tridoor).reset_index(drop=True)    
        
        # 有匡列到人
        if len(df_merge_infected) != 0 and len(df_merge_potential) != 0:
            for i in range(len(df_merge_infected['clock_out_time'])):
                df_merge_infected['clock_in_time'][i] =  df_merge_infected['clock_in_time'][i].strftime("%Y-%m-%d %H:%M:%S")
                if df_merge_infected['clock_out_time'][i] != "":
                    df_merge_infected['clock_out_time'][i] = df_merge_infected['clock_out_time'][i].strftime("%Y-%m-%d %H:%M:%S")

            df_merge_infected = df_merge_infected.to_dict(orient="records")
            df_merge_potential = df_merge_potential.to_dict(orient="records")
            dit = {"footprint" : df_merge_infected, "potential": df_merge_potential}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False, cls=DateEncoder))

        # 沒有匡列到人
        if len(df_merge_potential) == 0:
            for i in range(len(df_merge_infected['clock_out_time'])):
                df_merge_infected['clock_in_time'][i] =  df_merge_infected['clock_in_time'][i].strftime("%Y-%m-%d %H:%M:%S")
                if df_merge_infected['clock_out_time'][i] != "":
                    df_merge_infected['clock_out_time'][i] = df_merge_infected['clock_out_time'][i].strftime("%Y-%m-%d %H:%M:%S")

            df_merge_infected = df_merge_infected.to_dict(orient="records")

            dit = {"footprint" : df_merge_infected, "potential": []}

            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(json.dumps(dit,ensure_ascii=False ,cls=DateEncoder))
  
