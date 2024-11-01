FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY ./reqs.txt reqs.txt

RUN pip install --no-cache-dir -r reqs.txt

COPY ./static static

COPY ./templates templates

COPY ./main.py main.py

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]