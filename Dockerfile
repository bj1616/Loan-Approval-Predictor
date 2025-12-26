#From
FROM python:3.9-slim

#workdir
WORKDIR /app

#copy
COPY requirements.txt .

# Install dependencies (ONCE, no cache)
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy only application code
COPY . .

#expose
EXPOSE 8501

#cmd
CMD ["streamlit","run","frontend.py","--server.address","0.0.0.0","--server.port","8501"]