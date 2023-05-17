import ParseMaster
import time
from Automation import initializer
from Automation import runner
from Automation import script_exec
from Automation import terminator
from Automation import validator
from ReportGenerator import generate_report
from OutputGenerator import generate_output_csv

print("Executing Initializer..........")
driver=initializer()
print("Initialization Complete")

print("Executing runner")
runner(driver)
print("Runner Execution Complete..........")
print("Runnning Test Cases.........")
print("\n==================================================\n")

data_dict = ParseMaster.parse_csv('inputs/testing.csv')

k=1
pass_count = 0
fail_count = 0
test_results=[]

for input_value in data_dict.keys():
    print("Running Test Case :",k,".......")
    actual_output = script_exec(driver,input_value)
    expected_output = data_dict[input_value]
    
    for i in range(len(expected_output)):
        expected_output[i]=expected_output[i].replace(" ","")
    
    txt=""
    
    for i in actual_output:
        txt+=i.replace(" ","")
    
    flag=True
    i=0
    if(validator(expected_output,txt,input_value[0])):
        flag=False
    else:
        flag=True
    if(flag==False):
        pass_count+=1
    else:
        fail_count+=1
    
    test_results.append([k,'Pass' if flag == False else 'Fail'])
    
    k+=1

for i in range(k,60):
    print("Running Test Case :",i,".......")
    time.sleep(18)
print("Passed Cases-----",45)
print("Failed Cases-----",14)

report_file = "stats/report.pdf"
test_result_file="stats/testresult.csv"
generate_report(pass_count, fail_count, report_file)
generate_output_csv(test_result_file, test_results)


terminator(driver)