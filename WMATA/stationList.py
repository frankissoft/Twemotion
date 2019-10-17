import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json

headers = {
    'api_key': '148b1a44ebc94ba2a036823ba7b023db'
}

# lines = {'RD', 'YL', 'GR', 'BL', 'OR', 'SV'}

params = urllib.parse.urlencode({
    # 'LineCode': "YL", "RD", "GR", "BL", "OR", "SV",
    # 'LineCode': 'RD',
    # 'LineCode': 'YL',
    # 'LineCode': 'GR',
    # 'LineCode': 'BL',
    # 'LineCode': 'OR',
    'Linecode': 'SV',
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request('GET', "/Rail.svc/json/jStations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(json.dumps(data.decode('UTF-8'), indent=4))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
