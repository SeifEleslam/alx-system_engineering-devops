# Update before installation
exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}

# Install nginx with puppet
package { 'nginx' :
  ensure   => latest,
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
    }
    error_page 404 /404.html;
}
",
}

# Restart Service
service { 'nginx':
  ensure => running,
  enable => true,
}
