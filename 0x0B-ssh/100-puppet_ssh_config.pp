# create a file
node default {
  $str = sprintf("%s\n%s\n%s\n%s\n%s\n%s\n%s\n",
    'Include /etc/ssh/ssh_config.d/*.conf',
    'Host *',
    'PasswordAuthentication no',
    'IdentityFile ~/.ssh/school',
    'SendEnv LANG LC_*',
    'HashKnownHosts yes',
    'GSSAPIAuthentication yes',
  )
  file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => $str,
  }
}


