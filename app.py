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
        "Change the sliders to see how temperature and humidity work together. "
        "These are numbers you enter yourself; the app does not show current weather."
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
        f"### So at {temperature}°F with {humidity}% humidity, it feels like around "
        f"**{heat_index:.0f}°F**."
    )
    if heat_index >= 125:
        st.warning(
            "That is a very high heat-index number. With extreme heat and humidity, "
            "this formula can go beyond the conditions used to build it, so the result "
            "may be less reliable. Follow local weather alerts, and do not use this "
            "number by itself to decide if it is safe outside."
        )

    st.markdown("#### What this number means")
    st.write(
        "The heat index shows how hot it feels when you look at temperature and "
        "humidity together instead of looking at temperature by itself. It is based "
        "on shady conditions with light wind. Direct sun, being active, clothing, "
        "health, and other things can add to the heat risk, so this number alone "
        "cannot tell you if it is safe to be outside."
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
    st.caption(f"Your selected point: {humidity}% humidity → {heat_index:.1f}°F heat index.")
    st.caption(
        "This graph shows that even if the temperature stays the same, more humidity "
        "can make it feel a lot hotter outside. That is something I noticed this "
        "summer in North Carolina."
    )
    compare_low = calculate_heat_index(temperature, 30)
    compare_high = calculate_heat_index(temperature, 80)
    st.info(
        f"At {temperature}°F, it feels like around {compare_low:.0f}°F with 30% "
        f"humidity and around {compare_high:.0f}°F with 80% humidity."
    )

    st.markdown("#### A few ways to lower your risk")
    recommendations = {
        "Below caution": ["Keep some water nearby and check the forecast before you go outside."],
        "Caution": ["Drink water regularly.", "If you are outside for a while, take breaks and find some shade."],
        "Extreme Caution": ["If you can, walk or play sports during the cooler parts of the day.", "Take frequent breaks in the shade or somewhere with AC.", "Check in on friends and family."],
        "Danger": ["Cut back on hard outdoor activity and take frequent breaks to cool down.", "Go somewhere with AC when you can.", "Pay attention to how you feel and check on people around you."],
        "Extreme Danger": ["Avoid strenuous outdoor activity.", "Spend time somewhere cool or air-conditioned.", "Check on others and follow local weather alerts."],
    }
    for tip in recommendations[category]:
        st.markdown(f"- {tip}")
    st.markdown(
        "On top of that, not everyone can afford to keep their AC running all the time, "
        "so some people may have a harder time staying cool when it is really hot. "
        "Check what cooling spaces are available through your county or health "
        "department, and check in on people around you."
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
        "This summer I noticed how hot and humid it was getting in North Carolina, "
        "and it even felt like the heat lasted into Fall. I think most people know it "
        "gets hot here, but they may not know how humidity adds to the heat risk. "
        "Warmer nights can also give people less time to cool down after a hot day. "
        "This worries me because it can make it harder for me, my loved ones, and "
        "other people to spend time outside, especially if they cannot afford to keep "
        "their home cool with AC."
    )
    st.markdown(
        '<div class="fact"><strong>If emissions keep rising quickly, North Carolina '
        'could warm another 6 to 10°F by 2100.</strong><br><br>The report projects '
        'this change in the statewide average temperature under a higher-emissions '
        'scenario. It is a long-term projection, not a guarantee or a forecast for '
        'one day.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "Source: [North Carolina Climate Science Report: Plain Language Summary "
        "(2020)](https://files.nc.gov/ncdeq/climate-change/climate-scinece-report/"
        "NC-Climate-Science-Report_Plain_Language_Summary.pdf) · "
        "[NC State Climate Office](https://climate.ncsu.edu/)"
    )
    st.info(
        "The calculator shows how temperature and humidity affect how hot it feels. "
        "The climate report is about long-term changes in climate. The calculator "
        "does not prove climate change by itself."
    )
    st.subheader("What Can We Do?")
    st.markdown(
        "- Talk to friends and family about climate change and share what you learned about heat safety.\n"
        "- Check in on people during hot weather and support local cooling spaces.\n"
        "- Learn about ways we can lower greenhouse gas emissions, both on our own and together.\n"
        "- Try NC Heat Helper and share it with friends or family."
    )

with quiz_tab:
    st.header("Quick Quiz")
    st.write("You have seen how humidity can change how hot it feels. Try these questions and see what you think.")
    questions = [
        ("What can humidity do to how hot it feels outside?", ["Humidity always makes the air feel cooler.", "Humidity can make it feel hotter because sweat does not dry as fast.", "Humidity does not affect how hot it feels."], 1,
         "Humidity makes it harder for sweat to evaporate, which is one way your body cools itself."),
        ("Why should you take breaks or slow down when it is extremely hot?", ["Taking a break makes the air cooler.", "It is always unsafe to exercise outside in summer.", "Taking breaks gives your body time to cool down and can lower heat strain."], 2,
         "Being active adds to the heat your body is dealing with, so breaks can help lower that strain."),
        ("Why can people without reliable AC have a harder time during extreme heat?", ["It changes the humidity outside.", "They may not have an easy place to cool down.", "It makes every hot day dangerous."], 1,
         "Without reliable AC, people may have fewer ways to get away from indoor heat."),
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
    "This app is for learning and does not replace official weather warnings or "
    "medical advice. The heat index does not include everything that matters for "
    "sports or hard physical activity, so use official guidance and a more complete "
    "heat-stress measure when one is needed."
)
