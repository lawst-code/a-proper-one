FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y && apt-get install git -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install git+https://github.com/lawst-code/Noxus.git
RUN pip install -e .
RUN pip install pytest

# Copy the plugin files
COPY . /app/a_proper_one/

# Set working directory to plugin
WORKDIR /app/a_proper_one

# Expose the default port
EXPOSE 8000

# Command to serve the specific plugin
CMD ["noxus", "serve", "--host", "0.0.0.0", "--port", "8000", "--plugin", "a_proper_one.yaml"]
