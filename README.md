# Google Alfred 3 Workflow

The missing Alfred 3 Workflow for obtaining google search results based on your query, with some handy tips.

## Installation

Download the [Google-Alfred3-Workflow.alfredworkflow](https://github.com/ethan-funny/Google-Alfred3-Workflow/raw/master/Google-Alfred3-Workflow.alfredworkflow) and import to Alfred 3.

## Usage

Keyword `gs`: get google search results based on your query.

![google-search-result-1](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/google-search-1.png)

![google-search-result-1](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/google-search-2.png)

By default, the program runs without proxy. However, it may not work because some websites including google are blocked in some countries. Luckily, this workflow provides socks5 proxy so that the program can access google. To do this, you need to:

- Enable the socks5 proxy on your computer firstly. You may refer to [shadowsocks](https://shadowsocks.org/en/index.html).

- Launch Alfred and type `gsc` to configure your local socks proxy port.

![configure proxy port](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/config-proxy-port.png)


### Handy Tips

In addition to get google search results, this workflow also provides some wonderful tips.


- `Enter` key to open the selected item in default browser.

- `command + Enter` key to copy the link of the selected item.

![copy-link](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/copy-link.png)

- `option + Enter` key to copy the link with markdown format of the selected item.

![copy-link-with-markdown-format](https://raw.github.com/ethan-funny/Google-Alfred3-Workflow/master/screenshots/copy-link-with-markdown-format.png)

- `command + Y` key to quick look the selected item.


## Copyright

The MIT License (MIT)

Copyright (c) 2016 [ethan-funny](https://github.com/ethan-funny)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

