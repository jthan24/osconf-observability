FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY hello.py .
ENV FLASK_APP=hello
ENV FLASK_ENV=development
EXPOSE 5000
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:5000/ || exit 1 .
CMD [ "flask", "run", "--host=0.0.0.0" ]


