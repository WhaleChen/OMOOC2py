# 梗点：Gitbook 安装 disqus
仔细看自己 寻求问题的脉络是非常有趣的：
-第一周：用gitbook 的网上editor 写文档, disqus 无头绪！！
    + 用尝试和官方文档解决问题的尝试，无果 [gitbookdocument](https://help.gitbook.com/)
    + gitbook developers
-第二周：发现可以fork 大妈的book.json
    + 复制,粘贴：梗更大了
	+ 重复重复10次，完了~
-第三周：接到不用过于在意gitbook的通知，放弃disqus了
    + 没有任何努力
-第四周：大家又回到gitbook,很多同学的笔记都用gitbook,我也用
    + 希望装上disqus
	+ 内心深处说：这个问题那么小！
	+ 事实又说：这个问题我搞不定！
	+ 看到disqus 就挠头！郁闷哪！
	
-今天：寻找自己到底出问题在何处
    + 答应Cnfeat 要加上disqus. 汗死了，下定决心！
    + 放下自己，Enjoy the moment 

正确代码：
```
{
	
	"plugins": ["disqus"],
	"pluginsConfig": {
		"disqus": {
			"shortName": "WhaleChen"
		}
	}
}
```


## 实际梗点：
- ["disqus"] 没有引号
- shortname ShortName
- 最大的梗点: 我申请了两个 账号，我关联的是 whale_road_by_python 这个也是一直让我不能连上的关键！

## 思维梗点：
- 先自己凭猛劲尝试
- 不行寻求完全的倚靠，大妈救我！！
- 发现不行，就放弃~

## 改进：
- 方向正确间站定了
- 放松，寻求帮助，而非倒在大妈之下，复制粘贴？？NO
- Move 一步一步

### 问题终于解决：实际时间：15 min 郁闷：3 week
- 惊了~ 



