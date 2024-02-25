FROM python:3.9  

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt 
RUN pip install keras --upgrade
ENV KERAS_BACKEND jax

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "server.py"] 