#02_app

How to run this app


docker build -t mypythonapp:0.0.1 .
docker images
docker run --name testpython1 --rm -d -p 8083:5000 -e PASSWORD="elsecretomejorguardado" mypythonapp:0.0.1

#Test the app

curl http://localhost:8083
