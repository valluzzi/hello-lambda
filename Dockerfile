FROM python:3.11-slim


RUN pip install -U httpx
# Predisposizione per Lambda AWS
RUN pip install -U awslambdaric
COPY lambda/lambda_function.py .

# overrided on lambda call
ENTRYPOINT ["python", "-m", "awslambdaric" ]
CMD [ "lambda_function.lambda_handler" ]