# create file in tmp

file { 'school':
    ensure => 'present',
    content => 'I love Puppet',
    path => '/tmp/school',
    mode => '0744',
    owner => 'www-data',
    group => 'www-data'
}
