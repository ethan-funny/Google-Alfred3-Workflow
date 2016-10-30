目录
===

* [安装](#安装)
* [配置](#配置)
* [使用](#使用)
* [存在的问题](#存在的问题)


# 安装

下载 [Google-Alfred3-Workflow.alfredworkflow](https://github.com/ethan-funny/Google-Alfred3-Workflow/raw/master/Google-Alfred3-Workflow.alfredworkflow)，然后双击将其导入 **Alfred 3**。

# 配置

本插件需要访问 google，因为众所周知的原因，所以在使用之前，需要先进行配置。

- **如果你使用的是 [Surge](http://nssurge.com/)**，你可以将它设置为 `系统代理`，然后就可以使用了，比如使用 `gs react` 进行搜索，可在 [Surge](http://nssurge.com/) 的 dashboard 界面看到请求记录：

![surge](http://i.imgur.com/aPPeWq1.png)

- **如果你使用的是 VPN**，也可以直接使用

- **如果你使用的是 shadowsocks**，可以参考下面的配置

本插件提供了 `socks5` 代理的设置，以便可以访问谷歌，这就需要你本机已经配置好了 `socks` 代理。如果你用 [shadowsocks](https://shadowsocks.com/)，本机电脑使用的是 `GoAgentX`，`GoAgentX` 的配置类似如下：

![goagentx](http://7xiht5.com1.z0.glb.clouddn.com/goagentx.png-ab)

Alfred 插件的配置只需要配置本地的代理端口，比如 GoAgentX 中的本地端口是 1234，那么 Alfred 插件的代理端口也要配置 1234，输入 `gsc 1234`，如下：

![configure proxy port](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/config-proxy-port.png)

配置好后，使用 `gs react` 进行搜索，应该可以在 GoAgentX 中看到请求记录，如下：

![goagentx](http://i.imgur.com/qmSXmOb.png)

**如果你不想用 socks 代理的话（默认是关闭的），你可以输入 `gsc 0`。**

# 使用

在使用之前请确保：

- 使用 `Alfred 3` 而不是 `Alfred 2`
- 可以科学上网

触发关键字 `gs`: 根据提供的关键词进行搜索，并给出搜索结果，如果你没有给出关键字，插件会自动使用你最近拷贝的字符作为关键词。

![google-search-result-1](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/google-search-1.png)

![google-search-result-2](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/google-search-2.png)

# 一些技巧

- `Enter` 键直接在浏览器打开选中的链接

- `Command + y` 键可以对链接的内容进行预览

![quicklook](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/quicklook.png)

- `Command + Enter` 键直接复制选中的链接

![copy-link](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/copy-link.png)

- `Option + Enter` 键用 `markdown` 形式复制选中的链接

![copy-link-with-markdown-format](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/copy-link-with-markdown-format.png)


# 存在的问题

- 目前插件还不是很完善，发现如果使用 `GoAgentX + shadowsocks`，有时会搜不出结果，期待你的 `pull request`.


# Copyright

The MIT License (MIT)

Copyright (c) 2016 [ethan-funny](https://github.com/ethan-funny)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


