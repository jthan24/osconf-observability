# osconf-observability


# Install o11y tools
```bash
git clone https://github.com/stefanprodan/dockprom.git
cd dockprom
ADMIN_USER=admin ADMIN_PASSWORD=admin ADMIN_PASSWORD_HASH=JDJhJDE0JE91S1FrN0Z0VEsyWmhrQVpON1VzdHVLSDkyWHdsN0xNbEZYdnNIZm1pb2d1blg4Y09mL0ZP docker-compose up
```

# Send information to the apps
```bash
for i in $(seq 1 1000); do curl http://localhost:8083; done 
for i in $(seq 1 1000); do curl http://localhost:8081; done
```
