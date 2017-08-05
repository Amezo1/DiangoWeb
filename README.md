# DiangoWeb Example


1、软件安装
brew search xx
brew install xx
--安装pip
sudo easy_install pip 
--安装sql orm
sudo pip install SQLAlchemy
--在~/.bash_profile中添加，使用命令行方式打开Sublime
alias subl="'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl'"

2、postgres数据
启动
pg_ctl -D /usr/local/var/postgresql@9.5 start
停止
pg_ctl -D /usr/local/var/postgresql@9.5 stop
客户端连接:qianfen/postgres  5432
psql -d postgres -h localhost -U qianfen

3、python数据库插件安装
http://initd.org/psycopg/download/
python setup.py build
sudo python setup.py install
ls -lrt /Library/Python/2.7/site-packages/
import psycopg2

4、安装Django
http://www.runoob.com/django/django-first-app.html
sudo pip install Django
--创建项目
django-admin.py startproject HelloWorld
--启动服务器，运行参数设置:runserver 0.0.0.0:8080
python manage.py runserver 0.0.0.0:8080
http://localhost:8080
http://localhost:8080/hello

--定义模型,数据库,cd HelloWorld,在HelloWorld项目目录下面
django-admin.py startapp TestModel
python manage.py migrate
python manage.py makemigrations TestModel
python manage.py migrate TestModel 

http://localhost:8080/dbinsert
http://localhost:8080/dbselect
http://localhost:8080/dbupdate
http://localhost:8080/dbdelete

http://localhost:8080/search
http://localhost:8080/searchpost
--manage.py需要设置编码，否则提交时编码错误
import sys
#否则会报错：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding('utf8')

--admin管理工具
http://localhost:8080/admin
--来创建超级用户
python manage.py createsuperuser 

--nginx
sudo pip install uwsgi
uwsgi --version
1、下载 PCRE 安装包，下载地址： http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
./configure
make && make install
pcre-config --version

uwsgi --http :8080 --chdir=/Users/qianfen/Documents/workspace/DjangoWeb/src --module=DjangoWeb.wsgi:application 
http://localhost:8080/searchpost
uwsgi --ini /Users/qianfen/Documents/workspace/etc/uwsgi8080.ini 
http://localhost:8080/searchpost

cd nginx-1.9.9
./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/Users/qianfen/Downloads/pcre-8.41
sudo make install
NGINXHOME=/usr/local/webserver/nginx
export PATH="/usr/local/opt/postgresql@9.5/bin:$NGINXHOME/sbin:$PATH"
nginx -v

uwsgi --ini /Users/qianfen/Documents/workspace/etc/uwsgi8080.ini 
sudo /usr/local/webserver/nginx/sbin/nginx 

http://localhost/DjangoWeb/search



--人脸识别
http://www.toutiao.com/i6447669480532214286/?tt_from=weixin_moments&utm_campaign=client_share&from=timeline&app=news_article&utm_source=weixin_moments&isappinstalled=1&iid=12156512852&utm_medium=toutiao_ios&wxshare_count=2&pbid=19388573246
https://github.com/ageitgey/face_recognition#face-recognition
https://face-recognition.readthedocs.io/en/latest/readme.html#installation
API 文件地址：https://face-recognition.readthedocs.io

brew install cmake
./bootstrap.sh --with-libraries=python
./b2
sudo ./b2 install
python -m pip install --upgrade pip
pip install --upgrade pip
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install numpy --upgrade --ignore-installed
pip install scipy --upgrade --ignore-installed
pip install scikit-learn --upgrade --ignore-installed
pip install face_recognition

--可能会报错scipy-0.13.0b1卸载不成功，可以用下面命令解决
重启电脑,长按Command+r 
csrutil disable
reboot


--uwsgi8080.ini
[uwsgi]
#http = :8080
socket = :8080
#uwsgi-socket = :8080
#项目根目录
#chdir = /Users/qianfen/Documents/workspace/DjangoWeb/src
#uwsgi文件，注意不用把后缀.py加上去    
#module = DjangoWeb.wsgi:application 
master = true         
vhost = true          
no-site = true        
workers = 2           
reload-mercy = 10     
vacuum = true        
max-requests = 1000   
limit-as = 512
buffer-size = 30000
pidfile = /Users/qianfen/Documents/workspace/etc/uwsgi8080.pid
daemonize = /Users/qianfen/Documents/workspace/etc/uwsgi8080.log


--nginx.conf
`
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
		    include  uwsgi_params;
            uwsgi_pass  127.0.0.1:8080;              #必须和uwsgi中的设置一致
            uwsgi_param UWSGI_SCRIPT DjangoWeb.wsgi;  #入口文件，即wsgi.py相对于项目根目录的位置，“.”相当于一层目录
            uwsgi_param UWSGI_CHDIR /Users/qianfen/Documents/workspace/DjangoWeb/src;       #项目根目录
            index  index.html index.htm;
            client_max_body_size 35m; 
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
`










