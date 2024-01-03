import uvicorn
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI

from InstagramTools.routers import friends

app = FastAPI(title='Example API', version='1.0.0')

app.add_middleware(CorrelationIdMiddleware, header_name='X-Request-ID')
app.include_router(friends, prefix='/friends', tags=['friends'])


if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000, log_config=None)
