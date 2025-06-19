from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import traceback
from logs.log_config import logger

from modul.inference import sentiment_analysis
from modul.model import Request

app = FastAPI(title="Sentiment Analysis API",
    description="author: Fiorentika Devasha",
    version="0.0.1",
    terms_of_service=None,
    contact=None,
    license_info=None)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/sentiment-analysis")
async def create_item(req: Request):
    try:
        logger.info(req)
        data = sentiment_analysis(req)
        logger.info(data)
        return {"resp_msg": "Sentiment analysis was successful.",
                     "resp_data":  data
                     }
    except Exception as e:
        error_trace = traceback.format_exc()
        logger.error(str(error_trace))
        return JSONResponse(
            status_code= status.HTTP_401_UNAUTHORIZED,
            content={"resp_msg": str(e),
                     "resp_data":  None
                     },
        )
    
# if __name__ == '__main__':
#     uvicorn.run('main:app', host="0.0.0.0", port=int("8000"),reload=True)