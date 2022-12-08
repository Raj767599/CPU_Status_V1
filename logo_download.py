import urllib
import requests

imgs=str(input("Enter The URL for logo downlod= "))


urllib.request.urlretrieve(imgs, f'logo.png')
print("downlod succcesfully")

