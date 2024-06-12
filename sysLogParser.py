import re
import os

def ip_count(file):
    dict1 = {}
    
    for line in file:
        match = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if match:
            if match.group(0) in dict1:
                dict1[match.group(0)] += 1
            else:
                dict1[match.group(0)] = 1
        else:
            pass
    file.seek(0)
    list1 = sorted(dict1.items(), key=lambda x: x[1])
    with open('./ipFile.txt', 'w') as f:
        for line in list1:
            f.writelines('IP ' + line[0] + ' was seen ' + str(line[1]) + ' time(s)\n')
            
def superuser_count(file):
    dict2 = {}
    
    for line in file:
        #print(line)
        if "Successful su" in line:
            #print(line)
            line = line.split()
            user = line[10]
            if user not in dict2:
                dict2[user] = 1
            else:
                dict2[user] += 1
    list2 = sorted(dict2.items(), key=lambda x: x[1])
    file.seek(0)
    with open('./superuser_count.txt', 'w') as f:
        for line in list2:
            f.writelines('User ' + line[0] + ' used superuser ' + str(line[1]) + ' time(s)\n')
            
def failed_logins(file):
    dict3 = {}
    for line in file:
        if 'Failed password' in line:
            user = line.split()[8]
            if user in dict3:
                dict3[user] += 1
            else:
                dict3[user] = 1
    list3 = sorted(dict3.items(), key=lambda x: x[1])
    file.seek(0)
    with open('./failedLogins.txt', 'w') as f:
        for line in list3:
            f.writelines('The user: ' + line[0] + ' failed to login ' + str(line[1]) + ' time(s)\n')
        
def main():
    ourFile = input('Specify a file to parse through (full directory)')
    if os.path.isfile(ourFile):
        with open(ourFile) as f:
            ip_count(f)
            superuser_count(f)
            failed_logins(f)
    else:
        print('Invalid Input')
main()
