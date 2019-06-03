import sys
import re
import requests 

share_base = 'https://h5.pipix.com/s/'
json_url = 'https://h5.pipix.com/bds/webapi/item/detail/'

share_id = sys.argv[1]

share_url = share_base + share_id

json_object_request = requests.get(url = share_url)

item_url = json_object_request.url

url_pattern = r'https://h5.pipix.com/item/(.*)\?.*'

url_search = re.findall(url_pattern, item_url)
try:
    item_id = url_search[0]
except:
    print("Short code is not valid")
    exit

json_object_request = requests.get(url = json_url, params = {'item_id': item_id}) 

video_url = json_object_request.json()['data']['item']['origin_video_download']['url_list'][0]['url']

# URL of the image to be downloaded is defined as image_url 
r = requests.get(video_url) # create HTTP response object 
  

with open(item_id + '.mp4','wb') as f: 
    f.write(r.content) 
