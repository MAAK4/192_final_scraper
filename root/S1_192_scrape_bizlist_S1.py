
'''
        >>> Step 1
        >>> Author : Hamza
        >>> Programming Style : Functional / Script
        >>> Script Aim : Scraper
        >>> Async/Sync : Sync (tbc_later)

        >>> Conclusion : Saves to .html.

        >>> Status : Under construction.

        >>> What does it do?    This script requests 192.com using relevant headers and searches for
                                a specific keyword - for e.g. Gold.
                                The response contains all companies that deal in the searched commodity.
                                The search is done using Advanced Business Search and this allows us
                                to enter the Keyword (Gold) as Business Type.

'''

import requests, os
from bs4 import BeautifulSoup as BS
from collections import ChainMap
# from utils import payload_parser as PP
# from utils import headers, url_adv_search
# # from log_script import log, console


params = """company: 
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


def prepare_params(item_needed : str, params_template : str) -> str:

	params_template = params_template.format(item_needed)
	params_template = [x.replace("\t", "") for x in params_template.split("\n")]
	params_template = [(x.split(":")) for x in params_template]
	params_template = {x:y for [x,y] in params_template}


	return params_template


print(prepare_params('gold', params_template=params))



def main(url_adv_search, headers, item_needed):

	params = """company: 
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
	btnSearch: Search""".format(item_needed)

	params = [x.replace("\t", "") for x in params.split("\n")]
	params = [(x.split(":")) for x in params]
	params = {x:y for [x,y] in params}

	r = requests.get(url_adv_search, headers = headers, params = params);
	response_text = r.text;

	file_type = "html";
	file_name : str = f"{item_needed}.{file_type}";

	print(f"Attempting to save ITEM : {item_needed}'s web/html page to {file_name}.");

	final_save_path = os.path.join("html_pages", file_name)

	with open(final_save_path, "w") as f:
		f.write(response_text); 
		print("Saved to {}".format(final_save_path));
		log.info("Saved to {}".format(final_save_path))
