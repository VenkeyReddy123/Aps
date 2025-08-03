from fastapi import FastAPI, Body, Request, HTTPException, UploadFile, File, Form
app = FastAPI()

@app.get('/')
async def getallSourcesForApplication(c_id):
    try:
        result = "access is suucess fully"
        return result
    except:
        return JSONResponse(content={'error'}, status_code=500)
