#base image

FROM centos:latest

# MAINTAINER
MAINTAINER chanxing9@gmail.com

RUN yum update && yum -y install httpd && yum -y \
    install mariadb-server mariadb-client && yum -y install git\
    yum -y install vim && yum -y install curl && yum -y install php\
    yum -y install php-mysql
RUN rm -rf /var/www/html/*

RUN git clone https://github.com/Audi-1/sqli-labs.git "/var/www/html/"

ADD ./sqli_lab.sh /etc/init.d/sqli_lab.sh
RUN chmod 755 /etc/init.d/sqli_lab.sh
CMD ["/etc/init.d/sqli_lab.sh"]
