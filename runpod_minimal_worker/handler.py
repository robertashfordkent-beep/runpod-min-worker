import runpod


def handler(job):
    data = job.get("input", {}) if isinstance(job, dict) else {}
    return {
        "ok": True,
        "echo": data,
    }


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
