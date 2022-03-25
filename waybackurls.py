import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='cc')
parser.add_argument('-u',type=str,required=False,help='输入url')
parser.add_argument('-f',type=str,required=False,help='输入文件')
parser.add_argument('-o',type=str,required=False,help='输出文件')
parser.add_argument('-d',type=str,required=False,help='子域名')
txt_file=parser.parse_args().o
host=parser.parse_args().u
txt_input=parser.parse_args().f
d=parser.parse_args().d

def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = str(r.content).replace("b'[[\"original\"],\\n[\"","").replace("\"],\\n[\"","\n").replace("\"]]\\n'","").replace("b'[]\\n'","")
    return results

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('-f 输入txt文件 -o 输出txt文件 -u 单个域名')
        sys.exit()
    with_subs = False
    if d:
        with_subs = True
    if host:
        print(host)
        try:
            urls = waybackurls(host, with_subs)
            #颜色
            print("\033[1;31m"+urls+"\033[0m")
            if txt_file:
                    with open(txt_file,"a") as object:
                        object.write(urls+"\n")
        except:
            pass
    else:
        for host in open(txt_input):
            print(host)
            try:
                urls=waybackurls(host, with_subs)
                #颜色
                print("\033[1;31m" + urls + "\033[0m")
                if txt_file:
                    with open(txt_file,"a") as object:
                        object.write(urls+"\n")
            except:
                continue
