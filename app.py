"""NC Heat Helper: a small educational Streamlit app about heat and humidity."""

import streamlit as st

from heat_index import calculate_heat_index, risk_category


st.set_page_config(page_title="NC Heat Helper", page_icon="☀️", layout="wide")
st.markdown(
    """
    <style>
    .stApp { background: #f5f8f8; color: #152b3c; }
    h1, h2, h3 { color: #123047 !important; }
    .stApp p, .stApp li, .stApp label,
    .stApp [data-testid="stWidgetLabel"],
    .stApp [data-testid="stWidgetLabel"] p,
    .stApp [role="radiogroup"] label,
    .stApp [role="radiogroup"] label p,
    .stApp [data-testid="stMetricLabel"],
    .stApp [data-testid="stMetricLabel"] *,
    .stApp [data-testid="stMetricValue"],
    .stApp [data-testid="stMetricValue"] *,
    .stApp [data-baseweb="tab"] {
        color: #152b3c !important;
    }
    .intro { border-left: 5px solid #188b83; padding: .8rem 1rem;
             background: #e8f3f1; border-radius: 6px; }
    .fact { background: #fff0df; border-left: 5px solid #ee8b36;
            padding: 1rem; border-radius: 6px; }
    a { color: #087d77 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("☀️ NC Heat Helper")
st.subheader("How hot does it actually feel outside?")
st.markdown(
    '<div class="intro">This summer I noticed how hot and humid it was getting in '
    "North Carolina, and it even felt like the heat continued into Fall. So I wanted "
    "to make a program that shows how humidity can change how hot it feels outside "
    "and give people a few useful tips to stay safe.</div>",
    unsafe_allow_html=True,
)

calculator_tab, why_tab, quiz_tab = st.tabs(
    ["Heat Calculator", "Why It Matters", "Quick Quiz"]
)

with calculator_tab:
    st.header("Try the heat index calculator")
    st.write(
        "Move the sliders to see how air temperature and humidity work together. "
        "These are values you choose; this app does not retrieve current weather."
    )
    left, right = st.columns(2)
    with left:
        temperature = st.slider("Air temperature (°F)", 70, 110, 90)
    with right:
        humidity = st.slider("Relative humidity (%)", 10, 100, 60)

    heat_index = calculate_heat_index(temperature, humidity)
    category = risk_category(heat_index)
    metric_a, metric_b, metric_c = st.columns(3)
    metric_a.metric("Air temperature", f"{temperature}°F")
    metric_b.metric("Relative humidity", f"{humidity}%")
    metric_c.metric("Calculated heat index", f"{heat_index:.1f}°F", category)
    st.markdown(
        f"### At {temperature}°F with {humidity}% humidity, it feels like about "
        f"**{heat_index:.0f}°F**."
    )
    if heat_index >= 125:
        st.warning(
            "This is a very high heat-index value. At extreme temperature and humidity "
            "combinations, the regression may be unreliable beyond the conditions in "
            "the data used to build it. Follow official local warnings and do not use "
            "this number by itself to make a safety decision."
        )

    st.markdown("#### What this number means")
    st.write(
        "Heat index combines air temperature and relative humidity to estimate the "
        "apparent temperature in shady conditions with light wind. Direct sunlight, "
        "physical activity, clothing, health, and other factors can increase heat risk. "
        "This educational calculator cannot tell you that an outdoor activity is safe."
    )

    st.markdown("#### How humidity changes the heat index")
    humidity_values = list(range(10, 101, 5))
    graph_values = [calculate_heat_index(temperature, value) for value in humidity_values]
    chart_rows = {"Heat Index (°F)": graph_values}
    chart_index = humidity_values
    # Streamlit labels the index as relative humidity for a readable built-in chart.
    import pandas as pd
    chart = pd.DataFrame(chart_rows, index=chart_index)
    chart.index.name = "Relative Humidity (%)"
    st.line_chart(chart)
    st.caption(f"Selected point: {humidity}% humidity → {heat_index:.1f}°F heat index.")
    st.caption(
        "Even when the temperature stays the same, having more humidity in the air "
        "can make it feel hotter. This is why really humid summer days in North "
        "Carolina can become uncomfortable or dangerous."
    )
    compare_low = calculate_heat_index(temperature, 30)
    compare_high = calculate_heat_index(temperature, 80)
    st.info(
        f"At {temperature}°F, the estimated heat index is {compare_low:.0f}°F at "
        f"30% humidity and {compare_high:.0f}°F at 80% humidity."
    )

    st.markdown("#### A few ways to lower your risk")
    recommendations = {
        "Below caution": ["Keep water nearby and check the local forecast before heading out."],
        "Caution": ["Drink water regularly.", "Take breaks and look for shade during longer outdoor activities."],
        "Extreme Caution": ["Plan walks or sports for cooler hours if possible.", "Take frequent breaks in shade or an air-conditioned place.", "Check in with friends and family."],
        "Danger": ["Reduce strenuous outdoor activity and take frequent cooling breaks.", "Use an air-conditioned location when you can.", "Pay attention to how you and people around you feel."],
        "Extreme Danger": ["Avoid strenuous outdoor activity where possible.", "Spend time in a cool or air-conditioned place.", "Check on others and follow local weather alerts."],
    }
    for tip in recommendations[category]:
        st.markdown(f"- {tip}")
    st.markdown(
        "Not everyone has reliable or affordable air conditioning. Community cooling "
        "spaces and checking on neighbors can matter during hot weather. Find local "
        "resources through your county or health department."
    )
    st.markdown(
        "Sources: [National Weather Service heat index equation]"
        "(https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml) · "
        "[NWS heat safety](https://www.weather.gov/ctp/heat) · "
        "[CDC heat and health](https://www.cdc.gov/heat-health/about/index.html)"
    )

with why_tab:
    st.header("Why This Matters in North Carolina")
    st.write(
        "I started thinking about this because the heat and humidity seemed to last "
        "later into the year. Hot days can make time outdoors harder, and warmer "
        "nights can give people less relief after a hot day. Humidity can make it "
        "harder for the body to cool itself, while access to air conditioning is not "
        "the same for everyone."
    )
    st.markdown(
        '<div class="fact"><strong>If emissions keep rising quickly, North Carolina '
        'could warm another 6 to 10°F by 2100.</strong><br><br>This is a projection '
        'for statewide average temperature under a higher-emissions scenario in the '
        '2020 North Carolina Climate Science Report. It is a long-term projection, '
        'not a forecast for one day.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "Source: [North Carolina Climate Science Report: Plain Language Summary "
        "(2020)](https://files.nc.gov/ncdeq/climate-change/climate-scinece-report/"
        "NC-Climate-Science-Report_Plain_Language_Summary.pdf) · "
        "[NC State Climate Office](https://climate.ncsu.edu/)"
    )
    st.info(
        "The calculator shows how temperature and humidity affect apparent "
        "temperature. The climate report is evidence about long-term climate change. "
        "The calculator itself does not prove climate change."
    )
    st.subheader("What Can We Do?")
    st.markdown(
        "- Talk with friends and family about climate change and share heat-safety information.\n"
        "- Check on people during hot weather and support access to community cooling resources.\n"
        "- Learn about practical ways to reduce greenhouse gas emissions, including choices we can make together.\n"
        "- Share NC Heat Helper with someone who spends time outside."
    )

with quiz_tab:
    st.header("Quick Quiz")
    st.write("See what stuck from the calculator and climate information.")
    questions = [
        ("How can humidity affect how hot it feels?", ["It always cools the air down.", "It can make it feel hotter by slowing sweat evaporation.", "It has no effect."], 1,
         "Humidity can slow the evaporation of sweat, one way the body cools itself."),
        ("Why take breaks or reduce strenuous activity in extreme heat?", ["Breaks make the weather cooler.", "Exercise is always unsafe outdoors.", "Rest breaks help lower heat strain and give you a chance to cool down."], 2,
         "Physical activity adds heat stress, so breaks and cooler locations can help reduce exposure."),
        ("Why can unreliable air conditioning increase heat risk?", ["It changes the outdoor humidity.", "It can limit access to a cooler place during hot weather.", "It makes every hot day dangerous."], 1,
         "People without reliable cooling may have fewer ways to escape indoor heat."),
    ]
    chosen = []
    for number, (prompt, options, _answer, _explanation) in enumerate(questions, start=1):
        chosen.append(st.radio(prompt, options, index=None, key=f"quiz_{number}"))
    if st.button("Check My Answers"):
        if any(answer is None for answer in chosen):
            st.warning("Please choose an answer for all three questions first.")
        else:
            score = sum(
                answer == questions[index][1][questions[index][2]]
                for index, answer in enumerate(chosen)
            )
            st.subheader(f"You got {score} out of {len(questions)} correct.")
            for index, (prompt, options, correct_index, explanation) in enumerate(questions):
                correct = chosen[index] == options[correct_index]
                st.markdown(
                    f"**{index + 1}. {'Correct' if correct else 'Not quite'}** — {explanation}"
                )

st.divider()
st.caption(
    "This app is for educational purposes and does not replace official weather "
    "warnings or medical advice. The general heat index does not account for every "
    "factor that matters during sports and physical activity; use official guidance "
    "and more complete heat-stress measurements when appropriate."
)
