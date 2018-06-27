import glob
import os

for filename in glob.glob('*.txt'):
	articles = open(filename,'r', encoding = 'utf-8-sig')
	count = 0
	print (filename)
	# print (articles)
	for article in articles:
		f = open(os.getcwd()+"\\created\\"+filename[:-4]+str(count)+'.txt', 'w', encoding = 'utf-8')
		count = count + 1 
		f.write(article)
		f.close()
		# print (article)