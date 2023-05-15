import ParseMaster
from Automation import initializer
from Automation import runner
from Automation import script_exec
from Automation import terminator
from ReportGenerator import generate_report
from OutputGenerator import generate_output_csv

print("Executing Initializer")
driver=initializer()
print("Initialization Complete")

print("Executing runner")
runner(driver)
print("Runner Execution Complete")

data_dict = ParseMaster.parse_csv('inputs/testing.csv')

k=1
pass_count = 0
fail_count = 0
test_results=[]

for input_value in data_dict.keys():
    print("==================================================")
    print("Running Test Case :",k)
    actual_output = script_exec(driver,input_value)
    expected_output = data_dict[input_value]
    
    for i in range(len(expected_output)):
        expected_output[i]=expected_output[i].replace(" ","")
    
    txt=""
    
    for i in actual_output:
        txt+=i.replace(" ","")
    
    flag=True
    i=0
    while(flag==True and i<len(expected_output)):
        if(expected_output[i] in txt):
            flag=False
        i+=1
    # print("Input        :",input_value)
    # print("Actual       :",actual_output)
    # print("Expected     :",expected_output)
    if(flag==False):
        print("Passed")
        pass_count+=1
    else:
        print("Failed")
        fail_count+=1
    
    test_results.append([k,'Pass' if flag == False else 'Fail'])
        
    print("==================================================")
    
    k+=1

report_file = "stats/report.pdf"
test_result_file="stats/testresult.csv"
generate_report(pass_count, fail_count, report_file)
generate_output_csv(test_result_file, test_results)


terminator(driver)