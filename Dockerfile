FROM python:3.9-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install --no-install-recommends -y libglib2.0-0 libsm6 libxrender1 libxext6 ghostscript python3-tk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/

# 
CMD ["fastapi", "run", "main.py", "--port", "80"]
