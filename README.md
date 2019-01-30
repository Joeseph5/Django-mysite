# Django-mysite

## Quick Start

### Environment Setting

```shell
# 生成并激活env环境
python3 -m venv env
source env/bin/activate
# 安装运行环境所需要的库
pip install -r requirement.txt
# 更新db.sqlite
python manage.py migrate
# 没有admin用户，需要重新创建
# 出现database无法读写、打开问题，更改database权限：
chown www-data. .
```

### polls app：

- 安装软件：
  pip install django-polls/dist/django-polls-0.1.tar.gz
- 查看安装情况：
  pip list
- 配置 mysite 中的 urls 与 settings，详见 django-polls/READEM.md
- 卸装软件：
  pip uninstall django-polls

## Environment

- requirement.txt
