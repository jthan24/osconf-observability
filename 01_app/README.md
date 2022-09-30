#01_app
How to run this app

```bash
docker build -t mynodeapp:0.0.1 . 
docker images 
docker run --name test-front --rm -d -p 8081:8080 mynodeapp:0.0.1
```

#Test the app
```bash
curl http://localhost:8081
```

