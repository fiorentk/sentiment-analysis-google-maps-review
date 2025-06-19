FROM python:3.10-slim

# Set working directory
WORKDIR /code


# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin file aplikasi ke dalam container
COPY ./app /code/.

# Jalankan aplikasi dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8007"]
