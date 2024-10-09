from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import router

app = FastAPI()

# for local postgres initializations.
# models.Base.metadata.create_all(bind=engine)

all_allowed = ["*"]


# @app.middleware('http')
# async def authorize(request: Request, call_next):
#     response = verify_token(request)
#     if not response == '':
#         print(response)
#         return JSONResponse(content={'detail': response}, status_code=401)
#     return await call_next(request)


app.add_middleware(
    CORSMiddleware,
    allow_origins=all_allowed,
    allow_credentials=True,
    allow_methods=all_allowed,
    allow_headers=all_allowed,
)

app.include_router(router)
