import csv
import ParseMaster
from Automation import run_automation

data_dict = ParseMaster.parse_csv('inputs/testing.csv')

k=1
for input_value in data_dict.keys():
    print("==================================================")
    print("Running Test Case :",k)
    actual_output = run_automation(input_value)
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
    print("Input        :",input_value)
    print("Actual       :",actual_output)
    print("Expected     :",expected_output)
    if(flag==False):
        print("Passed")
    else:
        print("Failed")
        
    print("==================================================")
    
    k+=1