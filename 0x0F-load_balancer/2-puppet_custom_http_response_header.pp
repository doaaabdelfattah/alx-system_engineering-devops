# Install NGINX
package { 'nginx':
  ensure => 'installed',
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
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
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

  # Add custom HTTP header X-Served-By with the hostname of the server
  add_header X-Served-By \$hostname;

}
",
}

# Enable the redirection configuration using nginx::resource::vhost
nginx::resource::vhost { 'default':
  ensure => present,
}

# Restart NGINX
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
