# Edit ssh configuration
file_line { 'SSHConfig[KeyPath]':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'SSHConfig[NoPwd]':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
