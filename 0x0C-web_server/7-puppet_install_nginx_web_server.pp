# install and configure nginx
node default {
  $str = sprintf("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\ns%\n%s\n%s\n",
    'server {',
    'listen 80 default_server;',
    'listen [::]:80 default_server;',
    'root /var/www/html;',
    'index index.html index.htm index.nginx-debian.html;',
    'server_name _;',
    'location / {',
    'try_files $uri $uri/ =404;}',
    'location /redirect_me {',
    'rewrite ^/redirect_me(.*)$ https://www.youtube.com permanent;}',
    '}')


  package {'nginx':
    ensure => present,
    name   => 'nginx',
  }
  file {'/etc/nginx/sites-available/default':
    ensure  => present,
    content => $str,
  }
  exec {'restart':
  command => '/usr/sbin/service nginx restart'
  }

}
