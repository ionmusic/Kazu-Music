FROM nikolaik/python-nodejs:python3.10-nodejs18
RUN apt-get install youtube-dl
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN pip3 install --upgrade youtube_dl
RUN pip3 youtube-dl --rm-cache-dir
CMD bash start
