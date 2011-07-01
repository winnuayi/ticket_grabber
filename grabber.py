import urllib
import urllib2
import socket
import cookielib

URL = 'https://ibb.garuda-indonesia.com/ibp/'

values = {
    'autoOrigin' : "Jakarta, Soekarno Hatta Arpt (CGK)",
    'autoDest' : "Balikpapan, Sepingan Arpt (BPN)",
    'Params[tripType]' : 'r',
    'Params[origin]' : 'CGK',
    'Params[dest]' : 'BPN',
    'Params[adults]' : '1',
    'Params[childs]' : '0',
    'Params[outDate]' : '2011-07-02',
    'Params[retDate]' : '2011-07-04',
    'Params[serviceClass]' : 'eco',
    'Params[searchBy]' : 'date'
}

# Table mapping response codes to messages; entries have the
# form {code: (shortmessage, longmessage)}.
responses = {
    100: ('Continue', 'Request received, please continue'),
    101: ('Switching Protocols',
          'Switching to new protocol; obey Upgrade header'),

    200: ('OK', 'Request fulfilled, document follows'),
    201: ('Created', 'Document created, URL follows'),
    202: ('Accepted',
          'Request accepted, processing continues off-line'),
    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
    204: ('No Content', 'Request fulfilled, nothing follows'),
    205: ('Reset Content', 'Clear input form for further input.'),
    206: ('Partial Content', 'Partial content follows.'),

    300: ('Multiple Choices',
          'Object has several resources -- see URI list'),
    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
    302: ('Found', 'Object moved temporarily -- see URI list'),
    303: ('See Other', 'Object moved -- see Method and URL list'),
    304: ('Not Modified',
          'Document has not changed since given time'),
    305: ('Use Proxy',
          'You must use proxy specified in Location to access this '
          'resource.'),
    307: ('Temporary Redirect',
          'Object moved temporarily -- see URI list'),

    400: ('Bad Request',
          'Bad request syntax or unsupported method'),
    401: ('Unauthorized',
          'No permission -- see authorization schemes'),
    402: ('Payment Required',
          'No payment -- see charging schemes'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'Nothing matches the given URI'),
    405: ('Method Not Allowed',
          'Specified method is invalid for this server.'),
    406: ('Not Acceptable', 'URI not available in preferred format.'),
    407: ('Proxy Authentication Required', 'You must authenticate with '
          'this proxy before proceeding.'),
    408: ('Request Timeout', 'Request timed out; try again later.'),
    409: ('Conflict', 'Request conflict.'),
    410: ('Gone',
          'URI no longer exists and has been permanently removed.'),
    411: ('Length Required', 'Client must specify Content-Length.'),
    412: ('Precondition Failed', 'Precondition in headers is false.'),
    413: ('Request Entity Too Large', 'Entity is too large.'),
    414: ('Request-URI Too Long', 'URI is too long.'),
    415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
    416: ('Requested Range Not Satisfiable',
          'Cannot satisfy request range.'),
    417: ('Expectation Failed',
          'Expect condition could not be satisfied.'),

    500: ('Internal Server Error', 'Server got itself in trouble'),
    501: ('Not Implemented',
          'Server does not support this operation'),
    502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
    503: ('Service Unavailable',
          'The server cannot process the request due to a high load'),
    504: ('Gateway Timeout',
          'The gateway server did not receive a timely response'),
    505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
}


url = 'https://ibb.garuda-indonesia.com/ibp/'
timeout = 15

socket.setdefaulttimeout(timeout)
# unnecessary
#user_agent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30"
#headers = {'User-Agent' : user_agent, 'Content-type' : "application/x-www-form-urlencoded"}

data = urllib.urlencode(values)

# unnecessary
#request = urllib2.Request(url, data, headers)

request = urllib2.Request(url, data)

try:
    response = urllib2.urlopen(request)
except URLError, e:
    print e.code
    print e.read()

cookies = cookielib.CookieJar()
cookies.extract_cookies(response, request)

cookie_handler = urllib2.HTTPCookieProcessor(cookies)
redirect_handler = urllib2.HTTPRedirectHandler()
opener = urllib2.build_opener(redirect_handler, cookie_handler)

second_response = opener.open(request)

html = second_response.read()

print html
