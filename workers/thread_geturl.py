import cfscrape

request = "GET / HTTP/1.1\r\n"

cookie_value, user_agent = cfscrape.get_cookie_string(
    "http://ab4.cdn.vizplay.org/v/9a6e0341fc4455d427998f64c7302a8c.mp4?st=D8XtHFTHAawXjBCQVuD39g&hash=r7eBYMQox1UUBcic_XS_nA")
request += "Cookie: %s\r\nUser-Agent: %s\r\n" % (cookie_value, user_agent)

print request
