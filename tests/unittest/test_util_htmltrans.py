from pydocbuild.util.htmltrans import *

html = """
html = '''

<html>
　　<head>
　　　　<meta name="content-type" content="text/html; charset=utf-8" />
　　　　<title>友情链接查询 - 站长工具</title>
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
　　　　<meta name="Keywords" content="友情链接查询" />
　　　　<meta name="Description" content="友情链接查询" />

　　</head>
　　<body>
　　　　<h1 class="heading">Top News</h1>
　　　　<p style="font-size: 200%">World News only on this page</p>
　　　　Ah, and here's some more text, by the way.
　　　　<p>... and this is a parsed fragment ...</p>

　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a>
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>

　　</body>
</html>
"""

class TestHtmlTransformations :

    def test_html_table_to_csv(self) :
        e = HtmlTableToCsvCode()
        s = "<table><tr><td>1</td><tr></table>"
        assert e.filter(s) == "<html><body>" + """<pre class="csv"><code>|1-1|1\n</code></pre>""" + "</body></html>"

    def test_lxml_html_cleaner(self) :

        LxmlHtmlCleaner().clean_from(html)
        assert True

    def test_bs4_html_filter(self) :

        html = """<html><body><a id="hello" href="baidu.com" class="class">hello</a></body></html>"""
        assert """<a class="class" href="baidu.com" id="hello">hello</a>""" \
            == InternalHtmlSelector("id", "hello").select_from(html)
        assert """<a class="class" href="baidu.com" id="hello">hello</a>""" \
            == InternalHtmlSelector("class", "class").select_from(html)
        assert """<a class="class" href="baidu.com" id="hello">hello</a>""" \
                == InternalHtmlSelector("css", "a").select_from(html)
        assert """<a id="hello" href="baidu.com" class="class">hello</a>""" \
                == InternalHtmlSelector("xpath", "//a").select_from(html)
