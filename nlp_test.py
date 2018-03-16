"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
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
newpath = r'C:/test_folder/'
if not os.path.exists(newpath):
	os.makedirs(newpath)
	
outputfile = newpath + '/' + 'results.log'
fileoutput = open(outputfile,"w") 

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        #print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))
    
    global total_score
    global file_ctr
    total_score = score + total_score
    file_ctr = file_ctr + 1
    fileoutput.write('Overall Sentiment: score of {} with magnitude of {} \n'.format(score, magnitude))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, encoding="utf8") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(content=content,type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(
    #    description=__doc__,
    #    formatter_class=argparse.RawDescriptionHelpFormatter)
    #parser.add_argument(
    #    'movie_review_filename',
    #    help='The filename of the movie review you\'d like to analyze.')
    #args = parser.parse_args()

	#path = 'C:\\news_data_for_nlp_2017-10-10\\'
	#path = 'C:\\news_data_for_nlp_2017-10-10\\TEST\\'
	for filename in glob.glob(os.path.join(newpath, '*.txt')):
		try:
			print('processing file = ', filename)
			analyze(filename)
		except Exception:
			continue
	
	average = total_score/file_ctr
	fileoutput.write('Total Score for this folder is: {} \n'.format(total_score))
	fileoutput.close()
	print('total_score = ', total_score)