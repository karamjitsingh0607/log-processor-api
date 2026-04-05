from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from processor.service import process_logs
import uuid, os, json
from config import RESULT_DIR

app = FastAPI()
results = {}

os.makedirs(RESULT_DIR,exist_ok=True)

def run_processing(job_id, lines):
    from config import BATCH_SIZE, NUM_WORKER
    result = process_logs(lines, BATCH_SIZE, NUM_WORKER)
    file_path = f"{RESULT_DIR}/{job_id}.json"
    with open(file_path, "w") as f:
        json.dump(result, f, indent= 4)
    results[job_id] = {
        "status": "completed",
        "INFO": len(result["INFO"]),
        "WARNING": len(result["WARNING"]),
        "ERROR": len(result["ERROR"])
    }
@app.post("/process-log")
async def process_log(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    lines = [line.decode("utf-8") for line in file.file]
    job_id = str(uuid.uuid4())
    results[job_id] = {"status": "processing"}
    background_tasks.add_task(run_processing, job_id, lines)
    return {
        "message": "Processing started",
        "job_id": job_id,
        "status_url": f"/status/{job_id}",
        "download_url": f"/download/{job_id}"
    }

@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id in results:
        return results[job_id]
    return {"status": "processing"}

@app.get("/download/{job_id}")
def download_file(job_id: str):
    file_path = f"{RESULT_DIR}/{job_id}.json"

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not ready")

    return FileResponse(
        path=file_path,
        media_type="application/json",
        filename=f"{job_id}.json"
    )