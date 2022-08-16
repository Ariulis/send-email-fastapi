from fastapi import Request, Depends
from fastapi.responses import HTMLResponse

from .. import get_setttings, logger, templates
from ..schemas import UserSchema
from ..email import send_email
from . import main
from .forms import UserForm

vars = get_setttings()


@main.get('/', response_class=HTMLResponse)
@logger.catch
def read_index(request: Request):
    form = UserForm()
    return templates.TemplateResponse(
        'index.html', {
            'request': request,
            'form': form
        }
    )


@main.post('/')
@logger.catch
async def login(data: UserSchema):
    await send_email(data)
    return 'The message has been successfully sent!'
