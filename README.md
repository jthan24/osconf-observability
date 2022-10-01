# osconf-observability

# How to start this 

Go to the 01_app and read README.md file </br>
After that, go to 02_app and read README.md file too

Please check the currents apps it's working in your machine in 8001 and 8003 ports

# Install o11y tools
```bash
git clone https://github.com/stefanprodan/dockprom.git
cd dockprom
ADMIN_USER=admin ADMIN_PASSWORD=admin ADMIN_PASSWORD_HASH=JDJhJDE0JE91S1FrN0Z0VEsyWmhrQVpON1VzdHVLSDkyWHdsN0xNbEZYdnNIZm1pb2d1blg4Y09mL0ZP docker-compose up
```

# Test your interface
Access to the Grafana  tool: http://<host-ip>:3000 in my case is http://192.168.56.113:3000
User and password was set with admin and admin default password

# Send information to the apps
```bash
for i in $(seq 1 1000); do curl http://localhost:8083; done 
for i in $(seq 1 1000); do curl http://localhost:8081; done
```

```bash
for i in $(seq 1 1000); do curl http://192.168.56.113:8081 > /dev/null ; sleep 0.1;  done 
for i in $(seq 1 1000); do curl http://192.168.56.113:8083 > /dev/null ; sleep 0.1;  done 
```
