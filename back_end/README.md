# README

后端框架结构：

`config`——装载一些配置

* `settings.py`

  设置文件


`controllers`——装载各种视图`url`

* `__init__.py`

  入口文件

* `activate.py`

  激活用户视图`url`

* `login.py`

  登录视图`url`

* `register_user.py`

  注册视图`url`

`demo`——存放各种临时的`demo`测试文件，和项目无关，最终会统一删除

`services`——装载各种视图对应的功能

* `__init__.py`

  入口文件

* `login_service.py`

  登录功能实现

* `mail_service.py`

  邮箱认证功能实现

* `mysql_service.py`

  封装数据库操作为类

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

### run with gunicorn

```bash
gunicorn -w4 -b 0.0.0.0:5000 --log-level=debug manage:app
```

### start nginx

```bash
docker run --name nginx_SEP -p 8080:80 -d nginx
```