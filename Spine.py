from email import header
import requests

while True:
	v =  input("Link: ")
	h = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
	}
	r = requests.get(v, headers=h).text.split('"preloadList":[{"url":"')[1].split('?a=')[0].replace("\\u002F", "/")
	open(v.split("video/")[1]+".mp4", "wb").write(requests.get(r, headers=h).content)