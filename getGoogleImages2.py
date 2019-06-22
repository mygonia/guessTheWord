from google_images_download import google_images_download 
import sys, re, pprint, json

urls = {}
def getURLs (noun):
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f

    response = google_images_download.googleimagesdownload()

    arguments = {"keywords"     : noun,
                 "limit"        : 4,
                 "print_urls"   : True,
                 "size"         : ">2MP",
                 "no_download": True,
                 }
    paths = response.download(arguments)

    sys.stdout = orig_stdout
    f.close()

    with open('URLS.txt') as f:
        content = f.read().splitlines()
    f.close()

    urlList = []
    for i in range(len(content)):
        line = content[i]
        if 'Image URL:' in line:
            separateAt = line.find(':')
            url = (line[separateAt + 2:])
            urlList.append(url)
    urls[noun] = urlList

f = open("nounlist.txt", "r", encoding='utf-8-sig')
for i in f.read().splitlines():
    if '-' not in i and ' ' not in i:
        print('Getting URLs for ' + i)
        try:
            getURLs(i)
        except:
            print('Failed to get URLs for ' + i)
            pass
    else:
        print('Skipped ' + i)

print('Making urlList.txt file')
with open('urlList.txt', 'w') as outfile:  
    json.dump(urls, outfile)

