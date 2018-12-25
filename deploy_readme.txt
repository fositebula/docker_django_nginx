sudo docker-compose build

sudo docker-compose up -d

sudo docker ps 找到docker_django_nginx_web的CONTAINER_ID

sudo docker exec -it CONTAINER_ID /bin/bash

执行 python manage.py createsuperuser创建超级用户

如果在浏览器上输入该电脑的ip地址不能访问到网页,需要查看web和nginx的log

python docker logs CONTAINER_ID, 一般是需要修改/nginx.conf中的server name