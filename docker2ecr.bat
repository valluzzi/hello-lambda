set image=hello-lambda
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 901702069075.dkr.ecr.us-east-1.amazonaws.com
docker build --no-cache -t %image% .
docker tag %image%:latest 901702069075.dkr.ecr.us-east-1.amazonaws.com/%image%:latest
docker push 901702069075.dkr.ecr.us-east-1.amazonaws.com/%image%:latest
pause