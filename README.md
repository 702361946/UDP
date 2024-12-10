>IPv4&端口指定

configure.json里的IPv4有如下含义

| sys         | user       |
|-------------|------------|
| 服务器绑定的ip&端口 | 指定服务器地址和端口 |

>通用内容

sys(user)_configure.json里的通用内容

| 键名            | 值          | 效果        |
|---------------|------------|-----------|
| "user input"  | True&False | 启用&关闭用户输入 |
| "setblocking" | True&False | 开启&关闭阻塞模式 |

>消息键对

键是收到的消息,值是返回的内容

需要注意sys_exit不返回任何内容

前面加上"m:"表示方法

详细可见_sys_message.py中的变量_m

| 键           | 方法      | 结果                     |
|-------------|---------|------------------------|
| "r_help"    | 读help文件 | 向客户端发送help内容           |
| "handshake" | 握手      | 向客户端发送"handshake"以确认连接 |
| "sys_exit"  | 退出      | 退出服务器                  |