# Use Python Image
FROM python

# Set working dir to /app
WORKDIR /app

# Run update and install Pip
RUN apt-get update && apt-get install -y \
    python-pip

# Copy folders in /app to /app
COPY /app /app

# Pip-install BeautifulSoup and requests
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install mysql-connector

# Run app
CMD ["python", "-u", "/app/cryptoTracker.py"]