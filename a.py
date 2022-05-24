import re

from datetime import date
todays_date = date.today()

####### —————————————— Processing OHOTa-RUBY ——————————————

inputFile = "./OHOTa.txt"
outputFile = "./OHOTa-Ruby.ot"

# loading data
f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf_8_sig')
bcv = ""

for ol in Lines:
	if len(ol) > 1:
		x = re.split ("\t", ol)
		if (x[0]== bcv):
			f.write(" ")
		else:
			bcv = x[0]
			f.write("\n")
			f.write("<rt>"+x[0]+"</rt> ")
		# --------------
		x[4] = re.sub("\n","",x[4])
		f.write("<RUBY><ruby><ruby>"+x[1]+"<rt>"+x[3]+"</rt></ruby><rt>"+x[4]+"</rt></ruby><rt>"+x[2]+"</rt></RUBY>")

# ---------- 
f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OHOTa-Ruby\nversion.major="+str(todays_date.year)+"\nversion.minor="+str(todays_date.month)+str(todays_date.day)+"\nversion.date="+str(todays_date)+"\ndescription=OHOTa-Ruby (https://github.com/Andley/OHOTa)")

f.close()
