import re;

def clean_number(number : str) -> str:  
    clean_number = "";

    number = number.strip();
    
    if (re.search('\D', number[0])!=None):
        # the longest global exension is 2
        global_extension = re.search("^\D\d{1,2}", number)
        if (len(global_extension.group()) > 2):
            rest = number;
        else:
            clean_number += '+' + global_extension.group()[1:] + ' ';

        rest = number[global_extension.end() : ]
    else:
        rest = number
    
    rest_of_number = re.findall('\d+',rest);
    clean_number += ' '.join(rest_of_number);

    return clean_number;
