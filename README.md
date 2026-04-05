# 🚀 Log Processing API (FastAPI + Multiprocessing)

## 📌 Overview
A scalable backend system built using FastAPI to process large log files efficiently using multiprocessing and batch-based processing.

This project demonstrates how to handle large-scale data processing while maintaining performance and memory efficiency.

---

## ⚙️ Features

- 📂 Upload large log files via API
- ⚡ Parallel processing using multiprocessing
- 🧠 Batch-based processing for memory efficiency
- 🔄 Background task execution (non-blocking API)
- 📊 Job status tracking
- 📥 Download processed results as JSON
- 🧩 Modular and clean architecture

---

## 🧠 Architecture

Client → FastAPI → Background Task → Processing Engine → File Storage → Download API


---

## 🔗 API Endpoints

### 1️⃣ Start Processing

**POST /process-log**

Upload a log file to start processing.

**Response:**
```json 
{
  "message": "Processing started",
  "job_id": "unique-id",
  "status_url": "/status/{job_id}",
  "download_url": "/download/{job_id}"
}

2️⃣ Check Status

GET /status/{job_id}
Example output:

{
  "status": "completed",
  "INFO": 1000,
  "WARNING": 200,
  "ERROR": 50
}

3️⃣ Download Result
GET /download/{job_id}
Downloads processed log result as JSON file.

```

---

🛠 Tech Stack
- Python
- FastAPI
- Multiprocessing
- JSON

---

📁 Project Structure

log-processor-api/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── processor/
│   ├── __init__.py
│   ├── worker.py
│   ├── chunker.py
│   ├── aggregator.py
│   └── service.py
│
└── results/

---

🚀 How to Run

1.  Clone Repository

- git clone https://github.com/YOUR_USERNAME/log-processor-api.git
- cd log-processor-api

2. Create Virtual Environment

- python -m venv venv
- source venv/bin/activate   # Mac/Linux
- venv\Scripts\activate      # Windows

3. Install Dependencies

- pip install -r requirements.txt

4. Run Server

- uvicorn main:app --reload

5. Open Swagger UI

- http://127.0.0.1:8000/docs

---

🧠 Key Learnings
- Handling large file processing efficiently
- Using multiprocessing for CPU-bound tasks
- Designing non-blocking APIs using background tasks
- Structuring scalable backend systems

---

🔮 Future Improvements
- Add Redis + Celery for distributed processing
- Store results in database
- Add authentication
- Improve monitoring and logging

---

👨‍💻 Author
Karamjit Singh