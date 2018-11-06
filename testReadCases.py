# CS506 Federal Prosecutor Project
# Justin, Ben, Hao
# 
# Preliminary code to parse through the .txt files and extract certain fields.
# Primarily using this file to explore the various data.

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
        

find_Info()
