# Use Python Image
FROM python:alpine3.14

# Set working dir to /app
WORKDIR /app

# Run update and install Pip
RUN apk update

# Copy folders in /app to /app
COPY /app /app

# Pip-install BeautifulSoup and requests
RUN pip install -r requirements.txt

# Run app
CMD ["python", "-u", "/app/cryptoTracker.py"]