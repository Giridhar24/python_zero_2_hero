# Topic of the Day: Intro to Docker (Dockerfile)
#
# Explanation: "It works on my machine!" is a famous developer excuse. Docker solves this by packaging your OS, libraries, and code into a Container.
#
# To use it, you write a blueprint called a Dockerfile.
#
# Code (Save as Dockerfile - No extension):

# 1. Base Image (The OS + Python)
# We start with a lightweight version of Linux that has Python 3.9 installed
FROM python:3.9-slim

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy our code from computer -> container
COPY . /app

# 4. Install libraries (if you had a requirements.txt)
# RUN pip install flask pandas

# 5. The command to run when the container starts
CMD ["python", "main.py"]


# To run this (Theory): docker build -t my-app . then docker run my-app.