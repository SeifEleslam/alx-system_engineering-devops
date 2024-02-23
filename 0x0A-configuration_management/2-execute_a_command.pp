# Kill it with puppet
exec { 'pkill -f killmenow':
  path => '/usr/bin',
}
