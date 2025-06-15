# My Scrap Project

A web scraping project utilizing Scrapy to extract data from online listings. this is using url hardcoded in the spider

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

## 📦 Project Structure

The project directory contains:

- `Dockerfile`: Docker configuration for the project.
- `scrapy.cfg`: Scrapy project configuration file.
- `requirements.txt`: Python dependencies.
- `my_scrap_project/`: Scrapy project directory containing spiders and settings.

## 🐳 Running with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/kavindaktk2025/my-scrap-project.git
cd my-scrap-project

## Build the Docker Image
bash
Copy
Edit
docker build -t my-scrap-project .
