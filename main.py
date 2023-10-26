import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(
    directory="templates"
)  # Directory where your HTML templates are stored


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/f1/current/last/results")
async def get_last_f1_results(request: Request):
    ergast_api_url = "http://ergast.com/api/f1/current/last/results.json"

    try:
        response = requests.get(ergast_api_url)
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

    except requests.exceptions.RequestException as e:
        return templates.TemplateResponse(
            "error.html", {"request": request, "error_message": f"Request error: {e}"}
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
