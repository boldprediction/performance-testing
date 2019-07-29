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
    with open('request-10.log') as f:
        for line in f:
            lineList.append(line)
            contrast_id = str(line).strip()
            respURL = "http://3.13.100.240:8000/api/get_contrast?contrast_id=" + contrast_id
            # print(requests.get(respURL).content)
            detailedlog.write("\n"+contrast_id + "\t")
            start_time = json.loads(requests.get(respURL).content)[
                'created_at']
            detailedlog.write(str(start_time) + "\t")

            end_time = json.loads(requests.get(respURL).content)[
                'result_generated_at']
            detailedlog.write(str(end_time) + "\t")

            date_time_str = start_time[0:26]
            date_time_str1 = end_time[0:26]
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')
            date_time_obj1 = datetime.datetime.strptime(
                date_time_str1, '%Y-%m-%d %H:%M:%S.%f')
            print((date_time_obj1 - date_time_obj).total_seconds())
            plotlog.write(str((date_time_obj1 - date_time_obj).total_seconds())+"\n")
            detailedlog.write(
                str((date_time_obj1 - date_time_obj).total_seconds())+"\n")

readcontrast()