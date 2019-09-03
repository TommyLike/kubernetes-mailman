#! /bin/bash
set -e
#Update exim4 service first
sudo update-exim4.conf

exec $@
