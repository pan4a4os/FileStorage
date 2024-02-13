import uvicorn
from fastapi import FastAPI
from source.api.routers import all_routers

app = FastAPI(title="File Storage API")

for router in all_routers:
    app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
