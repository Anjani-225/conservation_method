from flask import Flask
from Bio.Blast import NCBIXML
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom

##running and parsing BLAST
#app = Flask(__name__)
#i = 0
#f = open('mafftIP.txt', 'w')
#f1 = open('mafftOP.txt', 'w')
#E_VALUE_THRESH = 1e-20
#for record in NCBIXML.parse(open("results.xml")): 
     #if record.alignments: 
       # print("\n") 
       # print("query: %s" % record.query[:100]) 
        #for align in record.alignments: 
         #  for hsp in align.hsps: 
          #    if hsp.expect < E_VALUE_THRESH: 
           #     print("match: %s " % align.title[:100]," ",align.hsps[:100])
               # print(i)
                #f.write(hsp.query)
                #print(hsp.query)
                #i  = i + 1

##running MAFFT

###blast search 
os.system("blastp -query test.fasta -subject uniprotsprot.fasta -outfmt '6 qseqid sseqid sseq evalue' -out file_align.txt")
##blast output parsed into fasta format
cmd ='''"awk 'BEGIN { OFS = "\n"} {print ">" $1 $2, $3}' file_align.txt > file2.txt"'''
os.system(cmd)
os.system("mafft --auto file2.txt > outputMAFFT.txt")

##AACon
final_cmd = "java -jar compbio-conservation-1.1.jar -i=outputMAFFT.txt -m -o=finalOutput.txt" 
os.system(final_cmd)
os.system('cat finalOutput.txt')
# Selects the page for which a function is to be defined. Right now there will only be one page in your website.

@app.route('/')
def hello():

    return "<h1>Hello World!</h1>" \
           "\nThis is my introduction to Flask!" \
           "\nI can write a lot of things on this page.\nLet's get started!"

# The above function returns the HTML code to be displayed on the page



if __name__ == '__main__':

   app.run()