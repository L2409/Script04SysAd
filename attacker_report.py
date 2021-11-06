#!/usr/bin/python3
#Logan Dorman
#11/6/21

#import geoip for the country of the ips, os for clear, and datetime for the date
from geoip import geolite2
import os
from datetime import date
import re

def main():
    #clears terminal
    os.system("clear")
    #get todays date
    day = date.today()
    #The location of the file
    filename = "/home/student/Desktop/Script04SysAd/syslog.log"
    #What the system is looking for in a line
    keyword = "Failed password"
    #Make a dicitonary that holds the ip as the key and the times the ip has appeared as the value
    ip_dict = {}
    #print the header
    print("Attacker Report -",day,"\n")

    #opens the filename as 'file'
    with open(filename) as file:
        file = file.readlines()
    
    #for each line in the file if the line contains the keyword, then split it into tokens and grab
    #the ip. Then put it in a dictionary.
    for line in file:
        if keyword in line:
            tokens = line.split(" ")
            ip = tokens[10]
            #lines that contain both keyword and user have the ip at a different token
            if "user" in line:
                ip = tokens[12]
            #Try to add to the dict at entry, if it doesn't exist then set dict[entry] to 1
            print(re.match("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$",line))
            if re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$",ip):
                try:
                    ip_dict[ip] += 1
                except:
                    ip_dict[ip] = 1

    #for each entry in dict grab the country from the ip and then print the line containing
    #its count, and the country that is associated with it
    for entry in ip_dict:
        try:
            match = geolite2.lookup(entry)
            if ip_dict[entry] >= 10:
                print("COUNT: ",ip_dict[entry], ", IP ADDR: ", entry, ", COUNTRY: ", match.country, sep="")
        except:
            pass
    


if __name__ == "__main__":
    main()

#Info on how to get date from: https://www.programiz.com/python-programming/datetime/current-datetime
