FROM python:3.9  

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt 
RUN pip install keras --upgrade
ENV KERAS_BACKEND jax
ENV PORT 80

COPY . /app

EXPOSE 80

CMD streamlit run app.py --server.port=${PORT} --browser.serverAddress="0.0.0.0"