# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)


@weather_routes.route("/api/weather/forecast.json")
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)

    country_code = url_params.get("country_code") or "US"
    zip_code = url_params.get("zip_code") or "20057"

    results = get_hourly_forecasts(
        country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "Invalid Geography. Please try again."}), 404
