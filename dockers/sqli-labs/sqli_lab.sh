#!/bin/bash
/usr/libexec/mariadb-prepare-db-dir %n
/usr/bin/mysqld_safe --basedir=/usr >/dev/null 2>&1 &
/usr/sbin/httpd -DFOREGROUND
