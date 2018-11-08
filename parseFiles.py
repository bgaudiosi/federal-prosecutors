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

# Parse DISK02
def gs_case_special_proj():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_case_special_proj.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['ID'] = line[10:20]
            row['CASEID'] = line[20:30]
            row['SPECIAL_PROJ'] = line[30:32]
            row['CREATE_DATE'] = line[32:43]
            row['CREATE_USER'] = line[43:73]
            row['UPDATE_DATE'] = line[73:84]
            row['UPDATE_USER'] = line[84:114]
            data.append(row)
    return data

def gs_evidence():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_evidence.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['LOCATION'] = line[30:34]
            row['TYPE'] = line[34:36]
            row['DISPOSITION'] = line[36:37]
            row['STORE_DATE'] = line[37:48]
            row['DISP_DATE'] = line[48:59]
            row['DC_EXHIBIT_NUM'] = line[59:84]
            row['GJ_EXHIBIT_NUM'] = line[84:109]
            row['CREATE_DATE'] = line[109:120]
            row['CREATE_USER'] = line[120:150]
            row['UPDATED_DATE'] = line[150:161]
            row['UPDATE_USER'] = line[161:191]
            data.append(row)
    return data

def gs_expert_case():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_expert_case.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['EXP_SIDE'] = line[30:31]
            row['EXPERTID'] = line[31:41]
            row['CREATE_DATE'] = line[41:52]
            row['CREATE_USER'] = line[52:82]
            row['UPDATED_DATE'] = line[82:93]
            row['UPDATE_USER'] = line[93:123]
            data.append(row)
    return data

def gs_inst_charge():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_inst_charge.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['CRTHISID'] = line[20:30]
            row['INSTID'] = line[30:40]
            row['CHARGE'] = line[40:65]
            row['CATEGORY'] = line[65:66]
            row['PENT_PROV'] = line[66:91]
            row['CREATE_DATE'] = line[91:102]
            row['CREATE_USER'] = line[102:132]
            row['UPDATED_DATE'] = line[132:143]
            row['UPDATE_USER'] = line[143:173]
            row['ID'] = line[173:183]
            data.append(row)
    return data

def gs_part_victim():
    global dir
    disk = "disk02"
    filename = dir + disk + '/gs_part_victim.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['VICTIM_TYPE'] = line[40:41]
            row['PROSECUTION'] = line[41:42]
            row['VICTIM_TIMES'] = line[43:53]
            row['THREATS'] = line[53:54]
            row['ELDERLY'] = line[54:55]
            row['VICTIM_IDENTIFIER'] = line[55:80]
            row['STATE_COMP_RECVD'] = line[80:94]
            row['SERVICES_REQUESTED'] = line[94:95]
            row['VIOLENT_CRIME'] = line[95:96]
            row['DISABILITY'] = line[96:97]
            row['NOTIFICAT_REQSTD'] = line[97:98]
            row['NOTIFICAT_RECVD'] = line[98:99]
            row['CREATE_DATE'] = line[99:110]
            row['CREATE_USER'] = line[110:140]
            row['UPDATED_DATE'] = line[140:151]
            row['UPDATE_USER'] = line[151:181]
            data.append(row)
    return data

def gs_relate_case():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_relate_case.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID1'] = line[10:20]
            row['CASEID2'] = line[20:30]
            row['CRTHISD1'] = line[30:40]
            row['CRTHISD2'] = line[40:50]
            row['REASON'] = line[50:52]
            row['CREATE_DATE'] = line[52:63]
            row['CREATE_USER'] = line[63:93]
            row['UPDATED_DATE'] = line[93:104]
            row['UPDATE_USER'] = line[104:134]
            row['ID'] = line[134:144]
            data.append(row)
    return data

def gs_relate_part():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_relate_part.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID1'] = line[20:30]
            row['PARTID2'] = line[30:40]
            row['REASON'] = line[40:42]
            row['CREATE_DATE'] = line[42:53]
            row['CREATE_USER'] = line[53:83]
            row['UPDATED_DATE'] = line[83:94]
            row['UPDATE_USER'] = line[94:125]
            data.append(row)
    return data

def gs_cont_services():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_cont_services.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['CONTID'] = line[30:40]
            row['ID'] = line[40:50]
            row['SERV_AGENCY'] = line[50:61]
            row['SERV_TYPE'] = line[61:65]
            row['SERV_LANGUAGE'] = line[65:68]
            row['SERV_SPECIAL'] = line[68:72]
            row['CREATE_DATE'] = line[72:83]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[113:124]
            row['UPDATE_USER'] = line[124:154]
            data.append(row)
    return data

def gs_contact_log():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_contact_log.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['CONT_DATE'] = line[40:51]
            row['PURPOSE'] = line[51:53]
            row['TYPE'] = line[53:55]
            row['INITIATOR'] = line[55:57]
            row['STAFFID'] = line[57:67]
            row['DOC_CODE'] = line[67:70]
            row['CREATE_DATE'] = line[70:81]
            row['CREATE_USER'] = line[81:111]
            row['UPDATED_DATE'] = line[111:122]
            row['UPDATE_USER'] = line[122:152]
            data.append(row)
    return data

def gs_control_sub():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_control_sub.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['TYPE'] = line[30:31]
            row['QUANTITY'] = line[31:45]
            row['MEASURE'] = line[45:46]
            row['OTHER_DESCRIP'] = line[46:76]
            row['CREATE_DATE'] = line[76:87]
            row['CREATE_USER'] = line[87:117]
            row['UPDATED_DATE'] = line[117:128]
            row['UPDATE_USER'] = line[128:158]
            data.append(row)
    return data

def gs_count():
    global DIR
    disk = "DISK02"
    filename = DIR + disk + '/gs_count.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['TYPE'] = line[30:31]
            row['QUANTITY'] = line[31:45]
            row['MEASURE'] = line[45:46]
            row['OTHER_DESCRIP'] = line[46:76]
            row['CREATE_DATE'] = line[76:87]
            row['CREATE_USER'] = line[87:117]
            row['UPDATED_DATE'] = line[117:128]
            row['UPDATE_USER'] = line[128:158]
            row['PENT_PROV'] = line[158:183]
            data.append(row)
    return data

# Parse DISK03
def gs_court_hist():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_court_hist.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['COURT'] = line[30:32]
            row['LOCATION'] = line[32:34]
            row['US_ROLE'] = line[34:36]
            row['COURT_NUMBER'] = line[36:61]
            row['FILING_DATE'] = line[61:72]
            row['SERVICE_DATE'] = line[72:83]
            row['TRIAL_DAYS'] = line[83:97]
            row['NOAP_DATE'] = line[97:108]
            row['APPEAL_TYPE'] = line[108:109]
            row['SENT_APPEAL'] = line[109:110]
            row['DISPOSITION'] = line[100:112]
            row['DISP_DATE'] = line[112:123]
            row['DISP_REASON1'] = line[123:127]
            row['DISP_REASON2'] = line[127:131]
            row['DISP_REASON3'] = line[131:135]
            row['SYS_DISP_DATE'] = line[135:146]
            row['SYS_FILING_DATE'] = line[146:157]
            row['CREATE_DATE'] = line[157:168]
            row['CREATE_USER'] = line[168:198]
            row['UPDATED_DATE'] = line[198:209]
            row['UPDATE_USER'] = line[209:239]
            data.append(row)
    return data

def gs_court_judge():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_court_judge.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['CRTHISID'] = line[20:30]
            row['ID'] = line[30:40]
            row['JUDGEID'] = line[40:50]
            row['DECISION'] = line[50:54]
            row['START_DATE'] = line[54:65]
            row['END_DATE'] = line[65:76]
            row['CREATE_DATE'] = line[76:87]
            row['CREATE_USER'] = line[87:117]
            row['UPDATED_DATE'] = line[117:128]
            row['UPDATE_USER'] = line[128:158]
            data.append(row)
    return data

def gs_dna():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_dna.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3]
            row['ID'] = line[3:13]
            row['CASEID'] = line[13:23]
            row['PROCEEDINGS_AFT_RELIEF_GRANTED'] = line[23:24]
            row['NEW_TRIAL_ORD'] = line[24:25]
            row['CHARGE_DISMISSED'] = line[25:26]
            row['GUILTY_PLEA_ENTERED'] = line[26:27]
            row['FOUND_GUILTY'] = line[27:28]
            row['ACQUITTED'] = line[28:29]
            row['RESENTENCING_CAP_CASE'] = line[29:30]
            row['TESTING_ORDERED'] = line[30:31]
            row['RELIEF_GRANTED'] = line[31:32]
            row['COMMENTS'] = line[32:33]
            row['CREATE_DATE'] = line[33:44]
            row['CREATE_USER'] = line[44:74]
            row['UPDATED_DATE'] = line[74:85]
            row['UPDATE_USER'] = line[85:115]
            data.append(row)
    return data

def gs_prop_value():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_prop_value.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['TYPE'] = line[40:42]
            row['VALUE'] = line[42:56]
            row['PROP_DATE'] = line[56:67]
            row['CREATE_DATE'] = line[67:78]
            row['CREATE_USER'] = line[78:108]
            row['UPDATED_DATE'] = line[108:119]
            row['UPDATE_USER'] = line[119:149]
            data.append(row)
    return data

def gs_region():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_region.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3]
            row['BRANCH'] = line[3:6]
            row['DESCRIPTION'] = line[6:36]
            row['CREATE_DATE'] = line[36:47]
            row['CREATE_USER'] = line[47:77]
            row['UPDATED_DATE'] = line[77:88]
            row['UPDATE_USER'] = line[88:118]
            data.append(row)
    return data

def gs_relate_appeal():
    global DIR
    disk = "DISK03"
    filename = DIR + disk + '/gs_relate_appeal.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID1'] = line[0:20]
            row['CRTHISID1'] = line[20:30]
            row['CASEID2'] = line[30:40]
            row['CRTHISID2'] = line[40:50]
            row['REASON'] = line[50:52]
            row['CREATE_DATE'] = line[52:63]
            row['CREATE_USER'] = line[63:93]
            row['UPDATED_DATE'] = line[93:104]
            row['UPDATE_USER'] = line[104:134]
            data.append(row)
    return data

# DISK04

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

