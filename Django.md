# Django

## Test

- `python manage.py test polls` 将会寻找 `polls` 应用里的测试代码，可以定位 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/2.1/topics/testing/tools/#django.test.TestCase) 的子类中的方法。

## 软件复用

参考：https://docs.djangoproject.com/zh-hans/2.1/intro/reusable-apps/

## server

fg重新前台运行，ctrl+z:挂起， ctrl+c：停止

## Apache2

### apache2 部署django

1. 安装apache2

2. 修改配置文件：/etc/apache2/apache.conf

3. 参考：https://my.oschina.net/skymyyang/blog/816173

   ```shell
   WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
   WSGIPythonHome /path/to/venv
   WSGIPythonPath /path/to/mysite.com
   
   <Directory /path/to/mysite.com/mysite>
   <Files wsgi.py>
   Require all granted
   </Files>
   </Directory>
   // 具体如下：
   WSGIScriptAlias / /home/ubuntu/Django-mysite/mysite/wsgi.py
   WSGIPythonHome /home/ubuntu/Django-mysite/env
   WSGIPythonPath /home/ubuntu/Django-mysite
   
   <Directory /home/ubuntu/Django-mysite/mysite>
   <Files wsgi.py>
   Require all granted
   </Files>
   </Directory>
   ```

### admin无css样式

django的静态文件static未加载。

1. 复制static文件至指定目录，执行python manage.py collectstatic

   ```python
   # setting.py
   # add admin css
   STATIC_ROOT =  os.path.join(BASE_DIR, "common_static")
   STATIC_URL = '/static/'
   STATICFILES_DIRS = (
   os.path.join(
           BASE_DIR, "env/lib/python3.5/site-packages/django/contrib/admin/static/"),
   )
   ```

2. 配置apache2中的static样式。

   sudo vim /etc/apache2/apache2.conf

   ```shell
   Alias /static/ /home/ubuntu/Django-mysite/common_static/
   <Directory /home/ubuntu/Django-mysite/common_static/>
   Require all granted
   </Directory>
   ```

   