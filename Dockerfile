FROM python:3.9.7

# Define Working directory
WORKDIR /usr/src/app
COPY requirements.txt ./

# Define command to install requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the command 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
