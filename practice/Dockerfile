FROM python:3.12
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /impose
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","main.py"]

