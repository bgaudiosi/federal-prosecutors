# CS506 Federal Prosecutor Project
# Justin, Ben, Hao
#
# Preliminary code to parse through the .txt files and extract certain fields.
# Primarily using this file to explore the various data.
import sys
import numpy as np
import pandas as pd

DIR = "/Volumes/ESD-USB/"

# Parse DISK01
def gs_also_known():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_also_known.txt'
    columns = ["DISTRICT", "CASEID", "PARTID", "ID", "LAST_NAME", "FIRST_NAME", "LAST_SOUNDS", "FIRST_SOUNDS", "CREATE_DATE", "CREATE_USER", "UPDATE_DATE", "UPDATE_USER"]
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASE_ID'] = line[10:20]
            row['PART_ID'] = line[20:30]
            row['ID'] = line[30:40]
            row['LAST_NAME'] = line[40:100]
            row['FIRST_NAME'] = line[100:130]
            row['LAST_SOUNDS'] = line[130:134]
            row['FIRST_SOUNDS'] = line[134:138]
            row['CREATE_DATE'] = line[138:149]
            row['CREATE_USER'] = line[149:179]
            row['UPDATE_DATE'] = line[179:190]
            row['UPDATE_USER'] = line[190:220]
            data.append(row)
    return data

def gs_archive_case():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_archive_case.txt'
    columns = ['DISTRICT','ID']
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['ID'] = line[10:20]
            row['CLASS'] = line[20:21]
            row['NAME'] = line[21:71]
            row['RECVD_DATE'] = line[71:82]
            row['US_ROLE'] = line[82:84]
            row['LEAD_CHARGE'] = line[84:109]
            row['PROG_CAT'] = line[109:112]
            row['CAUSE_ACT'] = line[112:116]
            row['BRANCH'] = line[116:119]
            row['COMMENTS'] = line[119:179]
            row['COURT'] = line[179:181]
            row['LOCATION'] = line[181:183]
            row['COURT_NUMBER'] = line[183:208]
            row['FILING_DATE'] = line[208:219]
            row['SERVICE_DATE'] = line[219:230]
            row['DISPOSITION'] = line[230:232]
            row['DISP_REASON'] = line[232:236]
            row['DISP_DATE'] = line[236:247]
            row['INST_TYPE'] = line[247:249]
            row['INST_FILE_DATE'] = line[249:260]
            row['AUSA_LAST_NAME'] = line[260:290]
            row['AUSA_FIRST_NAME'] = line[290:320]
            row['AGENCY'] = line[320:324]
            row['APPEALS_FILED'] = line[324:335]
            row['STORE_NUM'] = line[334:355]
            row['DEST_DATE'] = line[355:366]
            row['CREATE_DATE'] = line[366:377]
            row['CREATE_USER'] = line[377:407]
            row['UPDATE_DATE'] = line[407:418]
            row['UDPATE_USER'] = line[418:448]
            data.append(row)
    return data


def gs_archive_part():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_archive_part.txt'
    columns = []
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT']
            row['CASEID']
            row['ID']
            row['LAST_NAME']
            row['FIRST_NAME']
            row['LAST_SOUNDS']
            row['FIRST_SOUNDS']
            row['ROLE']
            row['DISPOSITION']
            row['DISP_REASON']
            row['DISP_DATE']
            row['CREATE_DATE']
            row['CREATE_USER']
            row['UPDATE_DATE']
            row['UPDATE_USER']
            data.append(row)
    return data

def gs_case():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_case.txt'
    columns = ["DISTRICT", "ID", "CLASS", "NAME"]
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3]
            row['ID'] = line[3:13]
            row['CLASS'] = line[13:14]
            row['NAME'] = line[14:64]
            row['RECVD_DATE'] = line[64:75] # convert to datetime
            row['SECURITY'] = line[75:76]
            row['PRIORITY'] = line[76:77]
            row['TYPE'] = line[77:81]
            row['US_ROLE'] = line[81:83]
            row['LIT_RESP'] = line[83:85]
            row['LIT_TRACK'] = line[85:86]
            row['WEIGHT'] = line[86:88]
            row['BRANCH'] = line[88:91]
            row['GRAND_JURY_NUM'] = line[91:106]
            row['UNIT'] = line[106:110]
            row['DCMNS_NUMBER'] = line[110:121]
            row['TRIBE'] = line[121:125]
            row['RESERVATION'] = line[125:129]
            row['SPEC_PROJ'] = line[129:131]
            row['VIC_WIT'] = line[131:132]
            row['ADR_MODE'] = line[132:134]
            row['COLLECT_IND'] = line[134:135]
            row['OFFENSE_FROM'] = line[135:146]
            row['OFFENSE_TO'] = line[146:157]
            row['LEAD_CHARGE'] = line[157:182]
            row['PHYSICAL_LOC'] = line[182:202]
            row['STORE_NUM'] = line[202:222]
            row['CIVIL_POTEN'] = line[222:223]
            row['SYS_INIT_DATE'] = line[223:234]
            row['ACCESS_DATE'] = line[234:245]
            row['STATUS'] = line[245:246]
            row['CLOSE_DATE'] = line[246:257]
            row['DEST_DATE'] = line[257:268]
            row['PERMANENT'] = line[268:269]
            row['CASE_RESTRICTED'] = line[269:270]
            row['CRIMINAL_POTEN'] = line[270:271]
            row['TOT_VICTIMS'] = line[271:282]
            row['RELATED_FLU_FLAG'] = line[282:283]
            row['QUI_TAM'] = line[283:284]
            row['CREATE_DATE'] = line[284:295]
            row['CREATE_USER'] = line[295:235]
            row['UPDATE_DATE'] = line[325:336]
            row['UPDATE_USER'] = line[336:337]
            data.append(row)
    return data

def gs_case_cause_act():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_case_cause_act.txt'
    columns = []
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['CAUSE_ACT'] = line[20:24]
            row['ID'] = line[24:34]
            row['CREATE_DATE'] = line[34:45]
            row['CREATE_USER'] = line[45:75]
            row['UPDATE_DATE'] = line[75:86]
            row['UPDATE_USER'] = line[86:116]
            data.append(row)
    return data

def gs_case_doj_div():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_case_doj_div.txt'
    columns = []
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['DOJ_DIV'] = line[30:34]
            row['DOJ_NUMBER'] = line[34:59]
            row['CREATE_DATE'] = line[59:70]
            row['CREATE_USER'] = line[70:100]
            row['UPDATE_DATE'] = line[100:111]
            row['UPDATE_USER'] = line[11:141]
            data.append(row)
    return data

def gs_case_dom_terr_ind():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_case_dom_terr_ind.txt'
    columns = []
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['ID'] = line[10:20]
            row['CASEID'] = line[20:30]
            row['DOM_TERR_IND'] = line[30:32]
            row['CREATE_DATE'] = line[32:43]
            row['CREATE_USER'] = line[43:73]
            row['UPDATE_DATE'] = line[73:84]
            row['UPDATE_USER'] = line[84:114]
            data.append(row)
    return data

def gs_case_prog_cat():
    global DIR
    disk = "DISK01"
    filename = DIR + disk + '/gs_case_prog_cat.txt'
    columns = []
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PROG_CAT'] = line[20:23]
            row['ID'] = line[23:33]
            row['CREATE_DATE'] = line[33:44]
            row['CREATE_USER'] = line[44:74]
            row['UPDATE_DATE'] = line[74:85]
            row['UPDATE_USER'] = line[85:115]
            data.append(row)
    return data

def find_Info():
    """Extracts fields from the LIONS database for testing purposes"""

    # Replace this string with the path to your data
    fileName = "E:/CS506DataDump/ProjectDump/FY2018/DISK01/gs_case.txt"
    case_file = open(fileName, 'r')

    cap = 100
    d = {}
    count = 0

    for line in case_file:
        # Field value (change the slice based on the README)
        val = line[157:182]
        if val in d:
            d[val] += 1
        else:
            d[val] = 1


        # Utilities
        count += 1
        if (count % 100000 == 0):
            print("Reached iteration " + str(count))
        # Comment out the below lines to not use a cap and go through whole file
        cap -= 1
        if cap == 0:
            break

    print(d)
    print("Number of lines: " + str(count))
    print("Number of keys: " + str(len(d)))


if __name__ == '__main__':
    case = gs_case()
    archive_case = gs_archive_case()
    districts = [d['DISTRICT'] for d in archive_case]
    print(case[0])
    print(archive_case[0])
    print("Length of gs_case:", len(case))
    print("Length of gs_archive_case:", len(archive_case))
    print(set(districts))

