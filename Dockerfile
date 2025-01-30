FROM python:3.12-slim
LABEL authors="Eraj"
RUN  apt update && apt install ffmpeg -y
WORKDIR /app
COPY requirements.txt .
RUN pip3 install  --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]