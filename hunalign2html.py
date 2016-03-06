import re
import codecs

def hunalign2html(hunalign_file, name):
	
	out_file = u"%s.html" % (name)

	f1 = codecs.open(out_file,"w","utf8")
	hf = codecs.open(hunalign_file,"r","utf8")

	f1.write("""
		<html>
		<head></head>
		<body>
		<table>
		""")

	for line in hf:
		fields = re.split(r'\t+', line.rstrip('\t'))
		f1.write("\n<tr><td>%s</td><td>%s</td></tr>" % (fields[1], fields[0]))

	f1.write("""
		</table>
		</body>
		""")

	f1.close()
	hf.close()	

if __name__ == '__main__':

	hunalign2html('Mozilla-Align.csv','Mozilla')	
