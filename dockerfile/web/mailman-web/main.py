import os
import socket
import ipaddress

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# NOTE: this is the MTA host, we need to update it.
EMAIL_HOST = 'mailman-exim4-0.mail-suit-service.default.svc.cluster.local'
EMAIL_PORT = 25

mailman_ip_address = socket.gethostbyname(
    os.environ.get('MAILMAN_HOST_IP')).split('.')
mailman_ip_cidr = "{0}.{1}.0.0/16".format(mailman_ip_address[0],
                                          mailman_ip_address[1])
MAILMAN_ARCHIVER_FROM = [str(ip) for ip in
                         ipaddress.IPv4Network(mailman_ip_cidr)]

ALLOWED_HOSTS = [
    "localhost",  # Archiving API from Mailman, keep it.
    # Add here all production URLs you may have.
    "mailman-database-0.mail-suit-service.default.svc.cluster.local",
    "mailman-core-0.mail-suit-service.default.svc.cluster.local",
    "mailman-web-0.mail-suit-service.default.svc.cluster.local",
    "mail-web-service.default.svc.cluster.local",
    # NOTE: This is the public ip address of the served host
    "159.138.26.163",
    "tommylike.me",
    os.environ.get('SERVE_FROM_DOMAIN'),
    os.environ.get('DJANGO_ALLOWED_HOSTS'),
]