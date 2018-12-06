# CS506 Federal Prosecutor Project
# Justin, Ben, Hao
#
# Preliminary code to parse through the .txt files and extract certain fields.
# Primarily using this file to explore the various data.
import sys
import re
from itertools import groupby

DIR = "data/"
n='INTEGER'
def v(x):
    return 'VARCHAR(' + str(x) + ')'
d = 'DATE'

def get_district_list():
    districts = ["AK", "ALM", "ALN", "ALS", "ARE", \
                 "ARW", "AZ", "CAC", "CAE", "CAN", \
                 "CAS", "CO", "CT", "DC", "DE", \
                 "FLM", "FLN", "FLS", "GAM", "GAN", \
                 "GAS", "GU", "HI", "IAN", "IAS", \
                 "ID", "ILC", "ILN", "ILS", "INN", \
                 "INS", "KS", "KYE", "KYW", "LAE", \
                 "LAM", "LAW", "MA", "MD", "ME", \
                 "MIE", "MIW", "MN", "MOE", "MOW", \
                 "MSN", "MSS", "MT", "NCE", "NCM", \
                 "NCW", "ND", "NE", "NH", "NJ", \
                 "NM", "NV", "NYE", "NYN", "NYS", \
                 "NYW", "OHN", "OHS", "OKE", "OKN", \
                 "OKW", "OR", "PAE", "PAM", "PAW", \
                 "PR", "RI", "SC", "SD", "TNE", \
                 "TNM", "TNW", "TXE", "TXN", "TXS", \
                 "TXW", "UT", "VAE", "VAW", "VI", \
                 "VT", "WAE", "WAW", "WIE", "WIW", \
                 "WVN", "WVS", "WY"]

    return districts

# Parse DISK01
def gs_also_known():
    global DIR
    filename = DIR + 'gs_also_known.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASE_ID', 'PART_ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CASE_ID,DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PART_ID, CASE_ID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)'
            },
            'types': {
                'DISTRICT':'VARCHAR(10)',
                'CASE_ID':'VARCHAR(10)',
                'PART_ID':'INTEGER',
                'ID':'INTEGER',
                'LAST_NAME':'VARCHAR(60)',
                'FIRST_NAME':'VARCHAR(60)',
                'LAST_SOUNDS':'VARCHAR(4)',
                'FIRST_SOUNDS':'VARCHAR(4)',
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASE_ID',
                'PART_ID',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASE_ID'] = line[10:20].rstrip().lstrip()
            row['PART_ID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['LAST_NAME'] = line[40:100].rstrip().lstrip()
            row['FIRST_NAME'] = line[100:130].rstrip().lstrip()
            row['LAST_SOUNDS'] = line[130:134].rstrip().lstrip()
            row['FIRST_SOUNDS'] = line[134:138].rstrip().lstrip()
            row['CREATE_DATE'] = line[138:149].rstrip().lstrip()
            row['CREATE_USER'] = line[149:179].rstrip().lstrip()
            row['UPDATE_DATE'] = line[179:190].rstrip().lstrip()
            row['UPDATE_USER'] = line[190:220].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_archive_case():
    global DIR
    filename = DIR + 'gs_archive_case.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CLASS': 'GS_CASE_CLASS(CODE)',
                'US_ROLE': 'GS_US_ROLE(CODE)',
                'PROG_CAT': 'GS_PROG_CAT(CODE)',
                'CAUSE_ACT': 'GS_CAUSE_ACT(CODE)',
                'COURT': 'GS_COURT(CODE)',
                'DISPOSITION': 'GS_DISP_TYPE(CODE)',
                'DISP_REASON': 'GS_DISP_REAS_TYPE(CODE)',
                'INST_TYPE': 'GS_INST_TYPE(CODE)',
                'AGENCY': 'GS_AGENCY(CODE)'
            },
            'types': {
                'DISTRICT': 'VARCHAR(10)',
                'ID':'VARCHAR(10)',
                'CLASS':'VARCHAR(1)',
                'NAME': 'VARCHAR(50)',
                'RECVD_DATE':'DATE',
                'US_ROLE': 'VARCHAR(2)',
                'LEAD_CHARGE': 'VARCHAR(25)',
                'PROG_CAT': 'VARCHAR(3)',
                'CAUSE_ACT': 'VARCHAR(4)',
                'BRANCH':'VARCHAR(3)',
                'COMMENTS':'VARCHAR(60)',
                'COURT':'VARCHAR(2)',
                'LOCATION':'VARCHAR(2)',
                'COURT_NUMBER':'VARCHAR(25)',
                'FILING_DATE': 'DATE',
                'SERVICE_DATE':'DATE',
                'DISPOSITION': 'VARCHAR(2)',
                'DISP_REASON':'VARCHAR(4)',
                'DISP_DATE':'DATE',
                'INST_TYPE':'VARCHAR(2)',
                'INST_FILE_DATE':'DATE',
                'AUSA_LAST_NAME':'VARCHAR(30)',
                'AUSA_FIRST_NAME':'VARCHAR(30)',
                'AGENCY':'VARCHAR(4)',
                'APPEALS_FILED':'INTEGER',
                'STORE_NUM':'VARCHAR(20)',
                'DEST_DATE':'DATE',
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null':[
                'DISTRICT',
                'ID',
                'CLASS',
                'RECVD_DATE',
                'DISPOSITION',
                'DISP_DATE',
                'AGENCY'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['ID'] = line[10:20].rstrip().lstrip()
            row['CLASS'] = line[20:21].rstrip().lstrip()
            row['NAME'] = line[21:71].rstrip().lstrip()
            row['RECVD_DATE'] = line[71:82].rstrip().lstrip()
            row['US_ROLE'] = line[82:84].rstrip().lstrip()
            row['LEAD_CHARGE'] = line[84:109].rstrip().lstrip()
            row['PROG_CAT'] = line[109:112].rstrip().lstrip()
            row['CAUSE_ACT'] = line[112:116].rstrip().lstrip()
            row['BRANCH'] = line[116:119].rstrip().lstrip()
            row['COMMENTS'] = line[119:179].rstrip().lstrip()
            row['COURT'] = line[179:181].rstrip().lstrip()
            row['LOCATION'] = line[181:183].rstrip().lstrip()
            row['COURT_NUMBER'] = line[183:208].rstrip().lstrip()
            row['FILING_DATE'] = line[208:219].rstrip().lstrip()
            row['SERVICE_DATE'] = line[219:230].rstrip().lstrip()
            row['DISPOSITION'] = line[230:232].rstrip().lstrip()
            row['DISP_REASON'] = line[232:236].rstrip().lstrip()
            row['DISP_DATE'] = line[236:247].rstrip().lstrip()
            row['INST_TYPE'] = line[247:249].rstrip().lstrip()
            row['INST_FILE_DATE'] = line[249:260].rstrip().lstrip()
            row['AUSA_LAST_NAME'] = line[260:290].rstrip().lstrip()
            row['AUSA_FIRST_NAME'] = line[290:320].rstrip().lstrip()
            row['AGENCY'] = line[320:324].rstrip().lstrip()
            row['APPEALS_FILED'] = line[324:335].rstrip().lstrip()
            row['STORE_NUM'] = line[334:355].rstrip().lstrip()
            row['DEST_DATE'] = line[355:366].rstrip().lstrip()
            row['CREATE_DATE'] = line[366:377].rstrip().lstrip()
            row['CREATE_USER'] = line[377:407].rstrip().lstrip()
            row['UPDATE_DATE'] = line[407:418].rstrip().lstrip()
            row['UDPATE_USER'] = line[418:448].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_archive_part():
    global DIR
    disk = "DISK01"
    filename = DIR + 'gs_archive_part.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT':'GS_CASE(ID, DISTRICT)',
                'DISTRICT':'GS_DISTRICT(DISTRICT)',
                'ROLE': 'GS_ROLE(CODE)',
                'DISPOSITION': 'GS_DISP_TYPE(CODE)',
                'DISP_REASON': 'GS_DISP_REAS_TYPE(CODE)'
            },
            'types': {
                'DISTRICT':'VARCHAR(10)',
                'CASEID': v(10),
                'ID': v(10),
                'LAST_NAME': v(60),
                'FIRST_NAME': v(30),
                'LAST_SOUNDS': v(4),
                'FIRST_SOUNDS': v(4),
                'ROLE': v(2),
                'DISPOSITION': v(2),
                'DISP_REASON': v(4),
                'DISP_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'LAST_NAME',
                'LAST_SOUNDS',
                'ROLE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['LAST_NAME'] = line[30:90].rstrip().lstrip()
            row['FIRST_NAME'] = line[90:120].rstrip().lstrip()
            row['LAST_SOUNDS'] = line[120:124].rstrip().lstrip()
            row['FIRST_SOUNDS'] = line[124:128].rstrip().lstrip()
            row['ROLE'] = line[128:130].rstrip().lstrip()
            row['DISPOSITION'] = line[130:132].rstrip().lstrip()
            row['DISP_REASON'] = line[132:136].rstrip().lstrip()
            row['DISP_DATE'] = line[136:147].rstrip().lstrip()
            row['CREATE_DATE'] = line[147:158].rstrip().lstrip()
            row['CREATE_USER'] = line[158:188].rstrip().lstrip()
            row['UPDATE_DATE'] = line[188:199].rstrip().lstrip()
            row['UPDATE_USER'] = line[199:229].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case():
    global DIR
    filename = DIR + 'gs_case.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CLASS': 'GS_CASE_CLASS(CODE)',
                'SECURITY, DISTRICT': 'GS_SECURITY(CODE, DISTRICT)',
                'PRIORITY': 'GS_PRIORITY(CODE)',
                'TYPE, DISTRICT': 'GS_CASE_TYPE(CODE, DISTRICT)',
                'US_ROLE': 'GS_US_ROLE(CODE)',
                'LIT_RESP': 'GS_LIT_RESP(CODE)',
                'LIT_TRACK, DISTRICT': 'GS_LIT_TRACK(CODE, DISTRICT)',
                'WEIGHT, DISTRICT': 'GS_CASE_WEIGHT(CODE, DISTRICT)',
                'BRANCH, DISTRICT': 'GS_REGION(BRANCH, DISTRICT)',
                'UNIT, DISTRICT': 'GS_UNIT(CODE, DISTRICT)',
                'TRIBE': 'GS_TRIBE(CODE)',
                'RESERVATION, DISTRICT': 'GS_RESERVATION(CODE, DISTRICT)',
                'SPEC_PROJ': 'GS_SPEC_PROJ(CODE)',
                'VIC_WIT': 'GS_VICTIM_WIT(CODE)',
                'ADR_MODE': 'GS_ADR_MODE(CODE)',
                'COLLECT_IND': 'GS_COLLECT_IND(CODE)',
                #'LEAD_CHARGE': '',
                'CIVIL_POTEN': 'GS_CIVIL_POTEN(CODE)',
                'STATUS': 'GS_CASE_STATUS(CODE)'
            },
            'types': {
                'DISTRICT': v(3),
                'ID': v(10),
                'CLASS': v(1),
                'NAME': v(50),
                'RECVD_DATE': d,
                'SECURITY': v(1),
                'PRIORITY': v(1),
                'TYPE': v(4),
                'US_ROLE': v(2),
                'LIT_RESP': v(2),
                'LIT_TRACK': v(1),
                'WEIGHT': v(2),
                'BRANCH': v(3),
                'GRAND_JURY_NUM': v(15),
                'UNIT': v(4),
                'DCMNS_NUMBER': v(11),
                'TRIBE': v(4),
                'RESERVATION': v(4),
                'SPEC_PROJ': v(2),
                'VIC_WIT': v(1),
                'ADR_MODE': v(2),
                'COLLECT_IND': v(1),
                'OFFENSE_FROM': d,
                'OFFENSE_TO': d,
                'LEAD_CHARGE': v(25),
                'PHYSICAL_LOC': v(20),
                'STORE_NUM': v(20),
                'CIVIL_POTEN': v(1),
                'SYS_INIT_DATE': d,
                'ACCESS_DATE': d,
                'STATUS': v(1),
                'CLOSE_DATE': d,
                'DEST_DATE': d,
                'PERMANENT': v(1),
                'CASE_RESTRICTED': v(1),
                'CRIMINAL_POTEN': v(1),
                'TOT_VICTIMS': n,
                'RELATED_FLU_FLAG': v(1),
                'QUI_TAM': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'CLASS',
                'RECVD_DATE',
                'LIT_RESP',
                'BRANCH',
                'SYS_INIT_DATE',
                'ACCESS_DATE',
                'STATUS'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3].rstrip().lstrip()
            row['ID'] = line[3:13].rstrip().lstrip()
            row['CLASS'] = line[13:14].rstrip().lstrip()
            row['NAME'] = line[14:64].rstrip().lstrip()
            row['RECVD_DATE'] = line[64:75].rstrip().lstrip() # convert to datetime
            row['SECURITY'] = line[75:76].rstrip().lstrip()
            row['PRIORITY'] = line[76:77].rstrip().lstrip()
            row['TYPE'] = line[77:81].rstrip().lstrip()
            row['US_ROLE'] = line[81:83].rstrip().lstrip()
            row['LIT_RESP'] = line[83:85].rstrip().lstrip()
            row['LIT_TRACK'] = line[85:86].rstrip().lstrip()
            row['WEIGHT'] = line[86:88].rstrip().lstrip()
            row['BRANCH'] = line[88:91].rstrip().lstrip()
            row['GRAND_JURY_NUM'] = line[91:106].rstrip().lstrip()
            row['UNIT'] = line[106:110].rstrip().lstrip()
            row['DCMNS_NUMBER'] = line[110:121].rstrip().lstrip()
            row['TRIBE'] = line[121:125].rstrip().lstrip()
            row['RESERVATION'] = line[125:129].rstrip().lstrip()
            row['SPEC_PROJ'] = line[129:131].rstrip().lstrip()
            row['VIC_WIT'] = line[131:132].rstrip().lstrip()
            row['ADR_MODE'] = line[132:134].rstrip().lstrip()
            row['COLLECT_IND'] = line[134:135].rstrip().lstrip()
            row['OFFENSE_FROM'] = line[135:146].rstrip().lstrip()
            row['OFFENSE_TO'] = line[146:157].rstrip().lstrip()
            row['LEAD_CHARGE'] = line[157:182].rstrip().lstrip()
            row['PHYSICAL_LOC'] = line[182:202].rstrip().lstrip()
            row['STORE_NUM'] = line[202:222].rstrip().lstrip()
            row['CIVIL_POTEN'] = line[222:223].rstrip().lstrip()
            row['SYS_INIT_DATE'] = line[223:234].rstrip().lstrip()
            row['ACCESS_DATE'] = line[234:245].rstrip().lstrip()
            row['STATUS'] = line[245:246].rstrip().lstrip()
            row['CLOSE_DATE'] = line[246:257].rstrip().lstrip()
            row['DEST_DATE'] = line[257:268].rstrip().lstrip()
            row['PERMANENT'] = line[268:269].rstrip().lstrip()
            row['CASE_RESTRICTED'] = line[269:270].rstrip().lstrip()
            row['CRIMINAL_POTEN'] = line[270:271].rstrip().lstrip()
            row['TOT_VICTIMS'] = line[271:282].rstrip().lstrip()
            row['RELATED_FLU_FLAG'] = line[282:283].rstrip().lstrip()
            row['QUI_TAM'] = line[283:284].rstrip().lstrip()
            row['CREATE_DATE'] = line[284:295].rstrip().lstrip()
            row['CREATE_USER'] = line[295:235].rstrip().lstrip()
            row['UPDATE_DATE'] = line[325:336].rstrip().lstrip()
            row['UPDATE_USER'] = line[336:337].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_cause_act():
    global DIR
    filename = DIR + 'gs_case_cause_act.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CAUSE_ACT', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CAUSE_ACT': 'GS_CAUSE_ACT(CODE)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CAUSE_ACT': v(4),
                'ID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CAUSE_ACT',
                'ID'
            ]

    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CAUSE_ACT'] = line[20:24].rstrip().lstrip()
            row['ID'] = line[24:34].rstrip().lstrip()
            row['CREATE_DATE'] = line[34:45].rstrip().lstrip()
            row['CREATE_USER'] = line[45:75].rstrip().lstrip()
            row['UPDATE_DATE'] = line[75:86].rstrip().lstrip()
            row['UPDATE_USER'] = line[86:116].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_doj_div():
    global DIR
    filename = DIR + 'gs_case_doj_div.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'DOJ_DIV': 'GS_DOJ_DIVISION(CODE)',
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'DOJ_DIV': v(4),
                'DOJ_NUMBER': v(25),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'DOJ_DIV'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['DOJ_DIV'] = line[30:34].rstrip().lstrip()
            row['DOJ_NUMBER'] = line[34:59].rstrip().lstrip()
            row['CREATE_DATE'] = line[59:70].rstrip().lstrip()
            row['CREATE_USER'] = line[70:100].rstrip().lstrip()
            row['UPDATE_DATE'] = line[100:111].rstrip().lstrip()
            row['UPDATE_USER'] = line[11:141].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_dom_terr_ind():
    global DIR
    filename = DIR + 'gs_case_dom_terr_ind.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'DOM_TERR_IND': 'GS_DOM_TERR_IND(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'ID': v(10),
                'CASEID': n,
                'DOM_TERR_IND': v(2),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'CASEID',
                'DOM_TERR_IND'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['ID'] = line[10:20].rstrip().lstrip()
            row['CASEID'] = line[20:30].rstrip().lstrip()
            row['DOM_TERR_IND'] = line[30:32].rstrip().lstrip()
            row['CREATE_DATE'] = line[32:43].rstrip().lstrip()
            row['CREATE_USER'] = line[43:73].rstrip().lstrip()
            row['UPDATE_DATE'] = line[73:84].rstrip().lstrip()
            row['UPDATE_USER'] = line[84:114].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_prog_cat():
    global DIR
    filename = DIR + 'gs_case_prog_cat.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PROG_CAT', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PROG_CAT': 'GS_PROG_CAT(CODE)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PROG_CAT': v(3),
                'ID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PROG_CAT',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PROG_CAT'] = line[20:23].rstrip().lstrip()
            row['ID'] = line[23:33].rstrip().lstrip()
            row['CREATE_DATE'] = line[33:44].rstrip().lstrip()
            row['CREATE_USER'] = line[44:74].rstrip().lstrip()
            row['UPDATE_DATE'] = line[74:85].rstrip().lstrip()
            row['UPDATE_USER'] = line[85:115].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# Parse DISK02
def gs_case_special_proj():
    global DIR
    filename = DIR + 'gs_case_special_proj.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID,DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'ID': n,
                'CASEID': v(1),
                'SPECIAL_PROJ': v(2),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'CASEID',
                'SPECIAL_PROJ'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['ID'] = line[10:20].rstrip().lstrip()
            row['CASEID'] = line[20:30].rstrip().lstrip()
            row['SPECIAL_PROJ'] = line[30:32].rstrip().lstrip()
            row['CREATE_DATE'] = line[32:43].rstrip().lstrip()
            row['CREATE_USER'] = line[43:73].rstrip().lstrip()
            row['UPDATE_DATE'] = line[73:84].rstrip().lstrip()
            row['UPDATE_USER'] = line[84:114].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_evidence():
    global DIR
    filename = DIR + 'gs_evidence.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID,DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'LOCATION, DISTRICT': 'GS_EVID_LOCATION(CODE, DISTRICT)',
                'TYPE, DISTRICT': 'GS_EVID_TYPE(CODE, DISTRICT)',
                'DISPOSITION, DISTRICT': 'GS_EVID_DISP(CODE, DISTRICT)',

            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'LOCATION': v(4),
                'TYPE': v(2),
                'DISPOSITION': v(1),
                'STORE_DATE': d,
                'DISP_DATE': d,
                'DC_EXHIBIT_NUM': v(25),
                'GJ_EXHIBIT_NUM': v(25),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'LOCATION',
                'TYPE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['LOCATION'] = line[30:34].rstrip().lstrip()
            row['TYPE'] = line[34:36].rstrip().lstrip()
            row['DISPOSITION'] = line[36:37].rstrip().lstrip()
            row['STORE_DATE'] = line[37:48].rstrip().lstrip()
            row['DISP_DATE'] = line[48:59].rstrip().lstrip()
            row['DC_EXHIBIT_NUM'] = line[59:84].rstrip().lstrip()
            row['GJ_EXHIBIT_NUM'] = line[84:109].rstrip().lstrip()
            row['CREATE_DATE'] = line[109:120].rstrip().lstrip()
            row['CREATE_USER'] = line[120:150].rstrip().lstrip()
            row['UPDATE_DATE'] = line[150:161].rstrip().lstrip()
            row['UPDATE_USER'] = line[161:191].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_expert_case():
    global DIR
    filename = DIR + 'gs_expert_case.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'EXP_SIDE': 'GS_EXPERT_SIDE(CODE)',
                'EXPERTID, DISTRICT': 'GS_EXPERT(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'EXP_SIDE': v(1),
                'EXPERTID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'EXP_SIDE',
                'EXPERTID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['EXP_SIDE'] = line[30:31].rstrip().lstrip()
            row['EXPERTID'] = line[31:41].rstrip().lstrip()
            row['CREATE_DATE'] = line[41:52].rstrip().lstrip()
            row['CREATE_USER'] = line[52:82].rstrip().lstrip()
            row['UPDATE_DATE'] = line[82:93].rstrip().lstrip()
            row['UPDATE_USER'] = line[93:123].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_inst_charge():
    global DIR
    filename = DIR + 'gs_inst_charge.txt'
    data = []
    sql = {
            'primary': ['CASEID', 'CRTHISID', 'INSTID', 'CHARGE', 'CATEGORY', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'INSTID, CASEID, CRTHISID, DISTRICT': 'GS_INSTRUMENT(ID, CASEID, CRTHISID, DISTRICT)',
                'CHARGE': 'GS_CHARGE_TYPE(CODE)',
                'CATEGORY': 'GS_CHARGE_CAT(CODE)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'PENT_PROV': 'GS_PENALTY_PROVISION(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'INSTID': n,
                'CHARGE': v(25),
                'CATEGORY': v(1),
                'PENT_PROV': v(25),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)',
                'ID': n
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'INSTID',
                'CHARGE',
                'CATEGORY',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CRTHISID'] = line[20:30].rstrip().lstrip()
            row['INSTID'] = line[30:40].rstrip().lstrip()
            row['CHARGE'] = line[40:65].rstrip().lstrip()
            row['CATEGORY'] = line[65:66].rstrip().lstrip()
            row['PENT_PROV'] = line[66:91].rstrip().lstrip()
            row['CREATE_DATE'] = line[91:102].rstrip().lstrip()
            row['CREATE_USER'] = line[102:132].rstrip().lstrip()
            row['UPDATE_DATE'] = line[132:143].rstrip().lstrip()
            row['UPDATE_USER'] = line[143:173].rstrip().lstrip()
            row['ID'] = line[173:183].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_part_victim():
    global DIR
    filename = DIR + 'gs_part_victim.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'VICTIM_TYPE': 'GS_VICTIM_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'VICTIM_TYPE': v(1),
                'PROSECUTION': v(1),
                'VICTIM_TIMES': n,
                'THREATS': v(1),
                'ELDERLY': v(1),
                'VICTIM_IDENTIFIER': v(25),
                'STATE_COMP_RECVD': 'FLOAT',
                'SERVICES_REQUESTED': v(1),
                'VIOLENT_CRIME': v(1),
                'DISABILITY': v(1),
                'NOTIFICAT_REQSTD': v(1),
                'NOTIFICAT_RECVD': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['VICTIM_TYPE'] = line[40:41].rstrip().lstrip()
            row['PROSECUTION'] = line[41:42].rstrip().lstrip()
            row['VICTIM_TIMES'] = line[43:53].rstrip().lstrip()
            row['THREATS'] = line[53:54].rstrip().lstrip()
            row['ELDERLY'] = line[54:55].rstrip().lstrip()
            row['VICTIM_IDENTIFIER'] = line[55:80].rstrip().lstrip()
            row['STATE_COMP_RECVD'] = line[80:94].rstrip().lstrip()
            row['SERVICES_REQUESTED'] = line[94:95].rstrip().lstrip()
            row['VIOLENT_CRIME'] = line[95:96].rstrip().lstrip()
            row['DISABILITY'] = line[96:97].rstrip().lstrip()
            row['NOTIFICAT_REQSTD'] = line[97:98].rstrip().lstrip()
            row['NOTIFICAT_RECVD'] = line[98:99].rstrip().lstrip()
            row['CREATE_DATE'] = line[99:110].rstrip().lstrip()
            row['CREATE_USER'] = line[110:140].rstrip().lstrip()
            row['UPDATE_DATE'] = line[140:151].rstrip().lstrip()
            row['UPDATE_USER'] = line[151:181].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relate_case():
    global DIR
    filename = DIR + 'gs_relate_case.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID1', 'CASEID2', 'DISTRICT'],
            'foreign':{
                'CASEID1, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CASEID2, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID1': v(10),
                'CASEID2': v(10),
                'CRTHISID1': n,
                'CRTHISID2': n,
                'REASON': v(2),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)',
                'ID': 'FLOAT'
            },
            'not_null': [
                'DISTRICT',
                'CASEID1',
                'CASEID2',
                'REASON',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID1'] = line[10:20].rstrip().lstrip()
            row['CASEID2'] = line[20:30].rstrip().lstrip()
            row['CRTHISID1'] = line[30:40].rstrip().lstrip()
            row['CRTHISID2'] = line[40:50].rstrip().lstrip()
            row['REASON'] = line[50:52].rstrip().lstrip()
            row['CREATE_DATE'] = line[52:63].rstrip().lstrip()
            row['CREATE_USER'] = line[63:93].rstrip().lstrip()
            row['UPDATE_DATE'] = line[93:104].rstrip().lstrip()
            row['UPDATE_USER'] = line[104:134].rstrip().lstrip()
            row['ID'] = line[134:144].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relate_part():
    global DIR
    filename = DIR + 'gs_relate_part.txt'
    data = []
    sql = {
            'primary': ['CASEID', 'PARTID1', 'PARTID2', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID1, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'PARTID2, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'REASON, DISTRICT': 'GS_RELATE_PART_REASON(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID1': n,
                'PARTID2': n,
                'REASON': v(2),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID1',
                'PARTID2',
                'REASON'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID1'] = line[20:30].rstrip().lstrip()
            row['PARTID2'] = line[30:40].rstrip().lstrip()
            row['REASON'] = line[40:42].rstrip().lstrip()
            row['CREATE_DATE'] = line[42:53].rstrip().lstrip()
            row['CREATE_USER'] = line[53:83].rstrip().lstrip()
            row['UPDATE_DATE'] = line[83:94].rstrip().lstrip()
            row['UPDATE_USER'] = line[94:125].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_cont_services():
    global DIR
    filename = DIR + 'gs_cont_services.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'CONTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'CONTID, CASEID, PARTID, DISTRICT': 'GS_CONTACT_LOG(ID, CASEID, PARTID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'SERV_AGENCY, DISTRICT': 'GS_SERV_AGENCY(ID, DISTRICT)',
                'SERV_TYPE, DISTRICT': 'GS_SERV_TYPE(CODE, DISTRICT)',
                'SERV_AGENCY, SERV_LANGUAGE, DISTRICT': 'GS_SERV_LANGUAGE(SERV_AGENCY, SERV_LANGUAGE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'CONTID': n,
                'ID': n,
                'SERV_AGENCY': n,
                'SERV_TYPE': v(4),
                'SERV_LANGUAGE': v(3),
                'SERV_SPECIAL': v(4),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'CONTID',
                'ID',
                'SERV_AGENCY'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['CONTID'] = line[30:40].rstrip().lstrip()
            row['ID'] = line[40:50].rstrip().lstrip()
            row['SERV_AGENCY'] = line[50:61].rstrip().lstrip()
            row['SERV_TYPE'] = line[61:65].rstrip().lstrip()
            row['SERV_LANGUAGE'] = line[65:68].rstrip().lstrip()
            row['SERV_SPECIAL'] = line[68:72].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:83].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[113:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[124:154].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_contact_log():
    global DIR
    filename = DIR + 'gs_contact_log.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'PURPOSE, DISTRICT': 'GS_CONTACT_PURP(CODE, DISTRICT)',
                'TYPE, DISTRICT': 'GS_CONTACT_TYPE(CODE, DISTRICT)',
                'INITIATOR': 'GS_INIATOR(CODE)',
                'STAFFID, DISTRICT': 'GS_STAFF(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'CONT_DATE': d,
                'PURPOSE': v(2),
                'TYPE': v(2),
                'INITIATOR': v(2),
                'STAFFID': n,
                'DOC_CODE': v(3),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'CONT_DATE',
                'PURPOSE',
                'TYPE',
                'INITIATOR',
                'STAFFID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['CONT_DATE'] = line[40:51].rstrip().lstrip()
            row['PURPOSE'] = line[51:53].rstrip().lstrip()
            row['TYPE'] = line[53:55].rstrip().lstrip()
            row['INITIATOR'] = line[55:57].rstrip().lstrip()
            row['STAFFID'] = line[57:67].rstrip().lstrip()
            row['DOC_CODE'] = line[67:70].rstrip().lstrip()
            row['CREATE_DATE'] = line[70:81].rstrip().lstrip()
            row['CREATE_USER'] = line[81:111].rstrip().lstrip()
            row['UPDATE_DATE'] = line[111:122].rstrip().lstrip()
            row['UPDATE_USER'] = line[122:152].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_control_sub():
    global DIR
    filename = DIR + 'gs_control_sub.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE': 'GS_CONTROL_TYPE(CODE)',
                'MEASURE': 'GS_MEASURE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'TYPE': v(1),
                'QUANTITY': 'FLOAT',
                'MEASURE': v(1),
                'OTHER_DESCRIP': v(30),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'TYPE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['TYPE'] = line[30:31].rstrip().lstrip()
            row['QUANTITY'] = line[31:45].rstrip().lstrip()
            row['MEASURE'] = line[45:46].rstrip().lstrip()
            row['OTHER_DESCRIP'] = line[46:76].rstrip().lstrip()
            row['CREATE_DATE'] = line[76:87].rstrip().lstrip()
            row['CREATE_USER'] = line[87:117].rstrip().lstrip()
            row['UPDATE_DATE'] = line[117:128].rstrip().lstrip()
            row['UPDATE_USER'] = line[128:158].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_count():
    global DIR
    filename = DIR + 'gs_count.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CRTHISID', 'INSTID', 'CHARGE', 'CATEGORY', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'INSTID': 'GS_INSTRUMENT(ID, CASEID, CRTHISID, DISTRICT)',
                'CHARGE' : 'GS_CHARGE_TYPE(CODE)',
                'CATEGORY': 'GS_CHARGE_CAT(CODE)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'INSTID': n,
                'CHARGE': v(25),
                'CATEGORY': v(1),
                'ID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'INSTID',
                'CHARGE',
                'CATEGORY',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CRTHISID'] = line[20:30].rstrip().lstrip()
            row['INSTID'] = line[30:40].rstrip().lstrip()
            row['CHARGE'] = line[41:65].rstrip().lstrip()
            row['CATEGORY'] = line[65:66].rstrip().lstrip()
            row['ID'] = line[66:76].rstrip().lstrip()
            row['CREATE_DATE'] = line[76:87].rstrip().lstrip()
            row['CREATE_USER'] = line[87:117].rstrip().lstrip()
            row['UPDATE_DATE'] = line[117:128].rstrip().lstrip()
            row['UPDATE_USER'] = line[128:158].rstrip().lstrip()
            row['PENT_PROV'] = line[158:183].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# Parse DISK03
def gs_court_hist():
    global DIR
    filename = DIR + 'gs_court_hist.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'COURT': 'GS_COURT(CODE)',
                'LOCATION, DISTRICT': 'GS_LOCATION(CODE, DISTRICT)',
                'US_ROLE': 'GS_US_ROLE(CODE)',
                'APPEAL_TYPE': 'GS_APPEAL_TYPE(CODE)',
                'DISPOSITION': 'GS_DISP_TYPE(CODE)',
                'DISP_REASON1': 'GS_DISP_REAS_TYPE(CODE)',
                'DISP_REASON2': 'GS_DISP_REAS_TYPE(CODE)',
                'DISP_REASON3': 'GS_DISP_REAS_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'COURT': v(2),
                'LOCATION': v(2),
                'US_ROLE': v(2),
                'COURT_NUMBER': v(25),
                'FILING_DATE': d,
                'SERVICE_DATE': d,
                'TRIAL_DAYS': 'FLOAT',
                'NOAP_DATE': d,
                'APPEAL_TYPE': v(1),
                'SENT_APPEAL': v(1),
                'DISPOSITION': v(2),
                'DISP_DATE': d,
                'DISP_REASON1': v(4),
                'DISP_REASON2': v(4),
                'DISP_REASON3': v(4),
                'SYS_DISP_DATE': d,
                'SYS_FILING_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'COURT',
                'US_ROLE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['COURT'] = line[30:32].rstrip().lstrip()
            row['LOCATION'] = line[32:34].rstrip().lstrip()
            row['US_ROLE'] = line[34:36].rstrip().lstrip()
            row['COURT_NUMBER'] = line[36:61].rstrip().lstrip()
            row['FILING_DATE'] = line[61:72].rstrip().lstrip()
            row['SERVICE_DATE'] = line[72:83].rstrip().lstrip()
            row['TRIAL_DAYS'] = line[83:97].rstrip().lstrip()
            row['NOAP_DATE'] = line[97:108].rstrip().lstrip()
            row['APPEAL_TYPE'] = line[108:109].rstrip().lstrip()
            row['SENT_APPEAL'] = line[109:110].rstrip().lstrip()
            row['DISPOSITION'] = line[110:112].rstrip().lstrip()
            row['DISP_DATE'] = line[112:123].rstrip().lstrip()
            row['DISP_REASON1'] = line[123:127].rstrip().lstrip()
            row['DISP_REASON2'] = line[127:131].rstrip().lstrip()
            row['DISP_REASON3'] = line[131:135].rstrip().lstrip()
            row['SYS_DISP_DATE'] = line[135:146].rstrip().lstrip()
            row['SYS_FILING_DATE'] = line[146:157].rstrip().lstrip()
            row['CREATE_DATE'] = line[157:168].rstrip().lstrip()
            row['CREATE_USER'] = line[168:198].rstrip().lstrip()
            row['UPDATE_DATE'] = line[198:209].rstrip().lstrip()
            row['UPDATE_USER'] = line[209:239].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_court_judge():
    global DIR
    filename = DIR + 'gs_court_judge.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CRTHISID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'JUDGEID, DISTRICT': 'GS_JUDGE(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'ID': n,
                'JUDGEID': n,
                'DECISION': v(4),
                'START_DATE': d,
                'END_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'ID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CRTHISID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['JUDGEID'] = line[40:50].rstrip().lstrip()
            row['DECISION'] = line[50:54].rstrip().lstrip()
            row['START_DATE'] = line[54:65].rstrip().lstrip()
            row['END_DATE'] = line[65:76].rstrip().lstrip()
            row['CREATE_DATE'] = line[76:87].rstrip().lstrip()
            row['CREATE_USER'] = line[87:117].rstrip().lstrip()
            row['UPDATE_DATE'] = line[117:128].rstrip().lstrip()
            row['UPDATE_USER'] = line[128:158].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_dna():
    global DIR
    filename = DIR + 'gs_dna.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(3),
                'ID': n,
                'CASEID': v(10),
                'PROCEEDINGS_AFT_RELIEF_GRANTED': v(1),
                'NEW_TRIAL_ORD': v(1),
                'CHARGE_DISMISSED': v(1),
                'GUILTY_PLEA_ENTERED': v(1),
                'FOUND_GUILTY': v(1),
                'ACQUITTED': v(1),
                'RESENTENCING_CAP_CASE': v(1),
                'TESTINGS_ORDERED': v(1),
                'RELIEF_GRANTED': v(1),
                'COMMENTS': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'CASEID',
                'PROCEEDINGS_AFT_RELIEF_GRANTED'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3].rstrip().lstrip()
            row['ID'] = line[3:13].rstrip().lstrip()
            row['CASEID'] = line[13:23].rstrip().lstrip()
            row['PROCEEDINGS_AFT_RELIEF_GRANTED'] = line[23:24].rstrip().lstrip()
            row['NEW_TRIAL_ORD'] = line[24:25].rstrip().lstrip()
            row['CHARGE_DISMISSED'] = line[25:26].rstrip().lstrip()
            row['GUILTY_PLEA_ENTERED'] = line[26:27].rstrip().lstrip()
            row['FOUND_GUILTY'] = line[27:28].rstrip().lstrip()
            row['ACQUITTED'] = line[28:29].rstrip().lstrip()
            row['RESENTENCING_CAP_CASE'] = line[29:30].rstrip().lstrip()
            row['TESTING_ORDERED'] = line[30:31].rstrip().lstrip()
            row['RELIEF_GRANTED'] = line[31:32].rstrip().lstrip()
            row['COMMENTS'] = line[32:33].rstrip().lstrip()
            row['CREATE_DATE'] = line[33:44].rstrip().lstrip()
            row['CREATE_USER'] = line[44:74].rstrip().lstrip()
            row['UPDATE_DATE'] = line[74:85].rstrip().lstrip()
            row['UPDATE_USER'] = line[85:115].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_prop_value():
    global DIR
    filename = DIR + 'gs_prop_value.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE, DISTRICT': 'GS_PROP_VALUE_TYPE(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(1),
                'PARTID': n,
                'ID': n,
                'TYPE': v(2),
                'VALUE': 'FLOAT',
                'PROP_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'TYPE',
                'VALUE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['TYPE'] = line[40:42].rstrip().lstrip()
            row['VALUE'] = line[42:56].rstrip().lstrip()
            row['PROP_DATE'] = line[56:67].rstrip().lstrip()
            row['CREATE_DATE'] = line[67:78].rstrip().lstrip()
            row['CREATE_USER'] = line[78:108].rstrip().lstrip()
            row['UPDATE_DATE'] = line[108:119].rstrip().lstrip()
            row['UPDATE_USER'] = line[119:149].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_region():
    global DIR
    filename = DIR + 'gs_region.txt'
    data = []
    sql = {
            'primary': ['BRANCH', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(3),
                'BRANCH': v(3),
                'DESCRIPTION': v(3),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'BRANCH',
                'DESCRIPTION'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3].rstrip().lstrip()
            row['BRANCH'] = line[3:6].rstrip().lstrip()
            row['DESCRIPTION'] = line[6:36].rstrip().lstrip()
            row['CREATE_DATE'] = line[36:47].rstrip().lstrip()
            row['CREATE_USER'] = line[47:77].rstrip().lstrip()
            row['UPDATE_DATE'] = line[77:88].rstrip().lstrip()
            row['UPDATE_USER'] = line[88:118].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relate_appeal():
    global DIR
    filename = DIR + 'gs_relate_appeal.txt'
    data = []
    sql = {
            'primary': ['CASEID1', 'CRTHISID1', 'CASEID2', 'CRTHISID2', 'REASON', 'DISTRICT'],
            'foreign':{
                'CASEID1, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID1, CASEID1, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'CASEID2, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID2, CASEID2, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'REASON, DISTRICT': 'GS_RELATE_CASE_REASON(CODE, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID1': v(10),
                'CRTHISID1': n,
                'CASEID2': v(10),
                'CRTHISID2': n,
                'REASON': v(2),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID1',
                'CRTHISID1',
                'CASEID2',
                'CRTHISID2',
                'REASON'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID1'] = line[0:20].rstrip().lstrip()
            row['CRTHISID1'] = line[20:30].rstrip().lstrip()
            row['CASEID2'] = line[30:40].rstrip().lstrip()
            row['CRTHISID2'] = line[40:50].rstrip().lstrip()
            row['REASON'] = line[50:52].rstrip().lstrip()
            row['CREATE_DATE'] = line[52:63].rstrip().lstrip()
            row['CREATE_USER'] = line[63:93].rstrip().lstrip()
            row['UPDATE_DATE'] = line[93:104].rstrip().lstrip()
            row['UPDATE_USER'] = line[104:134].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# DISK04
def gs_sentence():
    global DIR
    filename = DIR + 'gs_sentence.txt'
    data = []
    sql = {
            'primary': ['CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'GUIDE_DEPART': 'GS_GUIDE_DEPART(CODE)',
                'INCAR_TYPE': 'GS_INCAR_TYPE(CODE)',
                'JUDGEID, DISTRICT': 'GS_JUDGE(ID, DISTRICT)',
                'SPEC_CONDITION': 'GS_SPECIAL_CONDITION(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'SENT_DATE': d,
                'GUIDE_DEPART': v(1),
                'INCAR_TYPE': v(3),
                'JUDGEID': v(10),
                'PROB_DAYS': n,
                'PROB_MONTHS': n,
                'PROB_YEARS': n,
                'SUPER_REL_DAYS': n,
                'SUPER_REL_MONTHS': n,
                'SUPER_REL_YEARS': n,
                'INCAR_DAYS': n,
                'INCAR_MONTHS': n,
                'INCAR_YEARS': n,
                'FINE': 'FLOAT',
                'SPEC_ASSESSMENT': 'FLOAT',
                'DISBARRED': v(1),
                'SPEC_CONDITION': v(4),
                'PROBATION_REVOKED': v(1),
                'SUPER_REL_REVOKED': v(1),
                'TOTAL_REVOKED_DAYS': n,
                'TOTAL_REVOKED_MONTHS': n,
                'TOTAL_REVOKED_YEARS': n,
                'RELATED_FLU_USAO': v(10),
                'RELATED_FLU_SEQ': v(3),
                'COMM_SERV_HOURS': 'FLOAT',
                'SYS_SENT_DATE': d,
                'RESITUTION_AMT': 'FLOAT',
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)',
                'SUPV_REL_INCAR_TYPE': v(1)
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'SENT_DATE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['SENT_DATE'] = line[30:41].rstrip().lstrip()
            row['GUIDE_DEPART'] = line[41:42].rstrip().lstrip()
            row['INCAR_TYPE'] = line[42:45].rstrip().lstrip()
            row['JUDGEID'] = line[45:55].rstrip().lstrip()
            row['PROB_DAYS'] = line[55:66].rstrip().lstrip()
            row['PROB_MONTHS'] = line[66:77].rstrip().lstrip()
            row['PROB_YEARS'] = line[77:88].rstrip().lstrip()
            row['SUPER_REL_DAYS'] = line[88:99].rstrip().lstrip()
            row['SUPER_REL_MONTHS'] = line[99:110].rstrip().lstrip()
            row['SUPER_REL_YEARS'] = line[110:121].rstrip().lstrip()
            row['INCAR_DAYS'] = line[121:132].rstrip().lstrip()
            row['INCAR_MONTHS'] = line[132:143].rstrip().lstrip()
            row['INCAR_YEARS'] = line[143:154].rstrip().lstrip()
            row['FINE'] = line[154:168].rstrip().lstrip()
            row['SPEC_ASSESSMENT'] = line[168:182].rstrip().lstrip()
            row['DEBARRED'] = line[182:183].rstrip().lstrip()
            row['SPEC_CONDITION'] = line[183:187].rstrip().lstrip()
            row['PROBATION_REVOKED'] = line[187:188].rstrip().lstrip()
            row['SUPER_REL_REVOKED'] = line[188:189].rstrip().lstrip()
            row['TOTAL_REVOKED_DAYS'] = line[189:200].rstrip().lstrip()
            row['TOTAL_REVOKED_MONTHS'] = line[200:211].rstrip().lstrip()
            row['TOTAL_REVOKED_YEARS'] = line[211:222].rstrip().lstrip()
            row['RELATED_FLU_USAO'] = line[222:232].rstrip().lstrip()
            row['RELATED_FLU_SEQ'] = line[232:235].rstrip().lstrip()
            row['COMM_SERV_HOURS'] = line[235:247].rstrip().lstrip()
            row['SYS_SENT_DATE'] = line[257:258].rstrip().lstrip()
            row['RESTITUTION_AMT'] = line[258:274].rstrip().lstrip()
            row['CREATE_DATE'] = line[274:285].rstrip().lstrip()
            row['CREATE_USER'] = line[285:315].rstrip().lstrip()
            row['UPDATE_DATE'] = line[315:326].rstrip().lstrip()
            row['UPDATE_USER'] = line[326:356].rstrip().lstrip()
            row['SUPV_REL_INCAR_TYPE'] = line[356:357].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# they split it up by district
def gs_event():
    global DIR
    districts = get_district_list()
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CRTHISID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE, DISTRICT': 'GS_EVENT_TYPE(CODE, DISTRICT)',
                'ACTION, DISTRICT': 'GS_ACTION(CODE, DISTRICT)',
                'JUDGEID': 'GS_JUDGE(ID, DISTRICT)',
                'STAFFID, DISTRICT': 'GS_STAFF(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'ID': n,
                'TYPE': v(4),
                'ACTION': v(2),
                'EVENT_DATE': d,
                'SCHED_DATE': d,
                'SCHED_TIME': d,
                'SCHED_LOC': v(200),
                'STAFFID': n,
                'JUDGEID': n,
                'DOCUMENT_CODE': v(3),
                'DOCUMENT_STAFFID': n,
                'DOCUMENT_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'ID',
                'TYPE'
            ]
    }
    for district in districts:
        filename = DIR + 'gs_event_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10].rstrip().lstrip()
                row['CASEID'] = line[10:20].rstrip().lstrip()
                row['CRTHISID'] = line[20:30].rstrip().lstrip()
                row['ID'] = line[30:40].rstrip().lstrip()
                row['TYPE'] = line[40:44].rstrip().lstrip()
                row['ACTION'] = line[44:46].rstrip().lstrip()
                row['EVENT_DATE'] = line[46:47].rstrip().lstrip()
                row['SCHED_DATE'] = line[47:68].rstrip().lstrip()
                row['SCHED_TIME'] = line[68:79].rstrip().lstrip()
                row['SCHED_LOC'] = line[79:279].rstrip().lstrip()
                row['STAFFID'] = line[279:289].rstrip().lstrip()
                row['JUDGEID'] = line[289:299].rstrip().lstrip()
                row['DOCUMENT_CODE'] = line[299:302].rstrip().lstrip()
                row['DOCUMENT_STAFFID'] = line[302:312].rstrip().lstrip()
                row['DOCUMENT_DATE'] = line[312:323].rstrip().lstrip()
                row['CREATE_DATE'] = line[323:334].rstrip().lstrip()
                row['CREATE_USER'] = line[334:364].rstrip().lstrip()
                row['UPDATE_DATE'] = line[364:375].rstrip().lstrip()
                row['UPDATE_USER'] = line[375:405].rstrip().lstrip()
                data.append(row)
    return (sql, data)


def gs_oppose_coun():
    global DIR
    filename = DIR + 'gs_oppose_coun.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'ATTORNEYID, DISTRICT': 'GS_OPPOSE_ATTORN(ID, DISTRICT)',
                'TYPE, DISTRICT': 'GS_COUNSEL_TYPE(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'ATTORNEYID': n,
                'TYPE': v(2),
                'START_DATE': d,
                'END_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'ATTORNEYID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['ATTORNEYID'] = line[40:50].rstrip().lstrip()
            row['TYPE'] = line[50:52].rstrip().lstrip()
            row['START_DATE'] = line[52:63].rstrip().lstrip()
            row['END_DATE'] = line[63:74].rstrip().lstrip()
            row['CREATE_DATE'] = line[74:85].rstrip().lstrip()
            row['CREATE_USER'] = line[85:115].rstrip().lstrip()
            row['UPDATE_DATE'] = line[115:126].rstrip().lstrip()
            row['UPDATE_USER'] = line[126:156].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_restitution():
    global DIR
    filename = DIR + 'gs_restitution.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT',
                'TYPE': 'GS_REST_TYPE(CODE)',
                'RECIPIENT': 'GS_REST_RECIPIENT(CODE)',
                'LIABILITY': 'GS_RELIEF_LIABILITY(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'VICTIMID': n,
                'TYPE': v(1),
                'RECIPENT': v(1),
                'AMOUNT': 'FLOAT',
                'LIABILITY': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'TYPE',
                'RECIPIENT',
                'AMOUNT'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['VICTIMID'] = line[40:50].rstrip().lstrip()
            row['TYPE'] = line[50:51].rstrip().lstrip()
            row['RECIPENT'] = line[51:52].rstrip().lstrip()
            row['AMOUNT'] = line[52:66].rstrip().lstrip()
            row['LIABILITY'] = line[66:67].rstrip().lstrip()
            row['CREATE_DATE'] = line[67:78].rstrip().lstrip()
            row['CREATE_USER'] = line[78:108].rstrip().lstrip()
            row['UPDATE_DATE'] = line[108:119].rstrip().lstrip()
            row['UPDATE_USER'] = line[119:149].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_participant():
    global DIR

    districts = get_district_list()
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT',
                'TYPE': 'GS_PART_TYPE(CODE)',
                'ROLE': 'GS_ROLE(CODE)',
                'SECURITY, DISTRICT': 'GS_SECURITY(CODE, DISTRICT)',
                'BUSINESS_TYPE, DISTRICT': 'GS_BUSINESS_TYPE(CODE, DISTRICT)',
                'PROP_TYPE, DISTRICT': 'GS_PROP_TYPE(CODE, DISTRICT)',
                'AGENCY': 'GS_AGENCY(CODE)',
                'JOB_POSITION, DISTRICT': 'GS_JOB_POSITION(CODE, DISTRICT)',
                'GENDER': 'GS_GENDER(CODE)',
                'RACE': 'GS_RACE(CODE)',
                'IMMIG_STAT, DISTRICT': 'GS_IMMIG_STAT(CODE, DISTRICT)',
                'COUNTRY': 'GS_COUNTRY_CIT(CODE)',
                'TRIBE': 'GS_TRIBE(CODE)',
                'RESERVATION, DISTRICT': 'GS_RESERVATION(CODE, DISTRICT)',
                'HOME_STATE': 'GS_STATE(CODE)',
                'OFF_STATE': 'GS_STATE(CODE)',
                'AGCYOFFID, DISTRICT': 'GS_AGENCY_OFF(ID, DISTRIC)',
                'EMPLOYER_TYPE': 'GS_EMPLOYER_TYPE(CODE)',
                'HCARE_BUSN_TYPE': 'GS_HCARE_BUSN_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'TYPE': v(1),
                'ROLE': v(2),
                'SECURITY': v(1),
                'DEFEND_NUM': n,
                'SALUTATION': v(20),
                'LAST_NAME': v(60),
                'FIRST_NAME': v(30),
                'TITLE': v(30),
                'LAST_SOUNDS': v(4),
                'FIRST_SOUNDS': v(4),
                'BUSINESS_TYPE': v(2),
                'EIN': v(20),
                'PROP_TYPE': v(2),
                'TOTAL_TRACTS': n,
                'CATS_ASSET_ID': v(15),
                'AGENCY': v(4),
                'AGENCY_NUM': v(30),
                'JOB_POSITION': v(4),
                'SSN': v(11),
                'BIRTHDATE': d,
                'GENDER': v(1),
                'JUVENILE': v(1),
                'RACE': v(2),
                'RACE_DESCRIP': v(30),
                'IMMIG_STAT': v(2),
                'COUNTRY': v(2),
                'TRIBE': v(4),
                'RESERVATION': v(4),
                'ARREST_DATE': d,
                'PDID': v(12),
                'FBI_NUMBER': v(15),
                'CRIM_HIST': v(1),
                'EST_LOST': 'FLOAT',
                'ACT_LOSS': 'FLOAT',
                'HOME_ADDRESS1': v(30),
                'HOME_ADDRESS2': v(30),
                'HOME_ADDRESS3': v(30),
                'HOME_CITY': v(20),
                'HOME_STATE': v(2),
                'HOME_COUNTY': v(20),
                'HOME_ZIPCODE': v(10),
                'HOME_PHONE': v(15),
                'HOME_FAX': v(15),
                'OFF_ADDRESS1': v(30),
                'OFF_ADDRESS2': v(30),
                'OFF_ADDRESS3': v(30),
                'OFF_CITY': v(20),
                'OFF_STATE': v(2),
                'OFF_COUNTY': v(20),
                'OFF_ZIPCODE': v(10),
                'OFF_PHONE': v(15),
                'OFF_FAX': v(15),
                'MARSHALS_NUM': v(9),
                'AGCYOFFID': n,
                'LOWER_CRT_TRIAL_NBR': v(25),
                'BUSINESS_CONTACT_LNAME': v(30),
                'BUSINESS_CONTACT_FNAME': v(30),
                'COLLECT_IND': v(1),
                'SYS_INIT_DATE': d,
                'WEIGHT': v(2),
                'EMPLOYER_NAME': v(40),
                'EMPLOYER_TYPE': v(3),
                'EMPLOYER_DESC': v(40),
                'NPI': v(10),
                'OCCUPATION': v(3),
                'OCCUP_DESC': v(60),
                'HCARE_BUSN_TYPE': v(3),
                'HCARE_BUSN_DESC': v(40),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'TYPE',
                'ROLE',
                'LAST_NAME',
                'SYS_INIT_DATE'
            ]
    }
    for district in districts:
        filename = DIR + 'gs_participant_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10].rstrip().lstrip()
                row['CASEID'] = line[10:20].rstrip().lstrip()
                row['ID'] = line[20:30].rstrip().lstrip()
                row['TYPE'] = line[30:31].rstrip().lstrip()
                row['ROLE'] = line[31:33].rstrip().lstrip()
                row['SECURITY'] = line[33:34].rstrip().lstrip()
                row['DEFEND_NUM'] = line[34:45].rstrip().lstrip()
                row['SALUTATION'] = line[45:65].rstrip().lstrip()
                row['LAST_NAME'] = line[65:125].rstrip().lstrip()
                row['FIRST_NAME'] = line[125:155].rstrip().lstrip()
                row['TITLE'] = line[155:185].rstrip().lstrip()
                row['LAST_SOUNDS'] = line[128:189].rstrip().lstrip()
                row['FIRST_SOUNDS'] = line[189:193].rstrip().lstrip()
                row['BUSINESS_TYPE'] = line[193:195].rstrip().lstrip()
                row['EIN'] = line[195:215].rstrip().lstrip()
                row['PROP_TYPE'] = line[215:217].rstrip().lstrip()
                row['TOTAL_TRACTS'] = line[217:228].rstrip().lstrip()
                row['CATS_ASSET_ID'] = line[228:243].rstrip().lstrip()
                row['AGENCY'] = line[243:247].rstrip().lstrip()
                row['AGENCY_NUM'] = line[247:277].rstrip().lstrip()
                row['JOB_POSITION'] = line[277:281].rstrip().lstrip()
                row['SSN'] = line[281:292].rstrip().lstrip()
                row['BIRTH_DATE'] = line[292:303].rstrip().lstrip()
                row['GENDER'] = line[303:304].rstrip().lstrip()
                row['JUVENILE'] = line[304:305].rstrip().lstrip()
                row['RACE'] = line[305:307].rstrip().lstrip()
                row['RACE_DESCRIP'] = line[307:337].rstrip().lstrip()
                row['IMMIG_STAT'] = line[337:339].rstrip().lstrip()
                row['COUNTRY'] = line[339:341].rstrip().lstrip()
                row['TRIBE'] = line[341:345].rstrip().lstrip()
                row['RESERVATION'] = line[345:349].rstrip().lstrip()
                row['ARREST_DATE'] = line[349:360].rstrip().lstrip()
                row['PDID'] = line[360:372].rstrip().lstrip()
                row['FBI_NUMBER'] = line[372:387].rstrip().lstrip()
                row['CRIM_HIST'] = line[387:388].rstrip().lstrip()
                row['EST_LOST'] = line[388:402].rstrip().lstrip()
                row['ACT_LOSS'] = line[402:416].rstrip().lstrip()
                row['HOME_ADDRESS1'] = line[416:446].rstrip().lstrip()
                row['HOME_ADDRESS2'] = line[446:476].rstrip().lstrip()
                row['HOME_ADDRESS3'] = line[476:506].rstrip().lstrip()
                row['HOME_CITY'] = line[506:526].rstrip().lstrip()
                row['HOME_STATE'] = line[526:528].rstrip().lstrip()
                row['HOME_COUNTY'] = line[528:548].rstrip().lstrip()
                row['HOME_ZIPCODE'] = line[548:558].rstrip().lstrip()
                row['HOME_PHONE'] = line[558:573].rstrip().lstrip()
                row['HOME_FAX'] = line[573:588].rstrip().lstrip()
                row['OFF_ADDRESS1'] = line[588:618].rstrip().lstrip()
                row['OFF_ADDRESS2'] = line[618:648].rstrip().lstrip()
                row['OFF_ADDRESS3'] = line[648:678].rstrip().lstrip()
                row['OFF_CITY'] = line[678:698].rstrip().lstrip()
                row['OFF_STATE'] = line[698:700].rstrip().lstrip()
                row['OFF_COUNTY'] = line[700:720].rstrip().lstrip()
                row['OFF_ZIPCODE'] = line[720:730].rstrip().lstrip()
                row['OFF_PHONE'] = line[730:745].rstrip().lstrip()
                row['OFF_FAX'] = line[745:760].rstrip().lstrip()
                row['MARSHALS_NUM'] = line[760:769].rstrip().lstrip()
                row['AGCYOFFID'] = line[769:779].rstrip().lstrip()
                row['LOWER_CRT_TRIAL_NBR'] = line[779:804].rstrip().lstrip()
                row['BUSINESS_CONTACT_LNAME'] = line[804:834].rstrip().lstrip()
                row['BUSINESS_CONTACT_FNAME'] = line[834:864].rstrip().lstrip()
                row['COLLECT_IND'] = line[864:865].rstrip().lstrip()
                row['SYS_INIT_DATE'] = line[865:876].rstrip().lstrip()
                row['WEIGHT'] = line[876:878].rstrip().lstrip()
                row['EMPLOYER_NAME'] = line[878:918].rstrip().lstrip()
                row['EMPLOYER_TYPE'] = line[918:921].rstrip().lstrip()
                row['EMPLOYER_DESC'] = line[921:961].rstrip().lstrip()
                row['NPI'] = line[961:971].rstrip().lstrip()
                row['OCCUPATION'] = line[971:974].rstrip().lstrip()
                row['OCCUP_DESC'] = line[974:1034].rstrip().lstrip()
                row['HCARE_BUSN_TYPE'] = line[1034:1037].rstrip().lstrip()
                row['HCARE_BUSN_DESC'] = line[1037:1077].rstrip().lstrip()
                row['CREATE_DATE'] = line[1077:1088].rstrip().lstrip()
                row['CREATE_USER'] = line[1088:1118].rstrip().lstrip()
                row['UPDATE_DATE'] = line[1118:1129].rstrip().lstrip()
                row['UPDATE_USER'] = line[1129:1159].rstrip().lstrip()
                data.append(row)
    return (sql, data)

def gs_part_event():
    global DIR
    districts = get_district_list()
    data = []
    sql = {
            'primary': ['CASEID', 'PARTID', 'CRTHISID', 'EVENTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'EVENTID, CASEID, CRTHISID, DISTRICT': 'GS_EVENT(ID, CASEID, CRTHISID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'

            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'CRTHISID': n,
                'EVENTID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'CRTHISID',
                'EVENTID'
            ]
    }
    for district in districts:
        filename = DIR + 'gs_part_event_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10].rstrip().lstrip()
                row['CASEID'] = line[10:20].rstrip().lstrip()
                row['PARTID'] = line[20:30].rstrip().lstrip()
                row['CRTHISID'] = line[30:40].rstrip().lstrip()
                row['EVENTID'] = line[40:50].rstrip().lstrip()
                row['CREATE_DATE'] = line[50:61].rstrip().lstrip()
                row['CREATE_USER'] = line[61:91].rstrip().lstrip()
                row['UPDATE_DATE'] = line[91:102].rstrip().lstrip()
                row['UPDATE_USER'] = line[102:132].rstrip().lstrip()
                data.append(row)
    return (sql, data)

def gs_court_order_disp():
    global DIR
    filename = DIR + 'gs_court_order_disp.txt'
    data = []

    # The keys don't seem right here
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CODE': 'GS_ORDER_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(3),
                'ID': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'PARTID': n,
                'CODE': v(4),
                'SYSTEM_DATE': d,
                'DATE_OF_ORDER': d,
                'LAST_NAME': v(60),
                'FIRST_NAME': v(30),
                'COURT': v(4),
                'COURT_NUMBER': v(25),
                'PARTID2': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'CASEID',
                'CRTHISID',
                'PARTID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3].rstrip().lstrip()
            row['ID'] = line[3:13].rstrip().lstrip()
            row['CASEID'] = line[13:23].rstrip().lstrip()
            row['CRTHISID'] = line[23:33].rstrip().lstrip()
            row['PARTID'] = line[33:43].rstrip().lstrip()
            row['CODE'] = line[43:47].rstrip().lstrip()
            row['SYSTEM_DATE'] = line[47:58].rstrip().lstrip()
            row['DATE_OF_ORDER'] = line[58:69].rstrip().lstrip()
            row['LAST_NAME'] = line[69:129].rstrip().lstrip()
            row['FIRST_NAME'] = line[129:159].rstrip().lstrip()
            row['COURT'] = line[159:163].rstrip().lstrip()
            row['COURT_NUMBER'] = line[163:188].rstrip().lstrip()
            row['PARTID2'] = line[188:198].rstrip().lstrip()
            row['CREATE_DATE'] = line[198:209].rstrip().lstrip()
            row['CREATE_USER'] = line[209:239].rstrip().lstrip()
            row['UPDATE_DATE'] = line[239:250].rstrip().lstrip()
            row['UPDATE_USER'] = line[250:280].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_defend_stat():
    global DIR
    filename = DIR + 'gs_defend_stat.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE': 'GS_DEFEND_STAT_TYPE(CODE)',
                'CUSTODY_LOC, DISTRICT': 'GS_CUSTODY_LOC(CODE, DISTRICT)',
                'DETEN_REASON, DISTRICT': 'GS_DETEN_REASON(CODE, DISTRICT)',
                'BOND_TYPE': 'GS_BOND_TYPE(CODE)',
                'TERM_REASON': 'GS_TERM_REASON(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'TYPE': v(2),
                'START_DATE': d,
                'CUSTODY_LOC': v(2),
                'DETEN_REASON': v(4),
                'BOND_TYPE': v(2),
                'BOND_AMOUNT': 'FLOAT',
                'BOND_PROVIDER': v(25),
                'TERM_REASON': v(2),
                'END_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'TYPE',
                'START_DATE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['TYPE'] = line[40:42].rstrip().lstrip()
            row['START_DATE'] = line[42:53].rstrip().lstrip()
            row['CUSTODY_LOC'] = line[53:55].rstrip().lstrip()
            row['DETEN_REASON'] = line[55:59].rstrip().lstrip()
            row['BOND_TYPE'] = line[59:61].rstrip().lstrip()
            row['BOND_AMOUNT'] = line[61:75].rstrip().lstrip()
            row['BOND_PROVIDER'] = line[75:100].rstrip().lstrip()
            row['TERM_REASON'] = line[100:102].rstrip().lstrip()
            row['END_DATE'] = line[102:113].rstrip().lstrip()
            row['CREATE_DATE'] = line[113:124].rstrip().lstrip()
            row['CREATE_USER'] = line[124:154].rstrip().lstrip()
            row['UPDATE_DATE'] = line[154:165].rstrip().lstrip()
            row['UPDATE_USER'] = line[165:195].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_instrument():
    global DIR
    filename = DIR + 'gs_instrument.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CRTHISID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE': 'GS_INST_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'ID': n,
                'TYPE': v(2),
                'FILING_DATE': d,
                'SYS_FILING_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'ID',
                'TYPE',
                'FILING_DATE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CRTHISID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['TYPE'] = line[40:42].rstrip().lstrip()
            row['FILING_DATE'] = line[42:53].rstrip().lstrip()
            row['SYS_FILING_DATE'] = line[53:64].rstrip().lstrip()
            row['CREATE_DATE'] = line[64:75].rstrip().lstrip()
            row['CREATE_USER'] = line[75:105].rstrip().lstrip()
            row['UPDATE_DATE'] = line[105:116].rstrip().lstrip()
            row['UPDATE_USER'] = line[116:146].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_agent():
    global DIR
    filename = DIR + 'gs_instrument.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'ID': n,
                'SALUTATION': v(8),
                'LAST_NAME': v(30),
                'FIRST_NAME': v(30),
                'TITLE': v(30),
                'PHONE': v(20),
                'FAX': v(15),
                'PAGER': v(15),
                'LEAD_AGENT': v(1),
                'EMAIL': v(100),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'ID',
                'LAST_NAME'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['SALUTATION'] = line[40:48].rstrip().lstrip()
            row['LAST_NAME'] = line[48:78].rstrip().lstrip()
            row['FIRST_NAME'] = line[78:108].rstrip().lstrip()
            row['TITLE'] = line[108:138].rstrip().lstrip()
            row['PHONE'] = line[138:158].rstrip().lstrip()
            row['FAX'] = line[158:173].rstrip().lstrip()
            row['PAGER'] = line[173:188].rstrip().lstrip()
            row['LEAD_AGENT'] = line[188:189].rstrip().lstrip()
            row['EMAIL'] = line[189:289].rstrip().lstrip()
            row['CREATE_DATE'] = line[289:300].rstrip().lstrip()
            row['CREATE_USER'] = line[300:330].rstrip().lstrip()
            row['UPDATE_DATE'] = line[330:341].rstrip().lstrip()
            row['UPDATE_USER'] = line[341:371].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_part_court():
    global DIR
    filename = DIR + 'gs_part_court.txt'
    data = []
    sql = {
            'primary': [],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                #'APPEAL_ROLE': , FIND THIS LATER
                'DISPOSITION': 'GS_DISP_TYPE(CODE)',
                'DISP_REASON': 'GS_DISP_REAS_TYPE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'CRTHISID': n,
                'APPEAL_ROLE': v(2),
                'DISPOSITION': v(2),
                'DISP_REASON': v(4),
                'DISP_DATE': d,
                'SYS_DISP_DATE': d,
                'SYS_INIT_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'CRTHISID',
                'SYS_INIT_DATE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['CRTHISID'] = line[30:40].rstrip().lstrip()
            row['APPEAL_ROLE'] = line[40:42].rstrip().lstrip()
            row['DISPOSITION'] = line[42:44].rstrip().lstrip()
            row['DISP_REASON'] = line[44:48].rstrip().lstrip()
            row['DISP_DATE'] = line[48:59].rstrip().lstrip()
            row['SYS_DISP_DATE'] = line[59:70].rstrip().lstrip()
            row['SYS_INIT_DATE'] = line[70:81].rstrip().lstrip()
            row['CREATE_DATE'] = line[81:92].rstrip().lstrip()
            row['CREATE_USER'] = line[92:122].rstrip().lstrip()
            row['UPDATE_DATE'] = line[122:133].rstrip().lstrip()
            row['UPDATE_USER'] = line[133:163].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_assignment():
    global DIR
    filename = DIR + 'gs_assignment.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'CRTHISID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT',
                'STAFFID, DISTRICT': 'GS_STAFF(ID, DISTRICT)',
                'POSITION, DISTRICT': 'GS_POSITION(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'CRTHISID': n,
                'ID': n,
                'STAFFID': n,
                'POSITION': v(1),
                'START_DATE': d,
                'END_DATE': d,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'CRTHISID',
                'ID',
                'STAFFID',
                'POSITION'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['CRTHISID'] = line[20:30].rstrip().lstrip()
            row['ID'] = line[30:40].rstrip().lstrip()
            row['STAFFID'] = line[40:50].rstrip().lstrip()
            row['POSITION'] = line[50:51].rstrip().lstrip()
            row['START_DATE'] = line[51:62].rstrip().lstrip()
            row['END_DATE'] = line[62:73].rstrip().lstrip()
            row['CREATE_DATE'] = line[73:84].rstrip().lstrip()
            row['CREATE_USER'] = line[84:114].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:125].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:155].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_part_count():
    global DIR
    filename = DIR + 'gs_part_count.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'PARTID', 'CRTHISID', 'INSTID', 'CHARGE', 'CATEGORY', 'COUNTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'CRTHISID, CASEID, DISTRICT': 'GS_COURT_HIST(ID, CASEID, DISTRICT)',
                'INSTID, CASEID, CRTHISID, DISTRICT': 'GS_INSTRUMENT(ID, CASEID, CRTHISID, DISTRICT)',
                'CHARGE': 'GS_CHARGE_TYPE(CODE)',
                'CATEGORY': 'GS_CHARGE_CAT(CODE)',
                'COUNTID, CASEID, CRTHISID, INSTID, CHARGE, CATEGORY, DISTRICT': 'GS_COUNT(ID, CASEID, CRTHISID, INSTID, CHARGE, CATEGORY, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'CRTHISID': n,
                'INSTID': n,
                'CHARGE': v(25),
                'CATEGORY': v(1),
                'COUNTID': n,
                'DISPOSITION': v(2),
                'DISP_REASON': v(4),
                'DISP_DATE': d,
                'SEALED': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'CRTHISID',
                'INSTID',
                'CHARGE',
                'CATEGORY',
                'COUNTID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['CRTHISID'] = line[30:40].rstrip().lstrip()
            row['INSTID'] = line[40:50].rstrip().lstrip()
            row['CHARGE'] = line[50:75].rstrip().lstrip()
            row['CATEGORY'] = line[75:76].rstrip().lstrip()
            row['COUNTID'] = line[76:86].rstrip().lstrip()
            row['DISPOSITION'] = line[86:88].rstrip().lstrip()
            row['DISP_REASON'] = line[88:92].rstrip().lstrip()
            row['DISP_DATE'] = line[92:103].rstrip().lstrip()
            row['SEALED'] = line[103:104].rstrip().lstrip()
            row['CREATE_DATE'] = line[104:115].rstrip().lstrip()
            row['CREATE_USER'] = line[115:145].rstrip().lstrip()
            row['UPDATE_DATE'] = line[145:156].rstrip().lstrip()
            row['UPDATE_USER'] = line[156:186].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_part_relief():
    global DIR
    filename = DIR + 'gs_part_relief.txt'
    data = []
    sql = {
            'primary': ['CASEID', 'PARTID', 'RELIEFID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'RELIEFID, CASEID, DISTRICT': 'GS_RELIEF(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'RELIEFID': n,
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID',
                'RELIEFID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['RELIEFID'] = line[30:40].rstrip().lstrip()
            row['CREATE_DATE'] = line[40:51].rstrip().lstrip()
            row['CREATE_USER'] = line[51:81].rstrip().lstrip()
            row['UPDATE_DATE'] = line[81:92].rstrip().lstrip()
            row['UPDATE_USER'] = line[92:122].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relief():
    global DIR
    filename = DIR + 'gs_relief.txt'
    data = []
    sql = {
            'primary': ['ID', 'CASEID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'TYPE': 'GS_RELIEF_TYPE(CODE)',
                'STAGE': 'GS_RELIEF_STAGE(CODE)',
                'REQUESTED_BY': 'GS_RELIEF_REQUESTED_BY(CODE)',
                'LIABILITY': 'GS_RELIEF_LIABILITY(CODE)',
                'AGENCY': 'GS_AGENCY(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID': n,
                'TYPE': v(1),
                'STAGE': v(1),
                'REQUESTED_BY': v(1),
                'LIABILITY': v(1),
                'AMOUNT': 'FLOAT',
                'NONMONETARY': v(30),
                'AGENCY': v(4),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID',
                'TYPE',
                'STAGE',
                'REQUESTED_BY',
                'AGENCY'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID'] = line[20:30].rstrip().lstrip()
            row['TYPE'] = line[30:31].rstrip().lstrip()
            row['STAGE'] = line[31:32].rstrip().lstrip()
            row['REQUESTED_BY'] = line[32:33].rstrip().lstrip()
            row['LIABILITY'] = line[33:34].rstrip().lstrip()
            row['AMOUNT'] = line[34:50].rstrip().lstrip()
            row['NONMONETARY'] = line[50:80].rstrip().lstrip()
            row['AGENCY'] = line[80:84].rstrip().lstrip()
            row['CREATE_DATE'] = line[84:95].rstrip().lstrip()
            row['CREATE_USER'] = line[95:125].rstrip().lstrip()
            row['UPDATE_DATE'] = line[125:136].rstrip().lstrip()
            row['UPDATE_USER'] = line[136:166].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_triggerlock():
    global DIR
    filename = DIR + 'gs_triggerlock.txt'
    data = []
    sql = {
            'primary': ['CASEID', 'PARTID', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'PARTID, CASEID, DISTRICT': 'GS_PARTICIPANT(ID, CASEID, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'PARTID': n,
                'BRADY_OFFENSE': v(1),
                'NOTICE_3_STRIKES': v(1),
                'DATE_NOTICE_FILED': d,
                'DATE_NOTICE_WITHDRAWN': d,
                'WITHDRAWAL_REASON': v(78),
                'CONVICTION_3_STRIKES': v(1),
                'LIFE_3_STRIKES': v(1),
                'NO_LIFE_REASON': v(78),
                'THIRD_PROSEC_TRIGG_OFFENSE': v(1),
                'TRIGGERLOCK_DEF': v(1),
                'BAILEY_SENTENCE_CHANGE': v(1),
                'SENTENCE_PRIOR_BAILEY': n,
                'ARMED_CAREER_CRIMINAL': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'PARTID'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['PARTID'] = line[20:30].rstrip().lstrip()
            row['BRADY_OFFENSE'] = line[30:31].rstrip().lstrip()
            row['NOTICE_3_STRIKES'] = line[31:32].rstrip().lstrip()
            row['DATE_NOTICE_FILED'] = line[32:43].rstrip().lstrip()
            row['DATE_NOTICE_WITHDRAWN'] = line[43:54].rstrip().lstrip()
            row['WITHDRAWAL_REASON'] = line[54:132].rstrip().lstrip()
            row['CONVICTION_3_STRIKES'] = line[132:133].rstrip().lstrip()
            row['LIFE_3_STRIKES'] = line[133:134].rstrip().lstrip()
            row['NO_LIFE_REASON'] = line[134:212].rstrip().lstrip()
            row['THIRD_PROSEC_TRIGG_OFFENSE'] = line[212:213].rstrip().lstrip()
            row['TRIGGERLOCK_DEF'] = line[213:214].rstrip().lstrip()
            row['BAILEY_SENTENCE_CHANGE'] = line[214:215].rstrip().lstrip()
            row['SENTENCE_PRIOR_BAILEY'] = line[215:226].rstrip().lstrip()
            row['ARMED_CAREER_CRIMINAL'] = line[226:227].rstrip().lstrip()
            row['CREATE_DATE'] = line[227:238].rstrip().lstrip()
            row['CREATE_USER'] = line[238:268].rstrip().lstrip()
            row['UPDATE_DATE'] = line[268:279].rstrip().lstrip()
            row['UPDATE_USER'] = line[279:309].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_comment():
    global DIR
    filename = DIR + 'gs_comment.txt'
    data = []
    sql = {
            'primary': ['ID1', 'ID2', 'CASEID', 'CATEGORY', 'DISTRICT'],
            'foreign':{
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'CATEGORY': 'GS_COMMENT_CAT(CODE)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'CASEID': v(10),
                'ID1': n,
                'ID2': n,
                'CATEGORY': v(1),
                'TEXT': v(1),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CASEID',
                'ID1',
                'ID2',
                'CATEGORY',
                'TEXT'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['CASEID'] = line[10:20].rstrip().lstrip()
            row['ID1'] = line[20:30].rstrip().lstrip()
            row['ID2'] = line[30:40].rstrip().lstrip()
            row['CATEGORY'] = line[40:41].rstrip().lstrip()
            row['TEXT'] = line[41:42].rstrip().lstrip()
            row['CREATE_DATE'] = line[42:53].rstrip().lstrip()
            row['CREATE_USER'] = line[53:83].rstrip().lstrip()
            row['UPDATE_DATE'] = line[83:94].rstrip().lstrip()
            row['UPDATE_USER'] = line[94:124].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_request():
    global DIR
    filename = DIR + 'gs_request.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'CASEID, DISTRICT': 'GS_CASE(ID, DISTRICT)',
                'STAFFID, DISTRICT': 'GS_STAFF(ID, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(10),
                'ID': n,
                'CASEID': v(10),
                'STAFFID': n,
                'REQUEST_DATE': d,
                'RECEIVE_DATE': d,
                'RETURN_DATE': d,
                'STORE_NUM': v(20),
                'BOXID': v(9),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'STAFFID',
                'REQUEST_DATE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10].rstrip().lstrip()
            row['ID'] = line[10:20].rstrip().lstrip()
            row['CASEID'] = line[20:30].rstrip().lstrip()
            row['STAFFID'] = line[30:40].rstrip().lstrip()
            row['REQUEST_DATE'] = line[40:51].rstrip().lstrip()
            row['RECEIVE_DATE'] = line[51:62].rstrip().lstrip()
            row['RETURN_DATE'] = line[62:73].rstrip().lstrip()
            row['STORE_NUM'] = line[73:93].rstrip().lstrip()
            row['BOXID'] = line[93:102].rstrip().lstrip()
            row['CREATE_DATE'] = line[102:113].rstrip().lstrip()
            row['CREATE_USER'] = line[113:143].rstrip().lstrip()
            row['UPDATE_DATE'] = line[143:154].rstrip().lstrip()
            row['UPDATE_USER'] = line[154:184].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_staff():
    global DIR
    filename = DIR + 'gs_staff.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'INIT_STAT': 'GS_INIT_STAT(CODE)',
                'STAFF_TITLE, DISTRICT': 'GS_STAFF_TILE(CODE, DISTRICT)',
                'STAFF_SECTION, DISTRICT' : 'GS_STAFF_SECTION(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(3),
                'ID': n,
                'USERNAME': v(18),
                'INITIALS': v(8),
                'INIT_STAT': v(1),
                'STAFF_TITLE': v(3),
                'SALUTATION': v(8),
                'LAST_NAME': v(30),
                'FIRST_NAME': v(30),
                'OFFICE_LOC': v(30),
                'PHONE': v(15),
                'ISSUED_DATE': d,
                'DEFAULT_DIR': v(40),
                'DEFAULT_PRINT': v(40),
                'DEFAULT_DC_LOC': v(2),
                'DEFAULT_BRANCH': v(3),
                'NAME_SEARCH': v(1),
                'STAFF_SEC_TYPE': v(1),
                'STAFF_SECTION': v(8),
                'CREATE_DATE': d,
                'CREATE_USER': v(30),
                'UPDATE_DATE': d,
                'UPDATE_USER': v(30),
                'AD_USERNAME': v(30),
                'LCMS_POSITION': v(25),
                'CASE_TYPE': v(10),
                'ACTION_STAGE': v(10),
                'DR_USERNAME': v(30),
                'GUID': v(30)
            },
            'not_null': [
                'DISTRICT',
                'ID',
                'USERNAME',
                'INITIALS',
                'INIT_STAT',
                'LAST_NAME',
                'ISSUED_DATE',
                'DEFAULT_BRANCH',
                'STAFF_SEC_TYPE'
            ]
    }
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3].rstrip().lstrip()
            row['ID'] = line[3:13].rstrip().lstrip()
            row['USERNAME'] = line[13:31].rstrip().lstrip()
            row['INITIALS'] = line[31:39].rstrip().lstrip()
            row['INIT_STAT'] = line[39:40].rstrip().lstrip()
            row['STAFF_TITLE'] = line[40:43].rstrip().lstrip()
            row['SALUTATION'] = line[43:51].rstrip().lstrip()
            row['LAST_NAME'] = line[51:81].rstrip().lstrip()
            row['FIRST_NAME'] = line[81:111].rstrip().lstrip()
            row['OFFICE_LOC'] = line[111:141].rstrip().lstrip()
            row['PHONE'] = line[141:156].rstrip().lstrip()
            row['ISSUED_DATE'] = line[156:167].rstrip().lstrip()
            row['DEFAULT_DIR'] = line[167:207].rstrip().lstrip()
            row['DEFAULT_PRINT'] = line[207:247].rstrip().lstrip()
            row['DEFAULT_DC_LOC'] = line[247:249].rstrip().lstrip()
            row['DEFAULT_BRANCH'] = line[249:252].rstrip().lstrip()
            row['NAME_SEARCH'] = line[252:253].rstrip().lstrip()
            row['STAFF_SEC_TYPE'] = line[253:254].rstrip().lstrip()
            row['STAFF_SECTION'] = line[254:262].rstrip().lstrip()
            row['CREATE_DATE'] = line[262:273].rstrip().lstrip()
            row['CREATE_USER'] = line[273:303].rstrip().lstrip()
            row['UPDATE_DATE'] = line[303:314].rstrip().lstrip()
            row['UPDATE_USER'] = line[314:344].rstrip().lstrip()
            row['AD_USERNAME'] = line[344:374].rstrip().lstrip()
            row['LCMS_POSITION'] = line[374:399].rstrip().lstrip()
            row['CASE_TYPE'] = line[399:409].rstrip().lstrip()
            row['ACTION_STAGE'] = line[409:419].rstrip().lstrip()
            row['DR_USERNAME'] = line[419:449].rstrip().lstrip()
            row['GUID'] = line[449:479].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# Now, in disk24, there's a bunch of constant tables that need to be translated
# These tables all have codes and their meanings, which vary depending on district
def gs_action():
    global DIR
    filename = DIR + 'table_gs_action.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_agency_off():
    global DIR
    filename = DIR + 'table_gs_agency_off.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'AGENCY': 'GS_AGENCY(CODE)',
                'STATE': 'GS_STATE(CODE)'
            },
            'types': {
                'DISTRICT': v(8),
                'ID': v(11),
                'AGENCY': v(4),
                'OFFICE': v(60),
                'ADDRESS1': v(30),
                'ADDRESS2': v(30),
                'ADDRESS3': v(30),
                'CITY': v(20),
                'STATE': v(5),
                'ZIPCODE': v(10),
                'SALUTATION': v(10),
                'CHIEF_LAST_NAME': v(30),
                'CHIEF_FIRST_NAME': v(30),
                'CHIEF_TITLE': v(30),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'ID'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['ID'] = line[9:20].rstrip().lstrip()
            row['AGENCY'] = line[21:25].rstrip().lstrip()
            row['OFFICE'] = line[26:86].rstrip().lstrip()
            row['ADDRESS1'] = line[87:117].rstrip().lstrip()
            row['ADDRESS2'] = line[118:148].rstrip().lstrip()
            row['ADDRESS3'] = line[149:179].rstrip().lstrip()
            row['CITY'] = line[180:200].rstrip().lstrip()
            row['STATE'] = line[201:206].rstrip().lstrip()
            row['ZIPCODE'] = line[207:217].rstrip().lstrip()
            row['SALUTATION'] = line[218:228].rstrip().lstrip()
            row['CHIEF_LAST_NAME'] = line[229:259].rstrip().lstrip()
            row['CHIEF_FIRST_NAME'] = line[260:290].rstrip().lstrip()
            row['CHIEF_TITLE'] = line[291:321].rstrip().lstrip()
            row['CREATE_DATE'] = line[322:332].rstrip().lstrip()
            row['CREATE_USER'] = line[333:363].rstrip().lstrip()
            row['UPDATE_DATE'] = line[364:374].rstrip().lstrip()
            row['UPDATE_USER'] = line[375:405].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_business_type():
    global DIR
    filename = DIR + 'table_gs_business_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[114:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_type():
    global DIR
    filename = DIR + 'table_gs_case_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['TYPE'] = line[45:50].rstrip().lstrip()
            row['CODE_STAT'] = line[51:59].rstrip().lstrip()
            row['GLB_CODE'] = line[60:67].rstrip().lstrip()
            row['CREATE_DATE'] = line[68:78].rstrip().lstrip()
            row['CREATE_USER'] = line[79:109].rstrip().lstrip()
            row['UPDATE_DATE'] = line[110:120].rstrip().lstrip()
            row['UPDATE_USER'] = line[121:151].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_case_weight():
    global DIR
    filename = DIR + 'table_gs_case_weight.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_counsel_type():
    global DIR
    filename = DIR + 'table_gs_counsel_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:54].rstrip().lstrip()
            row['CODE_STAT'] = line[55:63].rstrip().lstrip()
            row['GLB_CODE'] = line[64:71].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:82].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:155].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_court_loc():
    global DIR
    filename = DIR + 'table_gs_court_loc.txt'
    data = []
    sql = {
            'primary': ['COURT', 'LOCATION', 'DISTRICT'],
            'foreign':{
                'COURT': 'GS_COURT(CODE)',
                'LOCATION, DISTRICT': 'GS_LOCATION(CODE, DISTRICT)',
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'COURT': v(4),
                'LOCATION': v(2),
                'DESCRIPTION': v(60),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'COURT',
                'LOCATION',
                'DISTRICT'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['COURT'] = line[9:11].rstrip().lstrip()
            row['LOCATION'] = line[12:14].rstrip().lstrip()
            row['DESCRIPTION'] = line[15:75].rstrip().lstrip()
            row['CREATE_DATE'] = line[76:86].rstrip().lstrip()
            row['CREATE_USER'] = line[878:117].rstrip().lstrip()
            row['UPDATE_DATE'] = line[118:128].rstrip().lstrip()
            row['UPDATE_USER'] = line[129:159].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_deten_reason():
    global DIR
    filename = DIR + 'table_gs_deten_reason.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

# this one's a little messed up
def gs_event_type():
    global DIR
    filename = DIR + 'table_gs_event_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE'
                #'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 6:
                count += 1
                continue

            if count % 0 != 0:
                continue

            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:84].rstrip().lstrip()
            row['TYPE'] = line[85:90].rstrip().lstrip()
            row['CODE_STAT'] = line[91:99].rstrip().lstrip()
            row['GLB_CODE'] = line[100:107].rstrip().lstrip()
            row['CREATE_DATE'] = line[108:118].rstrip().lstrip()
            row['CREATE_USER'] = line[119:149].rstrip().lstrip()
            row['UPDATE_DATE'] = line[150:160].rstrip().lstrip()
            #row['UPDATE_USER'] = line[].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_evid_disp():
    global DIR
    filename = DIR + 'table_gs_evid_disp.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:39].rstrip().lstrip()
            row['CODE_STAT'] = line[40:48].rstrip().lstrip()
            row['GLB_CODE'] = line[59:56].rstrip().lstrip()
            row['CREATE_DATE'] = line[57:67].rstrip().lstrip()
            row['CREATE_USER'] = line[68:98].rstrip().lstrip()
            row['UPDATE_DATE'] = line[99:109].rstrip().lstrip()
            row['UPDATE_USER'] = line[110:140].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_evid_location():
    global DIR
    filename = DIR + 'table_gs_evid_location.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_evid_type():
    global DIR
    filename = DIR + 'table_gs_evid_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:54].rstrip().lstrip()
            row['CODE_STAT'] = line[55:63].rstrip().lstrip()
            row['GLB_CODE'] = line[64:71].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:82].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:115].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_expert():
    global DIR
    filename = DIR + 'table_gs_expert.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'INIT_STAT': 'GS_INIT_STAT(CODE)',
                'TYPE, DISTRICT': 'GS_EXPERT_TYPE(CODE, DISTRICT)',
                'STATE': 'GS_STATE(CODE)'
            },
            'types': {
                'DISTRICT': v(8),
                'ID': n,
                'INITIALS': v(8),
                'INIT_STAT': v(8),
                'TYPE': v(4),
                'SSN': v(11),
                'SALUTATION': v(10),
                'LAST_NAME': v(30),
                'FIRST_NAME': v(30),
                'TITLE': v(20),
                'ADDRESS_1': v(30),
                'ADDRESS_2': v(30),
                'ADDRESS_3': v(30),
                'CITY': v(20),
                'STATE': v(5),
                'ZIPCODE': v(10),
                'PHONE': v(15),
                'FAX': v(15),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'ID',
                'DISTRICT'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['ID'] = line[9:20].rstrip().lstrip()
            row['INITIALS'] = line[21:29].rstrip().lstrip()
            row['INIT_STAT'] = line[30:38].rstrip().lstrip()
            row['TYPE'] = line[39:43].rstrip().lstrip()
            row['SSN'] = line[44:55].rstrip().lstrip()
            row['SALUTATION'] = line[56:66].rstrip().lstrip()
            row['LAST_NAME'] = line[67:97].rstrip().lstrip()
            row['FIRST_NAME'] = line[98:128].rstrip().lstrip()
            row['TITLE'] = line[129:149].rstrip().lstrip()
            row['ADDRESS_1'] = line[160:190].rstrip().lstrip()
            row['ADDRESS_2'] = line[191:221].rstrip().lstrip()
            row['ADDRESS_3'] = line[222:252].rstrip().lstrip()
            row['CITY'] = line[253:273].rstrip().lstrip()
            row['STATE'] = line[274:279].rstrip().lstrip()
            row['ZIPCODE'] = line[280:290].rstrip().lstrip()
            row['PHONE'] = line[291:306].rstrip().lstrip()
            row['FAX'] = line[307:322].rstrip().lstrip()
            row['CREATE_DATE'] = line[323:333].rstrip().lstrip()
            row['CREATE_USER'] = line[334:364].rstrip().lstrip()
            row['UPDATE_DATE'] = line[364:375].rstrip().lstrip()
            row['UPDATE_USER'] = line[376:406].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_expert_type():
    global DIR
    filename = DIR + 'table_gs_expert_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_immig_stat():
    global DIR
    filename = DIR + 'table_gs_immig_stat.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
    return (sql, data)

def gs_job_position():
    global DIR
    filename = DIR + 'table_gs_job_position.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_judge():
    global DIR
    filename = DIR + 'table_gs_judge.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'INIT_STAT': 'GS_INIT_STAT(CODE)',
                'TYPE, DISTRICT': 'GS_JUDGE_TYPE(CODE, DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'ID': n,
                'INITIALS': v(8),
                'INIT_STAT': v(4),
                'LAST_NAME': v(30),
                'FIRST_NAME': v(30),
                'COURT_ROOM': v(25),
                'TYPE': v(4),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [

            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            if 'GS_JUDGE' in line or 'Date:' in line:
                count = 0
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['ID'] = line[8:20].rstrip().lstrip()
            row['INITIALS'] = line[21:29].rstrip().lstrip()
            row['INIT_STAT'] = line[30:34].rstrip().lstrip()
            row['LAST_NAME'] = line[35:65].rstrip().lstrip()
            row['FIRST_NAME'] = line[66:96].rstrip().lstrip()
            row['COURT_ROOM'] = line[97:122].rstrip().lstrip()
            row['TYPE'] = line[123:127].rstrip().lstrip()
            row['CREATE_DATE'] = line[128:138].rstrip().lstrip()
            row['CREATE_USER'] = line[139:169].rstrip().lstrip()
            row['UPDATE_DATE'] = line[170:180].rstrip().lstrip()
            row['UPDATE_USER'] = line[181:211].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_judge_type():
    global DIR
    filename = DIR + 'table_gs_judge_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_lit_track():
    global DIR
    filename = DIR + 'table_gs_lit_track.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)


def gs_location():
    global DIR
    filename = DIR + 'table_gs_location.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_oppose_attorn():
    global DIR
    filename = DIR + 'table_gs_oppose_attorn.txt'
    data = []
    sql = {
            'primary': ['ID', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)',
                'INIT_STAT': 'GS_INIT_STAT(CODE)',
                'STATE': 'GS_STATE(CODE)'
            },
            'types': {
                'DISTRICT': v(10),
                'ID': n,
                'INITIALS': v(10),
                'INIT_STAT': v(10),
                'SALUTATION': v(10),
                'LAST_NAME': v(30),
                'FIRST_NAME': v(30),
                'TITLE': v(30),
                'FIRM': v(50),
                'ADDRESS1': v(30),
                'ADDRESS2': v(30),
                'ADDRESS3': v(30),
                'CITY': v(20),
                'STATE': v(5),
                'ZIPCODE': v(10),
                'PHONE': v(15),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            if 'GS_OPPOSE_ATTORN' in line or 'Date:' in line:
                count = 0
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['ID'] = line[9:20].rstrip().lstrip()
            row['INITIALS'] = line[21:31].rstrip().lstrip()
            row['INIT_STAT'] = line[32:40].rstrip().lstrip()
            row['SALUTATION'] = line[41:51].rstrip().lstrip()
            row['LAST_NAME'] = line[52:82].rstrip().lstrip()
            row['FIRST_NAME'] = line[83:113].rstrip().lstrip()
            row['TITLE'] = line[114:144].rstrip().lstrip()
            row['FIRM'] = line[145:195].rstrip().lstrip()
            row['ADDRESS1'] = line[196:226].rstrip().lstrip()
            row['ADDRESS2'] = line[227:257].rstrip().lstrip()
            row['ADDRESS3'] = line[258:288].rstrip().lstrip()
            row['CITY'] = line[289:309].rstrip().lstrip()
            row['STATE'] = line[310:315].rstrip().lstrip()
            row['ZIPCODE'] = line[316:326].rstrip().lstrip()
            row['PHONE'] = line[327:342].rstrip().lstrip()
            row['FAX'] = line[343:358].rstrip().lstrip()
            row['CREATE_DATE'] = line[359:369].rstrip().lstrip()
            row['CREATE_USER'] = line[370:400].rstrip().lstrip()
            row['UPDATE_DATE'] = line[401:411].rstrip().lstrip()
            row['UPDATE_USER'] = line[412:442].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_position():
    global DIR
    filename = DIR + 'table_gs_position.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_prop_type():
    global DIR
    filename = DIR + 'table_gs_prop_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_prop_value_type():
    global DIR
    filename = DIR + 'table_gs_prop_value_type.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(50),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:64].rstrip().lstrip()
            row['CODE_STAT'] = line[65:73].rstrip().lstrip()
            row['GLB_CODE'] = line[74:81].rstrip().lstrip()
            row['CREATE_DATE'] = line[82:92].rstrip().lstrip()
            row['CREATE_USER'] = line[93:123].rstrip().lstrip()
            row['UPDATE_DATE'] = line[124:134].rstrip().lstrip()
            row['UPDATE_USER'] = line[135:165].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relate_case_reason():
    global DIR
    filename = DIR + 'table_gs_relate_case_reason.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(50),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:64].rstrip().lstrip()
            row['CODE_STAT'] = line[65:73].rstrip().lstrip()
            row['GLB_CODE'] = line[74:81].rstrip().lstrip()
            row['CREATE_DATE'] = line[82:92].rstrip().lstrip()
            row['CREATE_USER'] = line[93:123].rstrip().lstrip()
            row['UPDATE_DATE'] = line[124:134].rstrip().lstrip()
            row['UPDATE_USER'] = line[135:165].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_relate_part_reason():
    global DIR
    filename = DIR + 'table_gs_relate_part_reason.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(30),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:44].rstrip().lstrip()
            row['CODE_STAT'] = line[45:53].rstrip().lstrip()
            row['GLB_CODE'] = line[54:61].rstrip().lstrip()
            row['CREATE_DATE'] = line[62:72].rstrip().lstrip()
            row['CREATE_USER'] = line[73:103].rstrip().lstrip()
            row['UPDATE_DATE'] = line[104:114].rstrip().lstrip()
            row['UPDATE_USER'] = line[115:145].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_reservation():
    global DIR
    filename = DIR + 'table_gs_reservation.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(40),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:54].rstrip().lstrip()
            row['CODE_STAT'] = line[55:63].rstrip().lstrip()
            row['GLB_CODE'] = line[64:71].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:82].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:155].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_security():
    global DIR
    filename = DIR + 'table_gs_security.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(40),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:54].rstrip().lstrip()
            row['CODE_STAT'] = line[55:63].rstrip().lstrip()
            row['GLB_CODE'] = line[64:71].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:82].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:155].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_staff_section():
    global DIR
    filename = DIR + 'table_gs_staff_section.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(8),
                'DESCRIPTION': v(50),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }

    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:17].rstrip().lstrip()
            row['DESCRIPTION'] = line[18:68].rstrip().lstrip()
            row['CODE_STAT'] = line[69:77].rstrip().lstrip()
            row['GLB_CODE'] = line[78:85].rstrip().lstrip()
            row['CREATE_DATE'] = line[86:96].rstrip().lstrip()
            row['CREATE_USER'] = line[97:127].rstrip().lstrip()
            row['UPDATE_DATE'] = line[128:138].rstrip().lstrip()
            row['UPDATE_USER'] = line[139:169].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_staff_title():
    global DIR
    filename = DIR + 'table_gs_staff_title.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(50),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:64].rstrip().lstrip()
            row['CODE_STAT'] = line[65:73].rstrip().lstrip()
            row['GLB_CODE'] = line[74:81].rstrip().lstrip()
            row['CREATE_DATE'] = line[82:92].rstrip().lstrip()
            row['CREATE_USER'] = line[93:123].rstrip().lstrip()
            row['UPDATE_DATE'] = line[124:134].rstrip().lstrip()
            row['UPDATE_USER'] = line[135:165].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def gs_unit():
    global DIR
    filename = DIR + 'table_gs_unit.txt'
    data = []
    sql = {
            'primary': ['CODE', 'DISTRICT'],
            'foreign':{
                'DISTRICT': 'GS_DISTRICT(DISTRICT)'
            },
            'types': {
                'DISTRICT': v(8),
                'CODE': v(4),
                'DESCRIPTION': v(40),
                'CODE_STAT': v(8),
                'GLB_CODE': v(7),
                'CREATE_DATE':'DATE',
                'CREATE_USER':'VARCHAR(30)',
                'UPDATE_DATE':'DATE',
                'UPDATE_USER':'VARCHAR(30)'
            },
            'not_null': [
                'DISTRICT',
                'CODE'
            ]
    }
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4 or len(line) == 0 or len(line) == 1 or 'rows' in line:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8].rstrip().lstrip()
            row['CODE'] = line[9:13].rstrip().lstrip()
            row['DESCRIPTION'] = line[14:54].rstrip().lstrip()
            row['CODE_STAT'] = line[55:63].rstrip().lstrip()
            row['GLB_CODE'] = line[64:71].rstrip().lstrip()
            row['CREATE_DATE'] = line[72:82].rstrip().lstrip()
            row['CREATE_USER'] = line[83:113].rstrip().lstrip()
            row['UPDATE_DATE'] = line[114:124].rstrip().lstrip()
            row['UPDATE_USER'] = line[125:155].rstrip().lstrip()
            data.append(row)
    return (sql, data)

def find_indices(line):
    return [(m.start(), m.end()) for m in re.finditer(r'\S+', line)]

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()

# Last thing is the stuff in lions global_LIONS.txt
def parse_global_LIONS():
    global DIR
    filename = DIR + 'global_LIONS.txt'
    datasets = {}
    data = []
    sql_tables = {
            'GS_ADR_MODE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(40),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_AGENCY_MASTER': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_AGENCY': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'STATUS': v(6),
                    'ABBREV': v(10),
                    'MASTER_CODE': v(10),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_APPEAL_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_AUDIT_FUNCTION': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            }, # NOT DONE
            'GS_BOND_TYPE':{
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CASE_CLASS': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CASE_STATUS': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(15),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CAUSE_ACT_MASTER': {
                'primary': ['MASTER_CODE'],
                'foreign':{},
                'types': {
                    'MASTER_CODE': v(4),
                    'DESCRIPTION': v(35),
                    'STATUS': v(6),
                    'BEGIN_DATE': d,
                    'END_DATE': d,
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CAUSE_ACT': {
                'primary': ['CODE'],
                'foreign':{
                    'MASTER_CODE': 'GS_CAUSE_ACT_MASTER(MASTER_CODE)'
                },
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(76),
                    'STATUS': v(6),
                    'MASTER_CODE': v(10),
                    'BEGIN_DATE': d,
                    'END_DATE': d,
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CHARGE_CAT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CHARGE_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(25),
                    'DESCRIPTION': v(70),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CIVIL_POTEN': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_COLLECT_IND': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_COMMENT_CAT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_CONTROL_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(40),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_COUNTRY_CIT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_COURT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(40),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_DEFEND_STAT_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(50),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_DISP_REAS_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'TYPE': v(5),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_DISP_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'TYPE': v(5),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_DOJ_DIVISION':{
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(50),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            } ,
            'GS_DOM_TERR_IND': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_EMPLOYER_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(60),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_EXPERT_SIDE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(15),
                    'CODE_STAT': v(8),
                    'GLB_CODE': v(7),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_GENDER': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_GUIDE_DEPART': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(60),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_HCARE_BUSN_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(60),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_INCAR_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_INITIATOR': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_INIT_STAT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_INST_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(35),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_LIT_RESP': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(60),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_MEASURE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_OCCUPATION': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(60),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_PART_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_PENALTY_PROVISION': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(25),
                    'DESCRIPTION': v(70),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_PRIORITY': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(25),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_PROG_CAT_MASTER': {
                'primary': ['MASTER_CODE'],
                'foreign':{},
                'types': {
                    'MASTER_CODE': v(4),
                    'DESCRIPTION': v(50),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_PROG_CAT': {
                'primary': ['CODE'],
                'foreign':{
                    'MASTER_CODE': 'GS_PROG_CAT_MASTER(MASTER_CODE)'
                },
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'STATUS': v(6),
                    'MASTER_CODE': v(10),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_RACE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_RELIEF_LIABILITY': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_RELIEF_REQUESTED_BY': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_RELIEF_STAGE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_RELIEF_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_REST_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_REST_RECIPIENT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_ROLE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(40),
                    'TYPE': v(5),
                    'PART_TYPE': v(8),
                    'STATUS': v(6),
                    'DISPOSE': v(7),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_ROLLUP': {
                'primary': ['DISP', 'DISP_REAS'],
                'foreign':{
                    'DISP': 'GS_DISP_TYPE(CODE)',
                    'DISP_REAS': 'GS_DISP_REAS_TYPE(CODE)'
                },
                'types': {
                    'DISP': v(4),
                    'DISP_REAS': v(8),
                    'CRIM_ORDER': v(10),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'DISP',
                    'DISP_REAS'
                ]
            },
            'GS_SPECIAL_CONDITION': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_SPEC_PROJ': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(30),
                    'TYPE': v(5),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_SPECIAL_SERVICES': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(75),
                    'STATUS': v(6),
                    'GLB_CODE': v(7),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_STATE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_STORAGE_ITEM_NO': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_TERM_REASON': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(20),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_TRIBE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(70),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_TYPE_OF_ACTION_MAP': {
                'primary': ['CODE1', 'CODE2'],
                'foreign':{},
                'types': {
                    'CODE1': v(6),
                    'CODE2': v(5),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_US_ROLE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(35),
                    'TYPE': v(5),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_VICTIM_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_VICTIM_UNIT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_VICTIM_WIT': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(11),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            },
            'GS_DISTRICT': {
                'primary': ['DISTRICT'],
                'foreign':{},
                'types': {
                    'DISTRICT': v(8),
                    'DESCRIPTION': v(50),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'DISTRICT'
                ]
            },
            'GS_ORDER_TYPE': {
                'primary': ['CODE'],
                'foreign':{},
                'types': {
                    'CODE': v(4),
                    'DESCRIPTION': v(140),
                    'STATUS': v(6),
                    'CREATE_DATE':'DATE',
                    'CREATE_USER':'VARCHAR(30)',
                    'UPDATE_DATE':'DATE',
                    'UPDATE_USER':'VARCHAR(30)'
                },
                'not_null': [
                    'CODE'
                ]
            }

    }
    count = 0
    with open(filename) as file:
        current_table = ""
        indices = []
        fields = []
        for line in file:
            if len(line) < 2:
                continue
            if "GS_" in line:
                if len(data) > 0:
                    datasets[current_table] = (sql_tables[current_table], data)
                    data = []
                    indices = []
                current_table = line[:-1].rstrip().lstrip()
                count = 0

            if count < 3:
                if "CreateDate" in line:
                    fields_bad = line.split()
                    fields = [convert(f) for f in fields_bad]
                    #print(fields)
                if "--" in line:
                    indices = find_indices(line)
                    #print(indices)
                count += 1
                continue
            row = {}
            for i in range(len(fields)):
                row[fields[i]] = line[indices[i][0]:indices[i][1]].rstrip().lstrip()
            data.append(row)
    return datasets

def create_complete_lions_dictionary():
    lions = {}
    lions['GS_ALSO_KNOWN'] = gs_also_known()
    lions['GS_ARCHIVE_CASE'] = gs_archive_case()
    return lions

if __name__ == '__main__':
    lions = create_complete_lions_dictionary()

