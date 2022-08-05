print("Imported Utilities.")

import re
from collections import ChainMap

with open("payload.txt") as f:
    pl = f.read()

def payload_parser(pl):    

    new_pl = {}

    split_by_newline = pl.split("\n")

    for x in split_by_newline:
        split_x = x.split(":")
        var_key = split_x[0]
        var_value = split_x[-1]
        if var_value in ["", " "]:
            new_pl[var_key] = ""            
        else:
            new_pl[var_key] = var_value

    return new_pl

def space_remover(tag_):
    tag_ = tag_.replace("\n", "")
    tag_ = (re.sub("\s+", " ", tag_).strip())
    tag_ = re.search("^(\d*) ", tag_).group(0)

headers = {
    "user-agent": 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }

sk_params = {"sk" : 'sk: 160a7058-f80f-4032-9d26-c9dd3da0556c'} # The key that breaks the web defense.


printer = lambda c, s : [print(x) for x in [
    f"{c} complete.", 
    f"{s} skipped due to empty tags.", 
    f"Total times http requests sent : {c + s}"
    ]]

basic_params = '''looking_for: {}
location: 
searchBtn: Search'''

adv_params = """company: 
description: {}
subbuild: 
buildno: 
buildname: 
street: 
locality: 
town: 
county: 
postcode: 
country: 
btnSearch: Search"""

url_adv_search ='https://www.192.com/businesses/search/advanced/'

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}