"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import glob
import os
import datetime

total_score = 0
file_ctr = 0
now = datetime.datetime.now()
now = str(now)
now = now.split(' ')
now = now[0]

#newpath = r'C:/news_data_for_nlp_' + now + '/'
newpath = r'C:/news_data_for_nlp_2018-02-24/'
if not os.path.exists(newpath):
	os.makedirs(newpath)
	
outputfile = newpath + '/' + 'merged.txt'
fileoutput = open(outputfile,"w") 

def print_lines(all_lines):
    fileoutput.write(all_lines)
    return 0


def mergeFiles(movie_review_filename):
    with open(movie_review_filename, encoding="utf8") as sraped_file:
        # Instantiates a plain text document.
        content = sraped_file.read()

    # Print all lines
    print_lines(content)

if __name__ == '__main__':
	for filename in glob.glob(os.path.join(newpath, '*.txt')):
		try:
			print('processing file = ', filename)
			mergeFiles(filename);
		except Exception:
			continue
			
	fileoutput.close()
	print('total_score = ', total_score)