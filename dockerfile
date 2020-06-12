FROM python:3.8.3

RUN mkdir /bg-discord-bot
WORKDIR /bg-discord-bot

COPY . .
RUN python3 -m pip install -r requirements.txt

CMD ["python","main.py"]