import json

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from zerodepth_solver import zerodepth_solve

app = FastAPI()


@app.post("/")
def zero_depth(args: list):
    min_depth, max_depth = zerodepth_solve(args)

    return_val = json.dumps([min_depth, max_depth])
    headers = {
        "Cache-Control": "no-cache, must-revalidate",
        "Content-Type": "application/json",
    }
    return StreamingResponse(content=iter(return_val), headers=headers)
