#!/bin/bash
set -e

sudo apt update
sudo apt install -y nginx

sudo cp /home/ubuntu/PiskeGram-Project/nginx.conf /etc/nginx/conf.d/piskegram.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
