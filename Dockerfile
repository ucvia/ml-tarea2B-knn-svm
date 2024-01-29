FROM python:3.10-buster
EXPOSE 8502

RUN apt-get update
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y ffmpeg

WORKDIR /usr/app
COPY . .
######## AGREGAR TUS LIBRERIAS EN REQUIREMENTS-HW ########
RUN pip install -r requirements-hw.txt
######## AGREGAR TUS LIBRERIAS EN REQUIREMENTS-HW ########
RUN pip install streamlit
RUN pip install pillow
RUN pip install numpy
RUN pip install scipy
RUN pip install pandas
RUN pip install st-pages
RUN pip install tensorflow
RUN pip install keras
RUN pip install streamlit-drawable-canvas
RUN pip install opencv-python

CMD ["streamlit", "run", "src/app.py", "--server.port", "8502"]