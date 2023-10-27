import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(
    directory="templates"
)  # Directory where your HTML templates are stored


@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):  # Add 'request' as a parameter
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/current_results", response_class=HTMLResponse)
async def current_results(request: Request):
    ergast_api_url = "http://ergast.com/api/f1/current/last/results.json"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(ergast_api_url)
            response.raise_for_status()  # Check for HTTP errors

            if response.status_code == 200:
                data = response.json()
            else:
                return templates.TemplateResponse(
                    "error.html",
                    {
                        "request": request,
                        "error_message": "Failed to fetch data from Ergast F1 API",
                    },
                )

        except httpx.RequestError as e:
            return templates.TemplateResponse(
                "error.html",
                {"request": request, "error_message": f"Request error: {e}"},
            )

        except ValueError as e:
            return templates.TemplateResponse(
                "error.html",
                {"request": request, "error_message": f"JSON decoding error: {e}"},
            )

        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "race_info": data["MRData"]["RaceTable"]["Races"][
                    -1
                ],  # Include race information
                "race_results": data["MRData"]["RaceTable"]["Races"][-1][
                    "Results"
                ],  # Include race results
            },
        )


@app.get("/current_schedule", response_class=HTMLResponse)
async def current_schedule(request: Request):
    ergast_api_url = "https://ergast.com/api/f1/current.json"

    async with httpx.AsyncClient() as client:
        response = await client.get(ergast_api_url)

        if response.status_code == 200:
            data = response.json()
            schedule_data = data["MRData"]["RaceTable"]["Races"]
            return templates.TemplateResponse(
                "current_schedule.html",
                {"request": request, "schedule_data": schedule_data},
            )

        return HTMLResponse(
            content="<html><body>Error fetching data from Ergast API</body></html>"
        )
