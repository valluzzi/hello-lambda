FROM python:3.10-bullseye

# Predisposizione per Lambda AWS
RUN pip install -U awslambdaric
COPY lambda/app.py .

# overrided on lambda call
ENTRYPOINT ["python3", "-m", "awslambdaric" ]
CMD [ "app.handler" ]