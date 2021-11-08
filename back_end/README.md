# README

后端框架结构：

`controllers`——装载各种视图`url`

* `__init__.py`

  入口文件

* `login.py`

  登录视图`url`

* `register_user.py`

  注册视图`url`

`services`——装载各种视图对应的功能

* `__init__.py`

  入口文件

* `login_service.py`

  登录功能实现

* `register_user_service.py`

  注册功能实现

`static`——装载静态文件

`templates`——装载模版文件

`test`——装载测试文件

* `login_test.py`

  测试登录功能

* `register_user_test.py`

  测试注册功能

`app.py`

注册蓝图，返回`app`实例

`headers.py`

定义常量

`manage.py`

运行`flask`后端入口文件，运行主函数即可