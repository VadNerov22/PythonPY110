import re

ip4 = re.compile(r"""
    (?:(?:25[0-5]| # 250-255
          2[0-4][0-9]|  # 200-249
          [01]?[0-9]?[0-9])\.){3} # 0 - 199
          (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])
""", re.VERBOSE)


if __name__ == "__main__":
    log_dump = """
    66.249.73.185 - - [17/May/2015:11:15:58 +0000] "GET stash-1/ HTTP/1.1" 304 - "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    74.125.176.81 - - [17/May/2015:12:23:28 +0000] "GET /?flav=rss20 HTTP/1.1" 200 29941 "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"
    66.249.73.135 - - [17/May/2015:15:31:14 +0000] "GET /blog/geekery/xdot/presentations/logool-2.20110530.html HTTP/1.1" 200 11936 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    187.45.193.158 - - [17/May/2015:18:47:54 +0000] "GET /presentations/logstash-1/file/about-me/tequila-face.jpg HTTP/1.1" 200 196054 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 2.0.50727; InfoPath.1)"
    90.220.199.149 - - [17/May/2015:21:55:18 +0000] "GET /blog/geekery/puppet-manage-homedirectory-contents.html HTTP/1.1" 200 10001 "https://www.google.co.uk/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
    """
    print(ip4.findall(log_dump))
