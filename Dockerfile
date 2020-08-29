FROM python:3

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install requests schedule python-dotenv

# Copy app 
COPY app.py ./

# Run the app
CMD [ "python", "-u", "./app.py" ]