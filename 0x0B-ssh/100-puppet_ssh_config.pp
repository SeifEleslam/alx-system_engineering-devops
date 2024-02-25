# Edit ssh configuration
file_line { '/etc/ssh/sshd_config':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/id_rsa',
}
file_line { '/etc/ssh/sshd_config':
  ensure => present,
  line   => 'PasswordAuthentication no',
}
