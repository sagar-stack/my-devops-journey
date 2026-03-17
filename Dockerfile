# 1. Use an official Python image as the base (The foundation)
FROM python:3.9-slim

# 2. Create a folder inside the container to hold our code (The workspace)
WORKDIR /app

# 3. Copy our shopping list and install the tools we need (The ingredients)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copy our actual python script to the container (The recipe)
COPY day18.py .

# 5. Tell the container what to do when it starts (The cooking instructions)
CMD ["python","-u","day18.py"]
