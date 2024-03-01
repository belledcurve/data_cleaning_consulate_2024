import re;

def clean_number(number : str) -> str:  
    clean_number = "";

    number = number.strip();
    
    if (re.search('\D', number[0])!=None):
        # the longest global exension is 2
        global_extension = re.search("^\D\d{0,2}", number)
        if (len(global_extension.group()) > 3):
            rest = number;
        else:
            clean_number += '+' + global_extension.group()[1:] + ' ';

        rest = number[global_extension.end() : ]
    else:
        rest = number
    
    rest_of_number = re.findall('\d+',rest);
    clean_number += ''.join(rest_of_number);

    return clean_number;



import pandas as pd;

testcase_numbers = pd.read_csv('../testcases/phone_numbers.csv');
testcase_numbers['clean_no'] = testcase_numbers.phone.apply(clean_number);

f = open('phone_numbers_test_case.csv', 'w');
for numbers in testcase_numbers.clean_no:
    f.write(numbers + '\n');

f.close()

