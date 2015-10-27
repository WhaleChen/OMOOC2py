# 用官方文件解决问题教训和总结

**解决问题的顺序**
- 提出问题
- 仔细思考完善问题 
- 参考最直接的方法，花大力气
- 寻找其他线索，花小力气

使用Tkinter ，本以为是一件很容易的事情，自以为学过一些VB，似乎30min就可以完成。
却发现，自己用了2个小时才找到问题。其实，我一直被一个问题阻碍：

> “在Tkinter中使用Entry widget 输入文字后如何确认输入的内容已经完成并用get来完成提取？”

似乎按ENTER是理所应当的，不过我一直无法成功完成获取entry的输入内容。
我发现自己有两个梗：
- 不喜欢将问题清晰化就急急下手解决； 
- 不喜欢用显而易见的东西解决问题。

这使得自己在自认为容易的事情上不能够一次性完成我就特别焦急。
焦急也没有解决方案。不断在网上搜索。
读一些看似高深，但其实无用的资料：比如

http://effbot.org/tkinterbook/entry.htm

http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry.html

这实在是无意义的尝试，因为我官方文献没有读。
我的flow是这样的：我初步看看官方文件，没有 entry的 主题，就离开了。

最后，我在万般无奈之下，才借助 搜索功能，将官方文件 entry相关点 搜索出来。

https://docs.python.org/2.7/library/tkinter.html

可是要知道，这一篇文章不断放在卡片背面！

    self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

目标代码终于找到，自己的梗则需要大大磨砺
