FROM python:3.9

# COPY . .

# RUN pip install --upgrade pip

# CMD ["python", "main.py"]
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app requests

# A distroless container image with Python and some basics like SSL certificates
ENV PYTHONPATH /app
CMD ["/app/main.py"]