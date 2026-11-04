# NC Heat Helper

NC Heat Helper is a small Streamlit app about how temperature and humidity affect the heat index. I made it after noticing how hot and humid North Carolina felt, including later into Fall. It is for college students, friends, family, and other people who spend time outside.

## Features

- Adjust temperature and humidity and see a heat index estimate and general category.
- Explore a humidity graph and compare two humidity levels at the same temperature.
- Get heat-safety reminders that change with the category.
- Read about North Carolina's long-term climate projection and take a three-question quiz.

The app uses values selected by the user; it does not retrieve current weather. The heat index follows the National Weather Service simple formula and Rothfusz regression procedure, including its documented humidity adjustments. The calculator is educational, is not a safety guarantee, and does not replace official warnings or medical advice. Heat index is a shaded, light-wind estimate and does not capture all factors relevant to sports or strenuous work.

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

The 6–10°F North Carolina figure is a projection of statewide average warming by the end of the century under the report's higher-emissions scenario. It is not a day-level forecast. The heat index demonstrates apparent temperature and does not itself prove climate change.

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository named `nc-heat-helper` and upload the files in this folder.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io) with your GitHub account and connect GitHub if prompted.
3. Choose **Create app**, select the `nc-heat-helper` repository and `main` branch, and set the main file path to `app.py`.
4. Deploy. Once it finishes, use the `.streamlit.app` link shown by Streamlit.
5. Open that URL in a private/incognito browser window to check what a visitor can access.

The app has no API keys or account system. A public GitHub repository and a public Streamlit app are needed for an instructor to open the app without signing in. Confirm the sharing/public settings in Streamlit before sharing the URL. No repository or app has been published from this workspace.

## Files

- `app.py` — Streamlit interface, graph, tips, climate information, and quiz.
- `heat_index.py` — NWS heat-index and category functions.
- `test_heat_index.py` — automated tests for calculations and category boundaries.
- `CREATORS_NOTE.md` — creator's note in the four requested sections.
