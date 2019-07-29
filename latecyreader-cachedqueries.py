import requests
import json
import datetime
import time
import traceback


ploterrlog = open("ploterr.log", "a+")
plotlog = open("plots.log", "a+")
detailedlog = open("detailed.log", "a+")


def readcontrast():
    lineList = list()
    with open('./logs/requests-all.log') as f:
        for line in f:
            lineList.append(line)
            contrast_id = str(line).strip()
            start_time = ticks = time.time()
            respURL = "http://3.13.100.240:8000/api/get_contrast?contrast_id=" + contrast_id
            detailedlog.write("\n"+contrast_id + "\t")
            while(requests.get(respURL).content == None):
                time.sleep(1)
            end_time = ticks = time.time()
            detailedlog.write(str(start_time) + "\t")
            detailedlog.write(str(end_time) + "\t")
            print((end_time - start_time))
            plotlog.write(str((end_time - start_time))+"\n")
            detailedlog.write(
                str((end_time - start_time))+"\n")


readcontrast()
