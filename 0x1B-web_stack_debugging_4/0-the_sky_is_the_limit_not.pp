# Fixing the number of failed requests to 0
exec { 'repair nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 5;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
