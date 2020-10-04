#todo
import json
def convert_json_to_csv(json_obj):
    the_whole_csv_file = "att,rlx,del,the,lal,hal,hbe,lbe,lga,mga,result\n"
    max_amt_of_rows = 99999999999

    for each_key in json_obj.keys():
        max_amt_of_rows = min(max_amt_of_rows, len(json_obj[each_key]))

    for i in range(max_amt_of_rows):
        the_whole_csv_file += "{},{},{},{},{},{},{},{},{},{},down\n".format(json_obj['att'][i], json_obj['rlx'][i], json_obj['del'][i], json_obj['the'][i], json_obj['lal'][i], json_obj['hal'][i], json_obj['hbe'][i], json_obj['lbe'][i], json_obj['lga'][i], json_obj['mga'][i])

    return the_whole_csv_file

my_file = open("complete_data.txt","r")

output_file = open("processed_data_down.csv","w")

for each_line in my_file:
    if each_line != "":
        json_obj = json.loads(each_line)
        output_file.write(convert_json_to_csv(json_obj))
        break
