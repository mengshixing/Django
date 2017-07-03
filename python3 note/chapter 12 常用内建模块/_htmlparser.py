#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#爬取html页面可以通过HTMLParser来解析

#原来是print()函数自身有限制，不能完全打印所有的unicode字符。
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

from html.parser import HTMLParser
from html.entities import name2codepoint

#http://blog.csdn.net/tianxicool/article/details/5942523


class myhtmlparser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        pass
        print('handle_starttag',tag,attrs)
        
    def handle_endtag(self,tag):
        pass
        print('handle_endtag',tag)
        
    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag <%s/>' % tag)

    def handle_data(self, data):
        print('handle_data',data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
        
parser = myhtmlparser()
parser.feed('<html>\
<head></head>\
<body>\
<!-- test html parser -->\
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>\
</body></html>')


# HTMLParser.handle_starttag(tag, attrs)

# 该方法用来处理一个标记的开始。通常被派生类重载；基类的实例什么都不做。
# tag 参数是 tag 的名字的小写化。 attrs 参数是一个 list ，由 (name, value) 组成，反映了 <> 里面的属性。 
# name 会被翻译成小写字母，在 value 中的引号也被移除了，字符实体引用也会被替换。
# 例如，有个 tag<A HREF=”http://www.cwi.nl/”> ，那么使用该方法就该这么做
# handle_starttag(’a’, [(’href’, ’http://www.cwi.nl/’)])
 
# HTMLParser.handle_startendtag(tag, attrs)
# 和 handle_starttag() 类似，用来处理 XHTML 风格的 空标签（ <a .../> ）。
# 可能被子类重载， which require this particular lexical information; 
# 默认的实现只是简单的调用 handle_starttag() 和 handle_endtag()

# HTMLParser.handle_endtag(tag)
# 该方法用来处理元素结束标记。可以被派生类重载；基类什么也不做。
# tag 参数是 tag 的 name 转化来的小写字母。

# HTMLParser.handle_data(data)
# 该方法用来处理随机的数据。可以被派生类重载；基类什么也不做。
 
# HTMLParser.handle_charref(name)
# 处理 &#ref 格式的字符引用。可以被派生类重载；基类什么也不做。
 
# HTMLParser.handle_entityref(name)
# 处理一般的 &name 格式的实体引用。 name 是一个一般的实体引用。
# 可以被派生类重载；基类什么也不做。 
	   	   
# HTMLParser.reset()
# 重置实例 . 所有未处理的数据都会丢失。在初始化时自动调用。
 
# HTMLParser.feed(data)
# 给分析器喂食。在由完整元素构成的情况下工作；不完整数据情况下，
# 会进行缓冲知道更多数据加进来或者 close() 被调用。

# HTMLParser.close()
# 处理所有缓冲数据。这个方法可以被派生类重定义，以便在输入结束后处理额外的事情
# 重定义的版本也要调用 HTMLParser 基类的 close() 方法。

# HTMLParser.getpos()
# 返回当前行数和列数 