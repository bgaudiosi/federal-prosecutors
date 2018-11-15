# CS506 Federal Prosecutor Project
# Justin, Ben, Hao
#
# Preliminary code to parse through the .txt files and extract certain fields.
# Primarily using this file to explore the various data.
import sys
import re
from itertools import groupby

DIR = "data/"

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
    filename = DIR + 'gs_archive_case.txt'
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
    filename = DIR + 'gs_archive_part.txt'
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
    filename = DIR + 'gs_case.txt'
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
    filename = DIR + 'gs_case_cause_act.txt'
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
    filename = DIR + 'gs_case_doj_div.txt'
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
    filename = DIR + 'gs_case_dom_terr_ind.txt'
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
    filename = DIR + 'gs_case_prog_cat.txt'
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
    filename = DIR + 'gs_case_special_proj.txt'
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
    filename = DIR + 'gs_evidence.txt'
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
    filename = DIR + 'gs_expert_case.txt'
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
    filename = DIR + 'gs_inst_charge.txt'
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
    global DIR
    filename = DIR + 'gs_part_victim.txt'
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
    filename = DIR + 'gs_relate_case.txt'
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
    filename = DIR + 'gs_relate_part.txt'
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
    filename = DIR + 'gs_cont_services.txt'
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
    filename = DIR + 'gs_contact_log.txt'
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
    filename = DIR + 'gs_control_sub.txt'
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
    filename = DIR + 'gs_count.txt'
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
    filename = DIR + 'gs_court_hist.txt'
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
    filename = DIR + 'gs_court_judge.txt'
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
    filename = DIR + 'gs_dna.txt'
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
    filename = DIR + 'gs_prop_value.txt'
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
    filename = DIR + 'gs_region.txt'
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
    filename = DIR + 'gs_relate_appeal.txt'
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
def gs_sentence():
    global DIR
    filename = DIR + 'gs_sentence.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['SENT_DATE'] = line[30:41]
            row['GUIDE_DEPART'] = line[41:42]
            row['INCAR_TYPE'] = line[42:45]
            row['JUDGEID'] = line[45:55]
            row['PROB_DAYS'] = line[55:66]
            row['PROB_MONTHS'] = line[66:77]
            row['PROB_YEARS'] = line[77:88]
            row['SUPER_REL_DAYS'] = line[88:99]
            row['SUPER_REL_MONTHS'] = line[99:110]
            row['SUPER_REL_YEARS'] = line[110:121]
            row['INCAR_DAYS'] = line[121:132]
            row['INCAR_MONTHS'] = line[132:143]
            row['INCAR_YEARS'] = line[143:154]
            row['FINE'] = line[154:168]
            row['SPEC_ASSESSMENT'] = line[168:182]
            row['DEBARRED'] = line[182:183]
            row['SPEC_CONDITION'] = line[183:187]
            row['PROBATION_REVOKED'] = line[187:188]
            row['SUPER_REL_REVOKED'] = line[188:189]
            row['TOTAL_REVOKED_DAYS'] = line[189:200]
            row['TOTAL_REVOKED_MONTHS'] = line[200:211]
            row['TOTAL_REVOKED_YEARS'] = line[211:222]
            row['RELATED_FLU_USAO'] = line[222:232]
            row['RELATED_FLU_SEQ'] = line[232:235]
            row['COMM_SERV_HOURS'] = line[235:247]
            row['SYS_SENT_DATE'] = line[257:258]
            row['RESTITUTION_AMT'] = line[258:274]
            row['CREATE_DATE'] = line[274:285]
            row['CREATE_USER'] = line[285:315]
            row['UPDATED_DATE'] = line[315:326]
            row['UPDATE_USER'] = line[326:356]
            row['SUPV_REL_INCAR_TYPE'] = line[356:357]
            data.append(row)
    return data

# they split it up by district
def gs_event():
    global DIR

    districts = get_district_list()

    data = []
    for district in districts:
        filename = DIR + 'gs_event_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10]
                row['CASEID'] = line[10:20]
                row['CRTHISID'] = line[20:30]
                row['ID'] = line[30:40]
                row['TYPE'] = line[40:44]
                row['ACTION'] = line[44:46]
                row['EVENT_DATE'] = line[46:47]
                row['SCHED_DATE'] = line[47:68]
                row['SCHED_TIME'] = line[68:79]
                row['SCHED_LOC'] = line[79:279]
                row['STAFFID'] = line[279:289]
                row['JUDGEID'] = line[289:299]
                row['DOCUMENT_CODE'] = line[299:302]
                row['DOCUMENT_STAFFID'] = line[302:312]
                row['DOCUMENT_DATE'] = line[312:323]
                row['CREATE_DATE'] = line[323:334]
                row['CREATE_USER'] = line[334:364]
                row['UPDATED_DATE'] = line[364:375]
                row['UPDATE_USER'] = line[375:405]
                data.append(row)
    return data


def gs_oppose_coun():
    global DIR
    filename = DIR + 'gs_oppose_coun.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['ATTORNEYID'] = line[40:50]
            row['TYPE'] = line[50:52]
            row['START_DATE'] = line[52:63]
            row['END_DATE'] = line[63:74]
            row['CREATE_DATE'] = line[74:85]
            row['CREATE_USER'] = line[85:115]
            row['UPDATED_DATE'] = line[115:126]
            row['UPDATE_USER'] = line[126:156]
            data.append(row)
    return data

def gs_restitution():
    global DIR
    filename = DIR + 'gs_restitution.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['VICTIMID'] = line[40:50]
            row['TYPE'] = line[50:51]
            row['RECIPENT'] = line[51:52]
            row['AMOUNT'] = line[52:66]
            row['LIABILITY'] = line[66:67]
            row['CREATE_DATE'] = line[67:78]
            row['CREATE_USER'] = line[78:108]
            row['UPDATED_DATE'] = line[108:119]
            row['UPDATE_USER'] = line[119:149]
            data.append(row)
    return data

def gs_participant():
    global DIR

    districts = get_district_list()
    data = []
    for district in districts:
        filename = DIR + 'gs_participant_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10]
                row['CASEID'] = line[10:20]
                row['ID'] = line[20:30]
                row['TYPE'] = line[30:31]
                row['ROLE'] = line[31:33]
                row['SECURITY'] = line[33:34]
                row['DEFEND_NUM'] = line[34:45]
                row['SALUTATION'] = line[45:65]
                row['LAST_NAME'] = line[65:125]
                row['FIRST_NAME'] = line[125:155]
                row['TITLE'] = line[155:185]
                row['LAST_SOUNDS'] = line[128:189]
                row['FIRST_SOUNDS'] = line[189:193]
                row['BUSINESS_TYPE'] = line[193:195]
                row['EIN'] = line[195:215]
                row['PROP_TYPE'] = line[215:217]
                row['TOTAL_TRACTS'] = line[217:228]
                row['CATS_ASSET_ID'] = line[228:243]
                row['AGENCY'] = line[243:247]
                row['AGENCY_NUM'] = line[247:277]
                row['JOB_POSITION'] = line[277:281]
                row['SSN'] = line[281:292]
                row['BIRTH_DATE'] = line[292:303]
                row['GENDER'] = line[303:304]
                row['JUVENILE'] = line[304:305]
                row['RACE'] = line[305:307]
                row['RACE_DESCRIP'] = line[307:337]
                row['IMMIG_STAT'] = line[337:339]
                row['COUNTRY'] = line[339:341]
                row['TRIBE'] = line[341:345]
                row['RESERVATION'] = line[345:349]
                row['ARREST_DATE'] = line[349:360]
                row['PDID'] = line[360:372]
                row['FBI_NUMBER'] = line[372:387]
                row['CRIM_HIST'] = line[387:388]
                row['EST_LOST'] = line[388:402]
                row['ACT_LOSS'] = line[402:416]
                row['HOME_ADDRESS1'] = line[416:446]
                row['HOME_ADDRESS2'] = line[446:476]
                row['HOME_ADDRESS3'] = line[476:506]
                row['HOME_CITY'] = line[506:526]
                row['HOME_STATE'] = line[526:528]
                row['HOME_COUNTY'] = line[528:548]
                row['HOME_ZIPCODE'] = line[548:558]
                row['HOME_PHONE'] = line[558:573]
                row['HOME_FAX'] = line[573:588]
                row['OFF_ADDRESS1'] = line[588:618]
                row['OFF_ADDRESS2'] = line[618:648]
                row['OFF_ADDRESS3'] = line[648:678]
                row['OFF_CITY'] = line[678:698]
                row['OFF_STATE'] = line[698:700]
                row['OFF_COUNTY'] = line[700:720]
                row['OFF_ZIPCODE'] = line[720:730]
                row['OFF_PHONE'] = line[730:745]
                row['OFF_FAX'] = line[745:760]
                row['MARSHALS_NUM'] = line[760:769]
                row['AGCYOFFID'] = line[769:779]
                row['LOWER_CRT_TRIAL_NBR'] = line[779:804]
                row['BUSINESS_CONTACT_LNAME'] = line[804:834]
                row['BUSINESS_CONTACT_FNAME'] = line[834:864]
                row['COLLECT_IND'] = line[864:865]
                row['SYS_INIT_DATE'] = line[865:876]
                row['WEIGHT'] = line[876:878]
                row['EMPLOYER_NAME'] = line[878:918]
                row['EMPLOYER_TYPE'] = line[918:921]
                row['EMPLOYER_DESC'] = line[921:961]
                row['NPI'] = line[961:971]
                row['OCCUPATION'] = line[971:974]
                row['OCCUP_DESC'] = line[974:1034]
                row['HCARE_BUSN_TYPE'] = line[1034:1037]
                row['HCARE_BUSN_DESC'] = line[1037:1077]
                row['CREATE_DATE'] = line[1077:1088]
                row['CREATE_USER'] = line[1088:1118]
                row['UPDATED_DATE'] = line[1118:1129]
                row['UPDATE_USER'] = line[1129:1159]
                data.append(row)
    return data

def gs_part_event():
    global DIR

    districts = get_district_list()
    data = []
    for district in districts:
        filename = DIR + 'gs_part_event_' + district + '.txt'
        with open(filename) as file:
            for line in file:
                row = {}
                row['DISTRICT'] = line[0:10]
                row['CASEID'] = line[10:20]
                row['PARTID'] = line[20:30]
                row['CRTHISID'] = line[30:40]
                row['EVENTID'] = line[40:50]
                row['CREATE_DATE'] = line[50:61]
                row['CREATE_USER'] = line[61:91]
                row['UPDATED_DATE'] = line[91:102]
                row['UPDATE_USER'] = line[102:132]
                data.append(row)
    return data

def gs_court_order_disp():
    global DIR
    filename = DIR + 'gs_court_order_disp.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3]
            row['ID'] = line[3:13]
            row['CASEID'] = line[13:23]
            row['CRTHISID'] = line[23:33]
            row['PARTID'] = line[33:43]
            row['CODE'] = line[43:47]
            row['SYSTEM_DATE'] = line[47:58]
            row['DATE_OF_ORDER'] = line[58:69]
            row['LAST_NAME'] = line[69:129]
            row['FIRST_NAME'] = line[129:159]
            row['COURT'] = line[159:163]
            row['COURT_NUMBER'] = line[163:188]
            row['PARTID2'] = line[188:198]
            row['CREATE_DATE'] = line[198:209]
            row['CREATE_USER'] = line[209:239]
            row['UPDATED_DATE'] = line[239:250]
            row['UPDATE_USER'] = line[250:280]
            data.append(row)
    return data

def gs_defend_stat():
    global DIR
    filename = DIR + 'gs_defend_stat.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['TYPE'] = line[40:42]
            row['START_DATE'] = line[42:53]
            row['CUSTODY_LOC'] = line[53:55]
            row['DETEN_REASON'] = line[55:59]
            row['BOND_TYPE'] = line[59:61]
            row['BOND_AMOUNT'] = line[61:75]
            row['BOND_PROVIDER'] = line[75:100]
            row['TERM_REASON'] = line[100:102]
            row['END_DATE'] = line[102:113]
            row['CREATE_DATE'] = line[113:124]
            row['CREATE_USER'] = line[124:154]
            row['UPDATED_DATE'] = line[154:165]
            row['UPDATE_USER'] = line[165:195]
            data.append(row)
    return data

def gs_instrument():
    global DIR
    filename = DIR + 'gs_instrument.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['CRTHISID'] = line[20:30]
            row['ID'] = line[30:40]
            row['TYPE'] = line[40:42]
            row['FILING_DATE'] = line[42:53]
            row['SYS_FILING_DATE'] = line[53:64]
            row['CREATE_DATE'] = line[64:75]
            row['CREATE_USER'] = line[75:105]
            row['UPDATED_DATE'] = line[105:116]
            row['UPDATE_USER'] = line[116:146]
            data.append(row)
    return data

def gs_agent():
    global DIR
    filename = DIR + 'gs_instrument.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['ID'] = line[30:40]
            row['SALUTATION'] = line[40:48]
            row['LAST_NAME'] = line[48:78]
            row['FIRST_NAME'] = line[78:108]
            row['TITLE'] = line[108:138]
            row['PHONE'] = line[138:158]
            row['FAX'] = line[158:173]
            row['PAGER'] = line[173:188]
            row['LEAD_AGENT'] = line[188:189]
            row['EMAIL'] = line[189:289]
            row['CREATE_DATE'] = line[289:300]
            row['CREATE_USER'] = line[300:330]
            row['UPDATED_DATE'] = line[330:341]
            row['UPDATE_USER'] = line[341:371]
            data.append(row)
    return data


def gs_part_court():
    global DIR
    filename = DIR + 'gs_part_court.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['CRTHISID'] = line[30:40]
            row['APPEAL_ROLE'] = line[40:42]
            row['DISPOSITION'] = line[42:44]
            row['DISP_REASON'] = line[44:48]
            row['DISP_DATE'] = line[48:59]
            row['SYS_DISP_DATE'] = line[59:70]
            row['SYS_INIT_DATE'] = line[70:81]
            row['CREATE_DATE'] = line[81:92]
            row['CREATE_USER'] = line[92:122]
            row['UPDATED_DATE'] = line[122:133]
            row['UPDATE_USER'] = line[133:163]
            data.append(row)
    return data


def gs_assignment():
    global DIR
    filename = DIR + 'gs_assignment.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['CRTHISID'] = line[20:30]
            row['ID'] = line[30:40]
            row['STAFFID'] = line[40:50]
            row['POSITION'] = line[50:51]
            row['START_DATE'] = line[51:62]
            row['END_DATE'] = line[62:73]
            row['CREATE_DATE'] = line[73:84]
            row['CREATE_USER'] = line[84:114]
            row['UPDATED_DATE'] = line[114:125]
            row['UPDATE_USER'] = line[125:155]
            data.append(row)
    return data

def gs_part_count():
    global DIR
    filename = DIR + 'gs_part_count.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['CRTHISID'] = line[30:40]
            row['INSTID'] = line[40:50]
            row['CHARGE'] = line[50:75]
            row['CATEGORY'] = line[75:76]
            row['COUNTID'] = line[76:86]
            row['DISPOSITION'] = line[86:88]
            row['DISP_REASON'] = line[88:92]
            row['DISP_DATE'] = line[92:103]
            row['SEALED'] = line[103:104]
            row['CREATE_DATE'] = line[104:115]
            row['CREATE_USER'] = line[115:145]
            row['UPDATED_DATE'] = line[145:156]
            row['UPDATE_USER'] = line[156:186]
            data.append(row)
    return data


def gs_part_relief():
    global DIR
    filename = DIR + 'gs_part_relief.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['RELIEFID'] = line[30:40]
            row['CREATE_DATE'] = line[40:51]
            row['CREATE_USER'] = line[51:81]
            row['UPDATED_DATE'] = line[81:92]
            row['UPDATE_USER'] = line[92:122]
            data.append(row)
    return data

def gs_relief():
    global DIR
    filename = DIR + 'gs_relief.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID'] = line[20:30]
            row['TYPE'] = line[30:31]
            row['STAGE'] = line[31:32]
            row['REQUESTED_BY'] = line[32:33]
            row['LIABILITY'] = line[33:34]
            row['AMOUNT'] = line[34:50]
            row['NONMONETARY'] = line[50:80]
            row['AGENCY'] = line[80:84]
            row['CREATE_DATE'] = line[84:95]
            row['CREATE_USER'] = line[95:125]
            row['UPDATED_DATE'] = line[125:136]
            row['UPDATE_USER'] = line[136:166]
            data.append(row)
    return data

def gs_triggerlock():
    global DIR
    filename = DIR + 'gs_triggerlock.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['PARTID'] = line[20:30]
            row['BRADY_OFFENSE'] = line[30:31]
            row['NOTICE_3_STRIKES'] = line[31:32]
            row['DATE_NOTICE_FILED'] = line[32:43]
            row['DATE_NOTICE_WITHDRAWN'] = line[43:54]
            row['WITHDRAWAL_REASON'] = line[54:132]
            row['CONVICTION_3_STRIKES'] = line[132:133]
            row['LIFE_3_STRIKES'] = line[133:134]
            row['NO_LIFE_REASON'] = line[134:212]
            row['THIRD_PROSEC_TRIGG_OFFENSE'] = line[212:213]
            row['TRIGGERLOCK_DEF'] = line[213:214]
            row['BAILEY_SENTENCE_CHANGE'] = line[214:215]
            row['SENTENCE_PRIOR_BAILEY'] = line[215:226]
            row['ARMED_CAREER_CRIMINAL'] = line[226:227]
            row['CREATE_DATE'] = line[227:238]
            row['CREATE_USER'] = line[238:268]
            row['UPDATED_DATE'] = line[268:279]
            row['UPDATE_USER'] = line[279:309]
            data.append(row)
    return data

def gs_comment():
    global DIR
    filename = DIR + 'gs_comment.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['CASEID'] = line[10:20]
            row['ID1'] = line[20:30]
            row['ID2'] = line[30:40]
            row['CATEGORY'] = line[40:41]
            row['TEXT'] = line[41:42]
            row['CREATE_DATE'] = line[42:53]
            row['CREATE_USER'] = line[53:83]
            row['UPDATED_DATE'] = line[83:94]
            row['UPDATE_USER'] = line[94:124]
            data.append(row)
    return data


def gs_request():
    global DIR
    filename = DIR + 'gs_request.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:10]
            row['ID'] = line[10:20]
            row['CASEID'] = line[20:30]
            row['STAFFID'] = line[30:40]
            row['REQUEST_DATE'] = line[40:51]
            row['RECEIVE_DATE'] = line[51:62]
            row['RETURN_DATE'] = line[62:73]
            row['STORE_NUM'] = line[73:93]
            row['BOXID'] = line[93:102]
            row['CREATE_DATE'] = line[102:113]
            row['CREATE_USER'] = line[113:143]
            row['UPDATED_DATE'] = line[143:154]
            row['UPDATE_USER'] = line[154:184]
            data.append(row)
    return data

def gs_staff():
    global DIR
    filename = DIR + 'gs_staff.txt'
    data = []
    with open(filename) as file:
        for line in file:
            row = {}
            row['DISTRICT'] = line[0:3]
            row['ID'] = line[3:13]
            row['USERNAME'] = line[13:31]
            row['INITIALS'] = line[31:39]
            row['INIT_STAT'] = line[39:40]
            row['STAFF_TITLE'] = line[40:43]
            row['SALUTATION'] = line[43:51]
            row['LAST_NAME'] = line[51:81]
            row['FIRST_NAME'] = line[81:111]
            row['OFFICE_LOC'] = line[111:141]
            row['PHONE'] = line[141:156]
            row['ISSUED_DATE'] = line[156:167]
            row['DEFAULT_DIR'] = line[167:207]
            row['DEFAULT_PRINT'] = line[207:247]
            row['DEFAULT_DC_LOC'] = line[247:249]
            row['DEFAULT_BRANCH'] = line[249:252]
            row['NAME_SEARCH'] = line[252:253]
            row['STAFF_SEC_TYPE'] = line[253:254]
            row['STAFF_SECTION'] = line[254:262]
            row['CREATE_DATE'] = line[262:273]
            row['CREATE_USER'] = line[273:303]
            row['UPDATE_DATE'] = line[303:314]
            row['UPDATE_USER'] = line[314:344]
            row['AD_USERNAME'] = line[344:374]
            row['LCMS_POSITION'] = line[374:399]
            row['CASE_TYPE'] = line[399:409]
            row['ACTION_STAGE'] = line[409:419]
            row['DR_USERNAME'] = line[419:449]
            row['GUID'] = line[449:479]
            data.append(row)
    return data

# Now, in disk24, there's a bunch of constant tables that need to be translated
# These tables all have codes and their meanings, which vary depending on district
def gs_action():
    global DIR
    filename = DIR + 'table_gs_action.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_agency_off():
    global DIR
    filename = DIR + 'table_gs_agency_off.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['ID'] = line[9:20]
            row['AGENCY'] = line[21:25]
            row['OFFICE'] = line[26:86]
            row['ADDRESS1'] = line[87:117]
            row['ADDRESS2'] = line[118:148]
            row['ADDRESS3'] = line[149:179]
            row['CITY'] = line[180:200]
            row['STATE'] = line[201:206]
            row['ZIPCODE'] = line[207:217]
            row['SALUTATION'] = line[218:228]
            row['CHIEF_LAST_NAME'] = line[229:259]
            row['CHIEF_FIRST_NAME'] = line[260:290]
            row['CHIEF_TITLE'] = line[291:321]
            row['CREATE_DATE'] = line[322:332]
            row['CREATE_USER'] = line[333:363]
            row['UPDATED_DATE'] = line[364:374]
            row['UPDATE_USER'] = line[375:405]
            data.append(row)
    return data

def gs_business_type():
    global DIR
    filename = DIR + 'table_gs_business_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[114:145]
            data.append(row)
    return data

def gs_case_type():
    global DIR
    filename = DIR + 'table_gs_case_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['TYPE'] = line[45:50]
            row['CODE_STAT'] = line[51:59]
            row['GLB_CODE'] = line[60:67]
            row['CREATE_DATE'] = line[68:78]
            row['CREATE_USER'] = line[79:109]
            row['UPDATED_DATE'] = line[110:120]
            row['UPDATE_USER'] = line[121:151]
            data.append(row)
    return data

def gs_case_weight():
    global DIR
    filename = DIR + 'table_gs_case_weight.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data


def gs_counsel_type():
    global DIR
    filename = DIR + 'table_gs_counsel_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:54]
            row['CODE_STAT'] = line[55:63]
            row['GLB_CODE'] = line[64:71]
            row['CREATE_DATE'] = line[72:82]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[114:124]
            row['UPDATE_USER'] = line[125:155]
            data.append(row)
    return data


def gs_court_loc():
    global DIR
    filename = DIR + 'table_gs_court_loc.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['COURT'] = line[9:11]
            row['LOCATION'] = line[12:14]
            row['DESCRIPTION'] = line[15:75]
            row['CREATE_DATE'] = line[76:86]
            row['CREATE_USER'] = line[878:117]
            row['UPDATED_DATE'] = line[118:128]
            row['UPDATE_USER'] = line[129:159]
            data.append(row)
    return data


def gs_deten_reason():
    global DIR
    filename = DIR + 'table_gs_deten_reason.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

# this one's a little messed up
def gs_event_type():
    global DIR
    filename = DIR + 'table_gs_event_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 6:
                count += 1
                continue

            if count % 0 != 0:
                continue

            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:84]
            row['TYPE'] = line[85:90]
            row['CODE_STAT'] = line[91:99]
            row['GLB_CODE'] = line[100:107]
            row['CREATE_DATE'] = line[108:118]
            row['CREATE_USER'] = line[119:149]
            row['UPDATED_DATE'] = line[150:160]
            #row['UPDATE_USER'] = line[]
            data.append(row)
    return data

def gs_evid_disp():
    global DIR
    filename = DIR + 'table_gs_evid_disp.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:39]
            row['CODE_STAT'] = line[40:48]
            row['GLB_CODE'] = line[59:56]
            row['CREATE_DATE'] = line[57:67]
            row['CREATE_USER'] = line[68:98]
            row['UPDATED_DATE'] = line[99:109]
            row['UPDATE_USER'] = line[110:140]
            data.append(row)
    return data

def gs_evid_location():
    global DIR
    filename = DIR + 'table_gs_evid_location.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_evid_type():
    global DIR
    filename = DIR + 'table_gs_evid_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:54]
            row['CODE_STAT'] = line[55:63]
            row['GLB_CODE'] = line[64:71]
            row['CREATE_DATE'] = line[72:82]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[114:124]
            row['UPDATE_USER'] = line[125:115]
            data.append(row)
    return data

def gs_expert():
    global DIR
    filename = DIR + 'table_gs_expert.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['ID'] = line[9:20]
            row['INITIALS'] = line[21:29]
            row['INIT_STAT'] = line[30:38]
            row['TYPE'] = line[39:43]
            row['SSN'] = line[44:55]
            row['SALUTATION'] = line[56:66]
            row['LAST_NAME'] = line[67:97]
            row['FIRST_NAME'] = line[98:128]
            row['TITLE'] = line[129:149]
            row['ADDRESS_1'] = line[160:190]
            row['ADDRESS_2'] = line[191:221]
            row['ADDRESS_3'] = line[222:252]
            row['CITY'] = line[253:273]
            row['STATE'] = line[274:279]
            row['ZIPCODE'] = line[280:290]
            row['PHONE'] = line[291:306]
            row['FAX'] = line[307:322]
            row['CREATE_DATE'] = line[323:333]
            row['CREATE_USER'] = line[334:364]
            row['UPDATED_DATE'] = line[364:375]
            row['UPDATE_USER'] = line[376:406]
            data.append(row)
    return data

def gs_expert_type():
    global DIR
    filename = DIR + 'table_gs_expert_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_immig_stat():
    global DIR
    filename = DIR + 'table_gs_immig_stat.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
    return data

def gs_job_position():
    global DIR
    filename = DIR + 'table_gs_job_position.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_judge():
    global DIR
    filename = DIR + 'table_gs_judge.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['ID'] = line[8:20]
            row['INITIALS'] = line[21:29]
            row['INIT_STAT'] = line[30:34]
            row['LAST_NAME'] = line[35:65]
            row['FIRST_NAME'] = line[66:96]
            row['COURT_ROOM'] = line[97:122]
            row['TYPE'] = line[123:127]
            row['CREATE_DATE'] = line[128:138]
            row['CREATE_USER'] = line[139:169]
            row['UPDATED_DATE'] = line[170:180]
            row['UPDATE_USER'] = line[181:211]
            data.append(row)
    return data

def gs_judge_type():
    global DIR
    filename = DIR + 'table_gs_judge_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_lit_track():
    global DIR
    filename = DIR + 'table_gs_lit_track.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data


def gs_location():
    global DIR
    filename = DIR + 'table_gs_location.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_oppose_attorn():
    global DIR
    filename = DIR + 'table_gs_oppose_attorn.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['ID'] = line[9:20]
            row['INITIALS'] = line[21:31]
            row['INIT_STAT'] = line[32:40]
            row['SALUTATION'] = line[41:51]
            row['LAST_NAME'] = line[52:82]
            row['FIRST_NAME'] = line[83:113]
            row['TITLE'] = line[114:144]
            row['FIRM'] = line[145:195]
            row['ADDRESS1'] = line[196:226]
            row['ADDRESS2'] = line[227:257]
            row['ADDRESS3'] = line[258:288]
            row['CITY'] = line[289:309]
            row['STATE'] = line[310:315]
            row['ZIPCODE'] = line[316:326]
            row['PHONE'] = line[327:342]
            row['FAX'] = line[343:358]
            row['CREATE_DATE'] = line[359:369]
            row['CREATE_USER'] = line[370:400]
            row['UPDATED_DATE'] = line[401:411]
            row['UPDATE_USER'] = line[412:442]
            data.append(row)
    return data

def gs_position():
    global DIR
    filename = DIR + 'table_gs_position.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_prop_type():
    global DIR
    filename = DIR + 'table_gs_prop_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_prop_value_type():
    global DIR
    filename = DIR + 'table_gs_prop_value_type.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:64]
            row['CODE_STAT'] = line[65:73]
            row['GLB_CODE'] = line[74:81]
            row['CREATE_DATE'] = line[82:92]
            row['CREATE_USER'] = line[93:123]
            row['UPDATED_DATE'] = line[124:134]
            row['UPDATE_USER'] = line[135:165]
            data.append(row)
    return data

def gs_relate_case_reason():
    global DIR
    filename = DIR + 'table_gs_relate_case_reason.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:64]
            row['CODE_STAT'] = line[65:73]
            row['GLB_CODE'] = line[74:81]
            row['CREATE_DATE'] = line[82:92]
            row['CREATE_USER'] = line[93:123]
            row['UPDATED_DATE'] = line[124:134]
            row['UPDATE_USER'] = line[135:165]
            data.append(row)
    return data

def gs_relate_part_reason():
    global DIR
    filename = DIR + 'table_gs_relate_part_reason.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:44]
            row['CODE_STAT'] = line[45:53]
            row['GLB_CODE'] = line[54:61]
            row['CREATE_DATE'] = line[62:72]
            row['CREATE_USER'] = line[73:103]
            row['UPDATED_DATE'] = line[104:114]
            row['UPDATE_USER'] = line[115:145]
            data.append(row)
    return data

def gs_reservation():
    global DIR
    filename = DIR + 'table_gs_reservation.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:54]
            row['CODE_STAT'] = line[55:63]
            row['GLB_CODE'] = line[64:71]
            row['CREATE_DATE'] = line[72:82]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[114:124]
            row['UPDATE_USER'] = line[125:155]
            data.append(row)
    return data

def gs_security():
    global DIR
    filename = DIR + 'table_gs_security.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:54]
            row['CODE_STAT'] = line[55:63]
            row['GLB_CODE'] = line[64:71]
            row['CREATE_DATE'] = line[72:82]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[114:124]
            row['UPDATE_USER'] = line[125:155]
            data.append(row)
    return data

def gs_staff_section():
    global DIR
    filename = DIR + 'table_gs_staff_section.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:17]
            row['DESCRIPTION'] = line[18:68]
            row['CODE_STAT'] = line[69:77]
            row['GLB_CODE'] = line[78:85]
            row['CREATE_DATE'] = line[86:96]
            row['CREATE_USER'] = line[97:127]
            row['UPDATED_DATE'] = line[128:138]
            row['UPDATE_USER'] = line[139:169]
            data.append(row)
    return data

def gs_staff_title():
    global DIR
    filename = DIR + 'table_gs_staff_title.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:64]
            row['CODE_STAT'] = line[65:73]
            row['GLB_CODE'] = line[74:81]
            row['CREATE_DATE'] = line[82:92]
            row['CREATE_USER'] = line[93:123]
            row['UPDATED_DATE'] = line[124:134]
            row['UPDATE_USER'] = line[135:165]
            data.append(row)
    return data

def gs_unit():
    global DIR
    filename = DIR + 'table_gs_unit.txt'
    data = []
    count = 0
    with open(filename) as file:
        for line in file:
            if count < 4:
                count += 1
                continue
            row = {}
            row['DISTRICT'] = line[0:8]
            row['CODE'] = line[9:13]
            row['DESCRIPTION'] = line[14:54]
            row['CODE_STAT'] = line[55:63]
            row['GLB_CODE'] = line[64:71]
            row['CREATE_DATE'] = line[72:82]
            row['CREATE_USER'] = line[83:113]
            row['UPDATED_DATE'] = line[114:124]
            row['UPDATE_USER'] = line[125:155]
            data.append(row)
    return data

def find_indices(line):
    return [(m.start(), m.end()) for m in re.finditer(r'\S+', line)]

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()

def parse_global_LIONS():
    global DIR
    filename = DIR + 'global_LIONS.txt'
    datasets = {}
    data = []
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
                    datasets[current_table] = data
                    data = []
                    indices = []
                current_table = line[:-1]
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
                row[fields[i]] = line[indices[i][0]:indices[i][1]]
            data.append(row)
    return datasets


def create_complete_lions_dictionary():


# Last thing is the stuff in lions global_LIONS.txt
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

