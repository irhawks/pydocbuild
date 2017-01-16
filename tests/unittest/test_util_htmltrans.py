from pydocbuild.util.htmltrans import *

class TestHtmlTransformations :

    def test_html_table_to_csv(self) :
        e = HtmlTableToCsvCode()
        s = "<table><tr><td>1</td><tr></table>"
        assert e.filter(s) == "<html><body>" + """<pre class="csv"><code>|1-1|1\n</code></pre>""" + "</body></html>"
