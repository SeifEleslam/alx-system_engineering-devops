# Create School File
file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
