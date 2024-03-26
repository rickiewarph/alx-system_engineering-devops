#!/usr/bin/env bash
# Configures a server using puppet

# defining a Puppet class called nginx_server 
#  encapsulating config for the Nginx server.
class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

#  To manage the Nginx service.
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
# To manage Nginx config file located at /etc/nginx/sites-available/default.
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
      server {
        listen      80 default_server;
        listen      [::]:80 default_server;
        root        /var/www/html;
        index       index.html index.htm;

        location / {
          return 200 'Hello World!';
        }

        location /redirect_me {
          return 301 http://cuberule.com/;
        }
      }
    ",
    notify => Service['nginx'],
  }
}
#  To include the nginx_server class, ensuring that it gets applied.
include nginx_server
