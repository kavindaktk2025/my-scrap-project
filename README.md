
# 🕷️ My Scrap Project

A Scrapy-based web scraping project designed to extract data from listing websites. This project includes Docker support to make deployment and execution easier across environments.

---

## 📁 Project Structure

```

my-scrap-project/
├── Dockerfile
├── docker-compose.yml
├── scrapy.cfg
├── requirements.txt
├── README.md
└── my\_scrap\_project/
├── **init**.py
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
└── spiders/
├── **init**.py
└── ikmanlistings.py

````

---

## 🚀 Quick Start (Dockerized)

### ✅ Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

---

### 🔨 Clone the Repository

```bash
git clone https://github.com/kavindaktk2025/my-scrap-project.git
cd my-scrap-project
````

---

### 🐳 Run Using Docker (One-Time Crawl)

1. **Build Docker Image:**

```bash
docker build -t my-scrap-project . -t scarper-c
```

2. **Run the Spider:**

```bash
docker run -it -v $(pwd)/output:/app/output  scraper-c
```

This will run the `ikmanlistings` spider and output the scraped data to your console. and will write the output to the local output folder output.json file

---

## 📄 Output

Scraped data can be exported to formats like JSON or CSV using Scrapy's built-in options:

```bash
scrapy crawl ikmanlistings -o output.json
```

> When using Docker, prepend this command with `docker run` or use `docker-compose exec` as shown above.

---

## ⚙️ Configuration Files

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["scrapy"]
```

---

### requirements.txt

```
scrapy>=2.13.2
beautifulsoup4>=4.13.4

```

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Kavinda T.K.**
GitHub: [@kavindaktk2025](https://github.com/kavindaktk2025)

---

## 📬 Contributions

Feel free to fork the project and submit PRs if you have improvements, bug fixes, or feature ideas!

```

---

Let me know if you'd like the README to include screenshots, output samples, or GitHub badges as well.
```
