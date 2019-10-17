import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    'api_key': '148b1a44ebc94ba2a036823ba7b023db'
}

params = urllib.parse.urlencode({

})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/Rail.svc/json/jLines?%s" % params, "{YL}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data.decode('UTF-8'))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
