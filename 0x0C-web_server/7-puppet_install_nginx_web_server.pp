# Install NGINX
package { 'nginx':
  provider => 'apt',
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
file { '/etc/nginx/sites-available/default':
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

# Enable the redirection configuration by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart NGINX
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
