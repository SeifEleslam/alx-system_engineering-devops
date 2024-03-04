# Install nginx with puppet
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
package { 'nginx' :
  ensure   => latest,
}
# Configure the server block for our site.
file { '/var/www/html':
  ensure => directory,
  owner  => root,
  group  => root,
  mode   => '0755',
}
# Create a simple index.html file to test the
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => root,
  group   => root,
  mode    => '0644',
  content => 'Hello World!',
}
# Configure server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => root,
  group   => root,
  mode    => '0644',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location / {
      add_header X-Served-By ${hostname};
    }}
",
}
# Restart Service
exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
