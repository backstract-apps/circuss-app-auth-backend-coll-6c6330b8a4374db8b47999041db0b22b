from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - circuss-app-auth-backend-coll-6c6330b8a4374db8b47999041db0b22b',debug=False,docs_url='/upbeat-cori-8dbcc416a02611ef885f0242ac12000493/docs',openapi_url='/upbeat-cori-8dbcc416a02611ef885f0242ac12000493/openapi.json')

app.include_router(router, prefix='/upbeat-cori-8dbcc416a02611ef885f0242ac12000493/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()