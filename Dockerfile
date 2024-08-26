# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8500

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8500", "--server.address=0.0.0.0"]
