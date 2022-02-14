FROM python:3.11.0a4-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 80
ENV NOM coca
CMD ["python", "app.py"]