import json,os
import json,os
import time
from datetime import datetime
import argparse
#from datetime import datetim

def date_to_epoch(normal_time):
    pattern = '%m-%d-%Y'
    epoch_time = int(time.mktime(time.strptime(normal_time, pattern)))
    return epoch_time

# function to convert epoch time to normal date_time
def epoch_to_date(epoch_time):
    normal_time = datetime.fromtimestamp(epoch_time)
    return normal_time

parser = argparse.ArgumentParser()
parser.add_argument("startDate",help = "enter the Min Date in MM-DD-YYYY format") 
parser.add_argument("endDate",help = "enter the Max Date MM-DD-YYYY format") 
args = parser.parse_args()

date_start = args.startDate
date_end = args.endDate

date_start = datetime.strptime(date_start,'%m-%d-%Y')
date_end = datetime.strptime(date_end,'%m-%d-%Y')

#file_name = "questions.json"
tag_dict={}
json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("qst_")]
for js in json_files:
    with open(js,'r') as data_file:
        file_data={}
        file_data = json.load(data_file)
        data_file.close()
    num_of_ans = 0 
    view_count = 0
    num_of_ques=0
    for ID in file_data:
        if(epoch_to_date(file_data[ID]['creation_date']) >= date_start and epoch_to_date(file_data[ID]['creation_date']) >= date_start):
            num_of_ans = num_of_ans + file_data[ID]['answer_count']
            view_count = view_count + file_data[ID]['view_count']
            num_of_ques = num_of_ques + 1
    tag_dict[js[4:-5]] = str(num_of_ans/num_of_ques)+"\t\t"+str(view_count/num_of_ques)
print("Tag\t\tAvg. Ans.\tAvg. Views per Ques.")
for tag in tag_dict:
    print(tag+"\t\t"+tag_dict[tag])
