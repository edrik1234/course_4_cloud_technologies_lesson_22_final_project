FROM python:3.11
WORKDIR /app
COPY config.json /app/config.json
COPY lesson_47_final_project.py /app/lesson_47_final_project.py
COPY print_colors.py /app/print_colors.py
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install -r requirements.txt
ENV HOST_IP=127.0.0.1
EXPOSE 80
CMD [ "python", "lesson_47_final_project.py"]
