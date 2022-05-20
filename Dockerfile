FROM python:latest
COPY main.py .
RUN pip3 install aiogram --upgrade
ENTRYPOINT [ "python3" ]
CMD ["main.py"]