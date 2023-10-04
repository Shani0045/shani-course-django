FROM python:3.10.13-alpine3.18
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . /opt/app
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x runtime.sh
EXPOSE 8000
