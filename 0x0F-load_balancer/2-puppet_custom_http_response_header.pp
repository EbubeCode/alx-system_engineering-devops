# install and configure nginx
node default {
  $str = sprintf("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n",
    'server {',
    'listen 80 default_server;',
    'listen [::]:80 default_server;',
    'add_header X-Served-By host_name;',
    'root /var/www/html;',
    'index index.html index.htm index.nginx-debian.html;',
    'server_name _;',
    'location / {',
    'try_files $uri $uri/ =404;}',
    '}')

  package {'nginx':
    ensure => present,
    name   => 'nginx',
  }
  file {'/etc/nginx/sites-available/default':
    ensure  => present,
    content => $str,
    require => Package['nginx'],
    before  => Exec['restart'],
  }
  file {'/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
    require => Package['nginx'],
    before  => Exec['restart'],
    }
  exec {'restart':
  command => '/bin/sed -i s/host_name/$HOSTNAME/ /etc/nginx/sites-available/default; /usr/sbin/service nginx restart'
  }

}
