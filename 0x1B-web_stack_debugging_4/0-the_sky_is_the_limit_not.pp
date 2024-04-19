# Puppet script
exec { 'Increase Limit' :
  command  => 'sed -i s/15/1000/ /etc/default/nginx',
  provider => shell,
}
-> exec {'Restart Nginx' :
  command  => '/usr/bin/env service nginx restart',
  provider => shell,
}
