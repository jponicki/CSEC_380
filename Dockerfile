FROM ubuntu

EXPOSE 80
EXPOSE 443

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python

RUN apt-get -y install python-mysqldb
RUN apt-get -y install ca-certificates
RUN apt-get -y install python-jwt

RUN a2enmod cgi
RUN a2enmod ssl
RUN a2dismod -f autoindex
RUN service apache2 restart
RUN rm -rf /var/www/html/*

RUN echo "                       \n \
<VirtualHost *:80>               \n \
   ServerAlias 127.0.0.1         \n \
   ServerName localhost          \n \
   redirect permanent / https://localhost \n \
<Directory /var/www/html/>       \n \
   Options -Indexes              \n \
</Directory>                     \n \
</VirtualHost>                   \n \
<VirtualHost *:443>              \n \
   AddType video/ogg .ogv        \n \
   AddType video/mp4 .mp4        \n \
   AddType video/webm .webm      \n \
   ServerName localhost          \n \
   ServerAlias 127.0.0.1         \n \
   DocumentRoot /var/www/html    \n \
   SSLEngine On                  \n \
   SSLCertificateFile /var/www/ca/server.crt \n \
   SSLCertificateKeyFile /var/www/ca/server.key \n \
<Directory /var/www/html>        \n \
   Options +ExecCGI -Indexes     \n \
   AddHandler cgi-script .py     \n \
   DirectoryIndex python/index.py\n \
</Directory>                     \n \
<Directory /var/www/html/python> \n \
   Options +ExecCGI -Indexes     \n \
   AddHandler cgi-script .py     \n \
</Directory>                     \n \
</VirtualHost>                   \n \
" >> /etc/apache2/apache2.conf


COPY ca /var/www/ca
COPY webapp/ /var/www/html/
RUN mkdir -p /var/www/html/videos

RUN chmod -R u+rwx,g+x,o+x /var/www/html
RUN chgrp -R www-data /var/www/html/videos
RUN chmod -R g+rwx /var/www/html/videos

RUN ln -sf /usr/bin/python /usr/local/bin/python
RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stderr /var/log/apache2/error.log
CMD /usr/sbin/apache2ctl -D FOREGROUND
