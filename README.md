# NC Heat Helper

NC Heat Helper is a Streamlit app I made to show how temperature and humidity affect how hot it feels. I noticed North Carolina was hot and humid this summer, and it felt like the heat lasted into Fall. I wanted to make a program that has a real use and gives students, friends, and family some helpful tips for hot weather.

## Features

- Adjust temperature and humidity and see a heat index estimate and general category.
- Explore a humidity graph and compare two humidity levels at the same temperature.
- Get heat-safety reminders that change with the category.
- Read about North Carolina's long-term climate projection and take a three-question quiz.

The app uses numbers you choose; it does not check current weather. The heat index uses the National Weather Service simple formula and Rothfusz regression, including the documented humidity adjustments. This calculator is for learning and cannot guarantee that an activity is safe or replace official warnings or medical advice. The heat index assumes shade and light wind, and it does not include everything that matters for sports or hard physical activity.

## Run locally on macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit normally opens the app in your browser at a localhost address (usually `http://localhost:8501`).

### Windows activation

In PowerShell, create the environment and activate it with:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run the calculation tests

```bash
python -m unittest -v test_heat_index.py
```

## Sources

- [NWS heat index equation](https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml)
- [NWS heat safety](https://www.weather.gov/ctp/heat)
- [CDC heat and health](https://www.cdc.gov/heat-health/about/index.html)
- [NC Climate Science Report: Plain Language Summary (2020)](https://files.nc.gov/ncdeq/climate-change/climate-scinece-report/NC-Climate-Science-Report_Plain_Language_Summary.pdf)
- [NC State Climate Office](https://climate.ncsu.edu/)

The report says North Carolina's statewide average temperature could rise 6–10°F by the end of the century under its higher-emissions scenario. This is a long-term projection, not a forecast for one day. The heat index shows how temperature and humidity affect how hot it feels; it does not prove climate change by itself.

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository named `nc-heat-helper` and upload the files in this folder.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io) with your GitHub account and connect GitHub if prompted.
3. Choose **Create app**, select the `nc-heat-helper` repository and `main` branch, and set the main file path to `app.py`.
4. Deploy. Once it finishes, use the `.streamlit.app` link shown by Streamlit.
5. Open that URL in a private/incognito browser window to check what a visitor can access.

The app has no API keys or account system. A public GitHub repository and a public Streamlit app let an instructor open it without signing in. The code is in GitHub and the app is deployed on Streamlit, but check the app's access setting before sharing so anyone with the link can open it.

## Files

- `app.py` — Streamlit interface, graph, tips, climate information, and quiz.
- `heat_index.py` — NWS heat-index and category functions.
- `test_heat_index.py` — automated tests for calculations and category boundaries.
- `CREATORS_NOTE.md` — creator's note in the four requested sections.
