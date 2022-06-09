FROM python:3.8

WORKDIR /
RUN apt-get update
RUN apt-get install libsndfile1 -y
ENV LANGUAGE en_US.UTF-8
COPY app/classification.py .

COPY requirements.txt .
COPY app/app.py .
RUN pip3 install --upgrade pip


# Below method does not work and still gives no module named numpy error even though numpy is present in requirements.txt

RUN pip install --no-cache-dir -U -r requirements.txt

EXPOSE 8000:8000

ENTRYPOINT ["python" , "app.py"]

