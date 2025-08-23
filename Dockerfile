FROM python:3-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy app 
COPY app.py ./

# Run the app
CMD [ "python", "-u", "./app.py" ]