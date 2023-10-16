from datetime import date, datetime, timedelta

from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.hotel.router import get_available_hotels
from app.utils import get_month_days

router = APIRouter(prefix="", tags=["Фронтенд"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    date_now = datetime.now().date()
    return templates.TemplateResponse(
        "auth/login.html",
        {
            "request": request,
            "from": date_now.strftime("%Y-%m-%d"),
            "to": (date_now + timedelta(days=1)).strftime("%Y-%m-%d")
        }
    )


@router.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    date_now = datetime.now().date()
    return templates.TemplateResponse(
        "auth/register.html",
        {
            "request": request,
            "from": date_now.strftime("%Y-%m-%d"),
            "to": (date_now + timedelta(days=1)).strftime("%Y-%m-%d")
        }
    )


@router.get("/", response_class=HTMLResponse)
async def redirect_to_hotels_page():
    date_now = datetime.now().date()
    date_to = date_now + timedelta(days=365)
    return RedirectResponse(f'hotels?date_from={date_now}&date_to={date_to}')


@router.get("/hotels", response_class=HTMLResponse)
async def get_hotels_page(
        request: Request,
        location: str = Query(None, description="Например: алтай"),
        date_from: str = Query(None, description=f"Min: {datetime.now().date()}"),
        date_to: str = Query(None, description=f"Например: {(datetime.now() + timedelta(days=1)).date()}, max: 365 дней"),
):
    date_now = datetime.now().date()
    date_max = date_now + timedelta(days=365)
    try:
        if not (date_from and date_to):
            raise ValueError

        date_from = date.fromisoformat(date_from)
        date_to = date.fromisoformat(date_to)
        if (date_from < date_now
                or date_to <= date_from
                or date_max < date_to):
            raise ValueError
    except ValueError:
        return RedirectResponse(
            f'hotels?date_from={date_now}&date_to={date_now + timedelta(days=1)}{f"&location={location}" if location else ""}')

    hotels = await get_available_hotels(
        max_days=365,
        location=location,
        date_from=date_from,
        date_to=date_to
    )

    dates_from = get_month_days(date_now)
    dates_to = dates_from.copy()
    dates_from.pop(-1)
    dates_to.pop(0)

    return templates.TemplateResponse(
        "hotels/hotels.html",
        {
            "request": request,
            "location": location or "",
            "date_from": date_from.strftime("%Y-%m-%d"),
            "date_to": date_to.strftime("%Y-%m-%d"),
            "hotels": hotels,
            "dates_from": dates_from,
            "dates_to": dates_to,
            "from": date_now.strftime("%Y-%m-%d"),
            "to": (date_now + timedelta(days=1)).strftime("%Y-%m-%d")
        },
    )