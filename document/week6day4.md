# 第七周纪要：玩耍自动化代码

keyword: 
主动思维 自动化 手机 MVP

## 第一点：自动化
- 文档本地化：get 
- DSL：领域专用语言
- 分组 别名
- [NARKOZ](http://www.leikeji.com/article/3838) 的例子[github](https://github.com/NARKOZ/hacker-scripts)

> that type of a guy who loves Vim, creates diagrams in Dot and writes wiki-posts in Markdown . If something - anything - requires more than 90 seconds of his time, he writes a script to automate that.

NARKOZ 让我兴奋了很久，一直在说提升效率，实际上是用程式替代重复行动的方式。这种思维习惯本身也是程式。只是是一种迭代后会倍增的迭代。
我开始回顾自己一直在做的事情，发现可以改进和程式化的太多了。比如开机吧，鼠标点了不止10下。OK，发现自己做的无非是同样的事情，然后看到其实先人早已不用如此愚蠢的策略了。
仔细想，如果要自动化，其实需要两个过程，一个是记录并自觉，通过重复的过程的不断记录让自己意识到到底是什么在不断重复，消耗自己不必要的精力和时间，同时将可重复的尽可能录制，
另一个就是学习和使用技术来完成这些循环的简化工作。有些工作太琐碎，暂时不能程式化，比如打扫卫生，那么就向那些做此工作的人致以敬意，并将精力放在那些容易程式化的地方。
### 梗点：
- 做事无序，效率低下
- 情绪起伏不定 
- 行动有始无终，有预想没有计划

### 改进：
- 点醒自醒：知道自己在重复劳动，很奇怪喜欢醉的感觉，就如同一种瘾，而NARKOZ的行为点醒了我，以后常常自醒
- 记录一切可记录的：记录让我们重构我的记忆
- 万事计划先：
- 使用一些有趣的高效软件，推荐 [AutoHotkey](http://ahkscript.org/)，在win档其实也可以玩自动化。慢慢和鼠标兄弟说Goodbye！
- 

## 第二点：手机和Qpython
- 手机Adroid系统一直让我感觉觉得很神奇！在大妈的讲解下才发现，不过是Linux！接近惊呼的状态！
- 获得root其实还需要一个过程的，详细看本周的作业
- 然后就是一大堆的东东搞不太懂busybox SHHDroid,不过既然手机就是linux，那么，你懂得~ 最小代价！

### 梗点：
- 不同手机真的不一样。发现我用的华为和苹果就大不相同。都是品牌惹的祸！
- 使用手机的习惯。其实手机中的一些习惯还真的比较无效，比如我浏览微信的方式，我统计就发现很无效，都属于用眼睛找的状态。那么小的一个屏幕~

### 改进：
- 读manual 按规矩来。没办法，这是必须的。
- 用busybox 和电脑来访问手机，就如同大妈演示的一样。
- 寻找手机的一些高效软件。不断更新效能储备。

## 第三点：源头和进化MVP
- 最精确的地方，来自于源头。
- 感性演示：大妈说自己是感性演示，那确实足够吸引我，让我觉得生活真的很美好！
- MVP Plan Do Check Act 迭代

### 梗点：
- 读原文有吃力：总觉得文档太枯燥了，同时一些东西都太琐碎。
- 勤于迭代这段有待加强：似乎交了作业就大功完成了。
- 喜欢直接看结果：总觉得看到的心里才踏实。

### 改进：
- 游玩原文：我主要觉得自己不喜欢读原文这件事情来自于一种情绪，既然只是情绪，那么就试着反情绪。去喜欢自己不喜欢的。这种尝试是一种突破情绪的做饭。难道不觉得自己总在“看原文就觉得烦”上很无聊吗？
- “看到原文，烦” ：
  逻辑
  
```  
if 看到原文：
    烦
```

- 不觉得很可笑吗？不好玩那~
- 迭代的问题在于其实作业是我们的帮助，并不是用来炫耀我有多棒的，而是来帮助我去进一步学习的，既然这样，自己已经搭建的东西当然最有价值。这段时间比较不愿修改也有原因，因为之前疲于赶进度。那么接下来就是迭代的最佳训练时机了。 
- 计算机英语可是最畅通的语言呢，Why not learn or just repeat as learning to sing?          


## [Google Python Style](https://google.github.io/styleguide/pyguide.html)英文版 这次放英文了
- 每周学一点，这应该是可以的
- 本周学到的：
- 打开文件类型的方式：[with](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement)
```
with open("hello.txt") as hello_file:
    for line in hello_file:
        print line
```
使用 contextlib 来处理网页型的文件打开, [contextlib](https://docs.python.org/2/library/contextlib.html) 阅读起来还真的需要一些音乐。

```
import contextlib

with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
    for line in front_page:
        print line
```
这样做是为了保证文件在执行完成后被有效关闭。

## 团队合作
- 期待和大家的合作

#### 一段文字：

> Coming together is a beginning;
keep together is a process;
working together is a success!

    from Henry Ford

#### 一段音乐：
- [自新大陆](http://music.baidu.com/album/48345740) from 德沃夏克
- 这是我第一次接触古典听的第一首交响乐，我发现，我被深深吸引了，那是15年前的事情了。
- 德沃夏克，在过了50岁之后，才到了美国，这个充满这热情和新气息的世界中，而我，也已经30了，这首歌恰能反应出当下我的心情。似乎又回到了中学的时代~真的很喜欢这个课程！
- 人生苦短，Python当歌 
