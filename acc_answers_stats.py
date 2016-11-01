import json,os
from bs4 import BeautifulSoup

#file_name = "questions.json"
tag_dict={}
json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("ans_")]
for js in json_files:
    with open(js,'r') as data_file:
        file_data={}
        file_data = json.load(data_file)
        data_file.close()
    len_of_ans = 0
    num_of_code = 0
    for ID in file_data:
        html_body = file_data[ID]['body']
        len_of_ans = len_of_ans + len(html_body)
        soup = BeautifulSoup(html_body,'html.parser')
        code_tags = soup.findAll('code')
        if code_tags:
            num_of_code = num_of_code + 1
        
    count = len(file_data)
    avg_len_of_ans = len_of_ans/count
    percent_of_code = 100 * (num_of_code/count)
    tag_dict[js[4:-5]] = str(avg_len_of_ans)+"\t"+str(percent_of_code)
print("Tag\t\tAvg. Ans. Length\t% of Ans. with Code")
for tag in tag_dict:
    print(tag+"\t\t"+tag_dict[tag])