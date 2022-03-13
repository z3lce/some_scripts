import re,argparse,csv,codecs

def flter_blank(string):
    return re.sub("\s","",string,flags=re.MULTILINE|re.UNICODE)

def csv_reader(filename):
    with codecs.open(filename,'r+','utf-8-sig') as f:
        csv_read=csv.reader(f,dialect='excel')
        for i in csv_read:
            match_res(i)
    f.close()        

def txt_reader(filename):
    with codecs.open(filename,'r+','utf-8-sig') as f:
        res=f.readline()
        match_res(res)
    f.close()    


def csv_writer(filename,content):
    with codecs.open(filename,'a+','utf-8-sig') as f:
        csv_write=csv.writer(f,dialect='excel')
        csv_write.writerow(content)


'''
@content:???
@ ???
'''
def match_res(content):
    content=flter_blank(content)
    list_matchmode=list()
    list_matchmode.append(re.compile('(2\S*?)((?:3)|(?:4)|(?:5)|(?:6)|(?:7)|(?:8)|(?:9))',flags=re.U))
    list_matchmode.append(re.compile('(6\S*?)((?:3)|(?:4)|(?:5)|(?:6)|(?:7)|(?:8)|(?:9)|(?:2))',flags=re.U))
    #print("log: pp@value=",pp)
    for i in list_matchmode:
        res =i.search(content)
        print(res.group(1),res.start(),res.end())
        s=res.end()-1
        while True:
            res =i.search(content,s,len(content))
            
            if res is None:
                break
            else:
                if res.group(1) is None:
                    break
                else:
                    print(res.group(1),res.start(),res.end(),res)
                    s=res.end()-1
        
       

        

parser=argparse.ArgumentParser(description="need inputfile and outputfile")
parser.add_argument("-i","--input",default='in.csv',help="inputfile name")
parser.add_argument('-o','--output',default='out.csv',help="outputfile name")
args=parser.parse_args()

if args.input:
    txt_reader(args.input)