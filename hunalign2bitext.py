import re
import codecs
from argparse import ArgumentParser

def hunalign2bitext(hunalign_file, name, lang1, lang2):
	
	out_file1 = u"%s.%s" % (name, lang1)
	out_file2 = u"%s.%s" % (name, lang2)

	f1 = codecs.open(out_file1,"w","utf8")
	f2 = codecs.open(out_file2,"w","utf8")

	hf = codecs.open(hunalign_file,"r","utf8")

	for line in hf:

		fields = re.split(r'\t+', line.rstrip('\t'))
		print (fields)
		print (fields[2])
	
		f1.write("\n" + fields[1])
		f2.write("\n" + fields[0])


	f1.close()
	f2.close()
	hf.close()	

if __name__ == '__main__':

	parser = ArgumentParser(description="Trosi ffeiliau TMX i ddwy ffeil")

	parser.add_argument('-s', '--source-csv', dest="source_csv", required=True, help="Ffeil testun Saesneg")
	parser.add_argument('-n', '--name', dest="base_filename", required=True, help="Enw'r ffeil ")
	args = vars(parser.parse_args())

	try:
		hunalign2bitext(args['source_csv'], args['base_filename'], 'en','cy')
	except Exception as e:
		print(e)
