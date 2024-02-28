#Install NGINX
package { 'nginx':
    provider => 'apt',
}

# Main file for string
file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0744',
}

# Create directory to store HTML files
file { '/etc/nginx/html':
  ensure => directory,
}

# Create default index.html page
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# 301 Redirection file 
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  mode    => '600',
  content => "\
server {
  listen 80;
  listen [::]:80 default_server;
  root   /etc/nginx/html;
  index  index.html index.htm;

  location /redirect_me {
    return 301 http://youtube.com/;
  }
}
",
}

# Restart NGINX 
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}