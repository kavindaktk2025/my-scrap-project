# My Scrap Project

A web scraping project utilizing Scrapy to extract data from online listings.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## 📦 Project Structure

The project directory contains:

- `Dockerfile`: Docker configuration for the project.
- `docker-compose.yml`: Docker Compose configuration for multi-container setup.
- `scrapy.cfg`: Scrapy project configuration file.
- `requirements.txt`: Python dependencies.
- `my_scrap_project/`: Scrapy project directory containing spiders and settings.

## 🐳 Running with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/kavindaktk2025/my-scrap-project.git
cd my-scrap-project
2. Build the Docker Image
bash
Copy
Edit
docker build -t my-scrap-project .
3. Run the Scrapy Spider
bash
Copy
Edit
docker run --rm my-scrap-project scrapy crawl ikmanlistings
This command runs the ikmanlistings spider and outputs the scraped data to the console.

🧪 Running with Docker Compose
Alternatively, you can use Docker Compose for easier management:

1. Build and Start the Services
bash
Copy
Edit
docker-compose up --build
2. Run the Spider
In a separate terminal, execute:

bash
Copy
Edit
docker-compose exec scrapy scrapy crawl ikmanlistings
This will run the spider within the Docker Compose environment.

🧹 Cleaning Up
To stop and remove the containers:

bash
Copy
Edit
docker-compose down
📄 Output
The scraped data will be stored in the output/ directory in JSON format.

📝 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### 🐳 Dockerfile

Ensure your `Dockerfile` is set up as follows:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["scrapy"]
🧪 requirements.txt
Your requirements.txt should include:

nginx
Copy
Edit
scrapy
📦 docker-compose.yml
For Docker Compose, use the following configuration:

yaml
Copy
Edit
version: '3.8'

services:
  scrapy:
    build: .
    volumes:
      - .:/app
    command: ["scrapy", "crawl", "ikmanlistings"]
