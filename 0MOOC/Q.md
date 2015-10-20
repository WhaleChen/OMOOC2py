
Q0 : 为什么 gitbook 用户名被加了数字 1？    

A ：先注册 gitbook，然后 sign in with github ，二者用户名相同时，后注册的 username 就被自动加 1  

> 这个问题一般常识是 2 个账户 username 重复了，两个账号都是自己的话,删了一个就行 ；官方[说明](https://help.gitbook.com/account/duplicate.html)  

此外证据：sign in with github 前有意查看过用户名，没有数字；   
应该就是了，虽有疑惑：为什么同邮箱同用户名不合并或提示呢（预设 github 和 gitbook 原本就有关联）？  
以防万一邮箱登陆看看，结果`Invalid username/email or password`（确定没输错）     
(⊙_⊙)?!   
傻了   
判定：只有一个账号  
带上账号唯一，普通方式注册 gitbook 之印象模糊，被加数字 1 的时间点不确定的3个条件，问`为什么 gitbook 用户名被加了数字 1？ `

 
**接下来就是编制不存在问题缠死自己的过程：**     

- 明明只有一个账号，干嘛莫名其妙加 1 （对之前`sign in with git触发`的怀疑合理化了）

- 进而我对 gitbook 有了奇怪的联想：gitbook 因不同的登录方式分配账户副本（联想了 git ，gitbook——git + book 就更相信了）即同一账号的不同版本；
  - 用普通登陆切换过来：结果 username 还是带数字  
  - 结论：网页无法切换

- 此时 Q 已变成：如何切换 gitbook 账号的不同版本；
  - 当时对问题变更没有任何怀疑（自动：我要解决它）
  - 参考Google 搜索 'gitbook' 第五条： “……是命令行工具”（此时我还没看到 gitbook 长什么样的图片，就把 gitbook 当和 git 差不多）  
  - 可能性：CLI gitbook 命令可以设置
  - 目标：下载 gitbook 
  - 联动 gitbook 和 github 搜教程时我都没有下载，要栽倒这里 ？为了一个数字？ಥ_ಥ
  
- 痛苦：一边荒谬“为了个 book 还要搞个 gitbook 版的 git，功能肯定还没 git 全”，一边烦躁复杂性（gitbook 真是这么复杂的话，我真要为了个数字 1 去折腾吗）
  - 脑里面又想着 git，接着：
  - 可能性：当前账户在使用中（与 github 关联，有 book 内容），原版本没有，所以默认当前的版本，新版本没有了，原版本就回来了
  - 目标：删除当前版本
  - 账号好好的她哪里错了ಥ_ಥ
   
  
- 此时更混乱了，开始反复点击 sign in with github； 
- 隐隐觉得附近不对劲（是不是哪个判断的前提错了）；中间还有小插曲（登陆不了gitbook ，找回邮件延迟）；
- 去 issue 提问，大妈回复：  
  - `相同的操作期待出现不同的结果``一切开始……换一种方式`  
  
- 这时感觉情绪发生了什么微妙的化学反应，马上就执行：

  - 立即把账户删除，分别检查用户名和邮箱哪个在占用中
  - 结果是用户名占用，邮箱未被占用
  - 那么是注册时用的邮箱是另外的了(⊙_⊙)?! 
  - 立即去其他邮箱搜'github'，结果是没有验证邮件……
  - 这次倒是没有立即否定了；点找回，把其他邮箱都填了
  - 当时gitbook给力，2分钟收到了TAT
  - 找回那个原初账号，删除，重新sign in with git
  - 结束
  
- 最后，转变的问题不存在，原初的问题很简单，以及神经智力  


ps.这里挖坑的原因之`不想麻烦、尝试未知`也促成 找到任务简单路径（一边看教程不实施一边探索 settings）  
pps.哭着写完，感觉裤子开裆(￣∇￣*)    
  