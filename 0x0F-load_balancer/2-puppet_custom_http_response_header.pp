# Install nginx with puppet
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

-> package { 'nginx' :
  ensure   => latest,
}

# Configure server
-> file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

# Restart Service
-> service { 'nginx':
  ensure => running,
  enable => true,
}
-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
