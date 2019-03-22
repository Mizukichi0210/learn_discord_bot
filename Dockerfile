FROM python:3.6-alpine

RUN mkdir -p /application/src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# Install discord.py
RUN python3 -m pip install -U discord.py