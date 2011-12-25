import sys
import os
sys.stdout.write("""worker_processes 1;
daemon off;
error_log run/error.log;
events {
    worker_connections  1024;
}
http {
    server {
        access_log run/access.log;

        client_body_temp_path run/client-body-temp 1 2;
        proxy_temp_path run/proxy-temp 1 2;
        fastcgi_temp_path run/fastcgi-temp 1 2;
        uwsgi_temp_path run/uwsgi-temp 1 2;
        scgi_temp_path run/scgi-temp 1 2;

        listen       %s default_server;
        location / {
            proxy_pass http://unix:run/gunicorn.sock;
        }
    }
}
""" % (os.environ['PORT'],))
