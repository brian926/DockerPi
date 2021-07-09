# Use Python Image
FROM python

# Set working dir to /app
WORKDIR /app

# Run update and install Pip
RUN apt-get update && apt-get install -y \
    python-pip

# Copy folders in /app to /app
COPY /app /app

# Pip-install BeautifulSoup
RUN pip install beautifulsoup4

# Run app
CMD python /app/cryptoTracker.py