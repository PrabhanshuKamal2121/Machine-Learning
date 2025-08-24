FROM python:3.13
#workdir
WORKDIR /app

#copy requirements and install dependencies (here their will be no cache and it will reduce imgae size)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the file
COPY . .

#Expose
EXPOSE 8000

#command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]