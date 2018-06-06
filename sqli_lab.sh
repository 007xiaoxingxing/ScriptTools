#!/bin/bash

/usr/sbin/httpd -DFOREGROUND &
/usr/libexec/mariadb-prepare-db-dir %n && /usr/bin/mysqld_safe --basedir=/usr &
/bin/bash
