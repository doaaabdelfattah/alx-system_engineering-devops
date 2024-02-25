#using Puppet to make changes to our configuration file.
file { '/etc/ssh/ssh_config':
    ensure => present,
    mode => '600',
    content => "\
    Host 501006-web-01
        HostName 54.237.109.172
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
}