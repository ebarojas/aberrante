#!/usr/bin/env bash

echo "=> Start config box..."
sudo apt-get update --allow-releaseinfo-change
sudo apt-get install -y git
# TODO Check ntpdate on stretch
# sudo apt-get install -y ntpdate
sudo apt-get install -y python3-pip
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U pyOpenSSL



# Install PostgreSQL
# TODO find the correct command for postgres db already installed
echo "Installing postgresql"
sudo apt-get install -y libpq-dev postgresql postgresql-contrib libxml2-dev \
libxslt1-dev zlib1g-dev build-essential libssl-dev libffi-dev
# For weasyprint
sudo apt-get install -y python3-dev python3-setuptools python3-wheel python3-cffi \
libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info

sudo sudo apt-get install -y ntp ntpdate
# Create database
sudo -i -u postgres psql -c "CREATE DATABASE mydb"

# Create user
echo "Creating user and granting privileges"
sudo -i -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant';"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mydb TO vagrant;"
sudo -i -u postgres psql -c "ALTER USER vagrant CREATEDB;"


echo "=> Installing requirements..."
sudo python3 -m pip install --break-system-packages -r /vagrant/requirements.txt

echo "=> Check flake8 for python lint..."
sudo python3 -m pip install -U flake8

# This logic is to check if vagrantbox has UTC time or not
if [ `sudo rm /etc/localtime` ]; then
    sudo ln -s /usr/share/zoneinfo/Etc/GMT/etc/localtime
    echo "Update vagrantbox to UTC time"
else
    echo "Vagrantbox is ready"
fi

echo "=> Synchronizing date and time"
sudo service ntp stop
sudo ntpdate -u pool.ntp.org

echo "=> End config box..."
