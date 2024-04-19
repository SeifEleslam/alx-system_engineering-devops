# Puppet script
exec { 'New User':
  command  => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
  provider => shell,
}
