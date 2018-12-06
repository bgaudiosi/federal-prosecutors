import psycopg2
from lions.parse import *

def global_lions_func(global_lions, table):
    sql, rows = global_lions[table]
    def func():
        return (sql, rows)
    return func

def create_table(name, sql):
    s =  'CREATE TABLE ' + name + ' (\n'
    for k,v in sql['types'].items():
        s += '    ' + k + ' ' + v
        #if k in sql['not_null']:
        #    s += ' NOT NULL'
        s += ',\n'

    s += '    PRIMARY KEY('
    for field in sql['primary']:
        s += field + ', '
    s = s[:-2] + '),\n'

    #for k,v in sql['foreign'].items():
    #    s += '    FOREIGN KEY (' + k + ') REFERENCES ' + v + ',\n'

    s = s[:-2] + '\n'
    s += ')'
    return s

def fill_table(name, sql, table):
    pass

def init(name, func, cur):
    print("Initializing", name)
    sql, table = func()
    #print(sql)
    #print(table[0])
    seen = {}
    name = name.lower()

    # First, check if table already exists
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (name,))
    exists = cur.fetchone()[0]
    if not exists:
        create_table_command = create_table(name, sql)
        cur.execute(create_table_command)

    insert_commands = []
    base = 'INSERT INTO ' + name + '('
    fields = ""
    for k in sql['types'].keys():
        fields += k + ', '

    base = base[:-2] + ') VALUES '

    primary_len = len(sql['primary'])
    seen = {}
    #'INSERT INTO table(col1, col2, ...) VALUES (..., ...)'
    num_scrubbed = 0
    row_num = 0
    for row in table:
        scrubbed = False
        values = []
        for k in sql['types'].keys():
            if k == 'UPDATE_USER' and list(sql['types'].keys())[-1] == 'UPDATE_USER':
                values += ['NULL']
                break

            if len(row[k]) == 0 or row[k][0] == '*':
                if k in sql['primary']:
                    scrubbed = True
                else:
                    values += ['NULL']
            else:
                values += [row[k]]

        if scrubbed:
            num_scrubbed += 1
            continue

        primary_key = str(tuple(values[:primary_len]))
        if primary_key in seen:
            continue
        else:
            seen[primary_key] = 1

        args = "(" + "%s,"*(len(values)-1) + "%s" + ")"
        args_str = cur.mogrify(args, values).decode('utf-8')
        args_str = args_str.replace("'NULL'", "NULL")
        row_num += 1
        cur.execute("INSERT INTO " + name + " VALUES " + args_str)
    print("Inserted", len(table), 'rows')
    print("Number of rows scrubbed:", num_scrubbed)

def initialize_db():
    # Create the datab
    lions = {}
    lions['GS_ALSO_KNOWN'] = gs_also_known
    lions['GS_ARCHIVE_CASE'] = gs_archive_case
    lions['GS_ARCHIVE_PART'] = gs_archive_part
    lions['GS_CASE'] = gs_case
    lions['GS_CASE_CAUSE_ACT'] = gs_case_cause_act
    lions['GS_CASE_DOJ_DIV'] = gs_case_doj_div
    lions['GS_CASE_DOM_TERR_IND'] = gs_case_dom_terr_ind
    lions['GS_CASE_PROG_CAT'] = gs_case_prog_cat
    lions['GS_CASE_SPECIAL_PROJ'] = gs_case_special_proj
    lions['GS_EVIDENCE'] = gs_evidence
    lions['GS_EXPERT_CASE'] = gs_expert_case
    lions['GS_INST_CHARGE'] = gs_inst_charge
    lions['GS_PART_VICTIM'] = gs_part_victim
    lions['GS_RELATE_CASE'] = gs_relate_case
    lions['GS_RELATE_PART'] = gs_relate_part
    lions['GS_CONT_SERVICES'] = gs_cont_services
    lions['GS_CONTACT_LOG'] = gs_contact_log
    lions['GS_CONTROL_SUB'] = gs_control_sub
    lions['GS_COUNT'] = gs_count
    lions['GS_COURT_HIST'] = gs_court_hist
    lions['GS_COURT_JUDGE'] = gs_court_judge
    lions['GS_DNA'] = gs_dna
    lions['GS_PROP_VALUE'] = gs_prop_value
    lions['GS_REGION'] = gs_region
    lions['GS_RELATE_APPEAL'] = gs_relate_appeal
    lions['GS_SENTENCE'] = gs_sentence
    lions['GS_EVENT'] = gs_event
    lions['GS_OPPOSE_COUN'] = gs_oppose_coun
    lions['GS_RESTITUTION'] = gs_restitution
    lions['GS_PARTICIPANT'] = gs_participant
    lions['GS_PART_EVENT'] = gs_part_event
    lions['GS_COURT_ORDER_DISP'] = gs_court_order_disp
    lions['GS_DEFEND_STAT'] = gs_defend_stat
    lions['GS_INSTRUMENT'] = gs_instrument
    lions['GS_AGENT'] = gs_agent
    lions['GS_PART_COURT'] = gs_part_court
    lions['GS_ASSIGNMENT'] = gs_assignment
    lions['GS_PART_COUNT'] = gs_part_count
    lions['GS_PART_RELIEF'] = gs_part_relief
    lions['GS_RELIEF'] = gs_relief
    lions['GS_TRIGGERLOCK'] = gs_triggerlock
    lions['GS_REQUEST'] = gs_request
    lions['GS_STAFF'] = gs_staff
    lions['GS_ACTION'] = gs_action
    lions['GS_AGENCY_OFF'] = gs_agency_off
    lions['GS_BUSINESS_TYPE'] = gs_business_type
    lions['GS_CASE_TYPE'] = gs_case_type
    lions['GS_CASE_WEIGHT'] = gs_case_weight
    lions['GS_COUNSEL_TYPE'] = gs_counsel_type
    lions['GS_COURT_LOC'] = gs_court_loc
    lions['GS_DETEN_REASON'] = gs_deten_reason
    lions['GS_EVENT_TYPE'] = gs_event_type
    lions['GS_EVID_DISP'] = gs_evid_disp
    lions['GS_EVID_LOCATION'] = gs_evid_location
    lions['GS_EVID_TYPE'] = gs_evid_type
    lions['GS_EXPERT'] = gs_expert
    lions['GS_EXPERT_TYPE'] = gs_expert_type
    lions['GS_IMMIG_STAT'] = gs_immig_stat
    lions['GS_JOB_POSITION'] = gs_job_position
    lions['GS_JUDGE'] = gs_judge
    lions['GS_JUDGE_TYPE'] = gs_judge_type
    lions['GS_LIT_TRACK'] = gs_lit_track
    lions['GS_LOCATION'] = gs_location
    lions['GS_OPPOSE_ATTORN'] = gs_oppose_attorn
    lions['GS_POSITION'] = gs_position
    lions['GS_PROP_TYPE'] = gs_prop_type
    lions['GS_PROP_VALUE_TYPE']= gs_prop_value_type
    lions['GS_RELATE_CASE_REASON'] = gs_relate_case_reason
    lions['GS_RELATE_PART_REASON'] = gs_relate_part_reason
    lions['GS_RESERVATION'] = gs_reservation
    lions['GS_SECURITY'] = gs_security
    lions['GS_STAFF_SECTION'] = gs_staff_section
    lions['GS_STAFF_TITLE'] = gs_staff_title
    lions['GS_UNIT'] = gs_unit
    global_lions = parse_global_LIONS()
    for table in global_lions.keys():
        lions[table] = global_lions_func(global_lions, table)

    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="postgres")
        cur = conn.cursor()

        conn.autocommit = True
        cur.execute("DROP DATABASE lions;")
        cur.execute("CREATE DATABASE lions;")

        cur.close()
        conn.commit()

        conn = psycopg2.connect(host="localhost", database="lions")
        cur = conn.cursor()
        conn.autocommit = True
        for key in lions.keys():
            init(key, lions[key], cur)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    initialize_db()
