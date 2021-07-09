FROM python
RUN apt-get update -y
COPY . .
CMD python /app/app.py