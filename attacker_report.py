#!/usr/bin/python3
#Logan Dorman
#11/6/21

from geoip import geolite2
import os
from datetime import date

def main():
    os.system("clear")
    day = date.today()
    filename = "/home/student/Desktop/Script04SysAd/syslog.log"
    keyword = "Failed password"
    ip_dict = {}
    print("Attacker Report -",day,"\n")

    with open(filename) as file:
        file = file.readlines()
    
    for line in file:
        if keyword in line:
            tokens = line.split(" ")
            ip = tokens[10]
            if "user" in line:
                ip = tokens[12]
            try:
                ip_dict[ip] += 1
            except:
                ip_dict[ip] = 0
                print("NEW IP! ",ip)

    for entry in ip_dict:
        print("COUNT: ",ip_dict[entry], ", IP ADDR: ", entry, ", COUNTRY: ", "WIP", sep="")
    


if __name__ == "__main__":
    main()

#Info on how to get date from: https://www.programiz.com/python-programming/datetime/current-datetime
