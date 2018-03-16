# -*- coding: utf-8 -*- 
#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""
import codecs
import sys
from os import path
from wordcloud import WordCloud


#d = path.dirname(__file__)
d = 'C:/news_data_for_nlp_2018-02-24/'

# Read the whole text.
text = open(path.join(d, 'merged.txt'), encoding="latin-1").read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.show()