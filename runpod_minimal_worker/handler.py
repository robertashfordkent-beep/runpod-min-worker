import runpod
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/ping")
def ping():
    return JSONResponse({"ok": True})


def handler(job):
    data = job.get("input", {}) if isinstance(job, dict) else {}
    return {
        "ok": True,
        "echo": data,
    }


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
