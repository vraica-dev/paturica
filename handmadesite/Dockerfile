# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/handmadesite

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/handmadesite/entrypoint.sh
RUN chmod +x /usr/src/handmadesite/entrypoint.sh


# copy project
COPY . .

ENTRYPOINT ["/usr/src/handmadesite/entrypoint.sh"]