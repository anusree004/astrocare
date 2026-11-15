
import streamlit as st
import pandas as pd
import random
import requests
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AstroCare",
    page_icon="🚀",
    layout="wide"
)


# --------------------------------
# SPACE THEME DESIGN
# --------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #071426;
    color: white;
}

h1, h2, h3 {
    color: #00D9FF !important;
}

[data-testid="stMetric"] {
    background-color: #132943;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #174B70;
}

[data-testid="stMetricValue"] {
    color: #00D9FF;
}

[data-testid="stSidebar"] {
    background-color: #10243B;
}

.stAlert {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------
# MAIN TITLE
# --------------------------------

st.title("🚀 AstroCare")

st.subheader(
    "Astronaut Health Monitoring System"
)

st.info(
    "🌌 Space Mission Health Monitoring | Simulated Data"
)


# --------------------------------
# ASTRONAUT PROFILE
# --------------------------------

st.sidebar.title("👩‍🚀 Astronaut Profile")

st.sidebar.write("Name: Astronaut 01")
st.sidebar.write("Mission: Space Exploration")
st.sidebar.write("Status: Active")
st.sidebar.write("Location: Space Station")


# --------------------------------
# HEALTH READINGS
# --------------------------------

heart_rate = random.randint(65, 105)
oxygen = random.randint(92, 100)
temperature = round(random.uniform(36.2, 37.6), 1)
sleep = random.randint(4, 9)


# --------------------------------
# HEALTH OVERVIEW
# --------------------------------

st.markdown("## 🩺 Health Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "❤️ Heart Rate",
    f"{heart_rate} BPM"
)

col2.metric(
    "🫁 Oxygen Level",
    f"{oxygen}%"
)

col3.metric(
    "🌡️ Temperature",
    f"{temperature} °C"
)

col4.metric(
    "😴 Sleep",
    f"{sleep} Hours"
)

st.divider()


# --------------------------------
# HEALTH HISTORY
# --------------------------------

st.markdown("## 📊 Health Monitoring History")

period = st.selectbox(
    "Select Monitoring Period",
    ["Last 6 Hours", "Last 12 Hours", "Last 24 Hours"]
)

if period == "Last 6 Hours":
    count = 6

elif period == "Last 12 Hours":
    count = 12

else:
    count = 24


heart_data = [
    random.randint(65, 105)
    for i in range(count)
]

oxygen_data = [
    random.randint(92, 100)
    for i in range(count)
]

time_labels = [
    f"{i+1}h"
    for i in range(count)
]


df = pd.DataFrame({
    "Time": time_labels,
    "Heart Rate (BPM)": heart_data,
    "Oxygen Level (%)": oxygen_data
})


chart1, chart2 = st.columns(2)

with chart1:

    st.write("❤️ Heart Rate History")

    st.line_chart(
        df.set_index("Time")["Heart Rate (BPM)"]
    )


with chart2:

    st.write("🫁 Oxygen Level History")

    st.line_chart(
        df.set_index("Time")["Oxygen Level (%)"]
    )

st.divider()


# --------------------------------
# HEALTH ALERT SYSTEM
# --------------------------------

st.markdown("## 🚨 Health Alert System")

alerts = []

if heart_rate > 100:
    alerts.append("High heart rate detected!")

if oxygen < 95:
    alerts.append("Low oxygen level detected!")

if temperature > 37.2:
    alerts.append(
        "Temperature is above the demo threshold!"
    )

if sleep < 6:
    alerts.append(
        "Sleep duration is below the demo target!"
    )


if alerts:

    st.error("⚠️ Attention Required")

    for alert in alerts:
        st.warning(alert)

else:

    st.success(
        "✅ All simulated readings are within configured demo limits."
    )

st.caption(
    "Alerts use illustrative thresholds and are not medical diagnoses."
)

st.divider()


# --------------------------------
# PDF HEALTH REPORT
# --------------------------------

st.markdown("## 📄 Astronaut Health Report")


def create_pdf_report():

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AstroCare Health Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Astronaut: Astronaut 01",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Mission: Space Exploration",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    data = [
        ["Health Parameter", "Recorded Value"],
        ["Heart Rate", f"{heart_rate} BPM"],
        ["Oxygen Level", f"{oxygen}%"],
        ["Temperature", f"{temperature} C"],
        ["Sleep Duration", f"{sleep} Hours"]
    ]

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.navy),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 10),
    ]))

    content.append(table)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Health Alerts",
            styles["Heading2"]
        )
    )

    if alerts:

        for alert in alerts:

            content.append(
                Paragraph(alert, styles["Normal"])
            )

    else:

        content.append(
            Paragraph(
                "No configured demo alerts.",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "All readings are simulated for demonstration "
            "purposes and are not real medical measurements.",
            styles["Italic"]
        )
    )

    pdf.build(content)

    buffer.seek(0)

    return buffer.getvalue()


pdf_data = create_pdf_report()

st.download_button(
    label="📥 Download Health Report (PDF)",
    data=pdf_data,
    file_name="AstroCare_Health_Report.pdf",
    mime="application/pdf"
)

st.divider()


# --------------------------------
# NASA RESEARCH DATA INTEGRATION
# --------------------------------

# --------------------------------
# NASA RESEARCH DATA INTEGRATION
# --------------------------------

st.markdown("## 🛰️ NASA Research Data")

st.write(
    "Explore space biology research datasets "
    "from NASA's Open Science Data Repository."
)

if st.button("🔍 Fetch NASA Research Data"):

    nasa_url = "https://osdr.nasa.gov/osdr/data/search"

    params = {
        "term": "spaceflight",
        "from": 0,
        "size": 10,
        "type": "cgene"
    }

    try:

        with st.spinner("Connecting to NASA..."):

            response = requests.get(
                nasa_url,
                params=params,
                timeout=30
            )

            response.raise_for_status()
            nasa_data = response.json()

        st.success("NASA data retrieved successfully!")

        # Extract results
        results = (
            nasa_data.get("hits", {})
            .get("hits", [])
        )

        st.markdown("### 📚 Research Datasets")

        if results:

            st.write(
                f"Datasets found: {len(results)}"
            )

            for item in results:

                source = item.get("_source", {})

                # NASA uses these field names
                dataset_id = (
                    source.get("Accession")
                    or source.get("accession")
                    or "Not provided"
                )

                title = (
                    source.get("Study Title")
                    or source.get("study_title")
                    or "Title not provided"
                )

                description = (
                    source.get("Study Description")
                    or source.get("study_description")
                    or source.get("Description")
                    or "Description not provided by NASA search results."
                )

                with st.expander(f"🧬 {title}"):

                    st.write(
                        "**Dataset ID:**",
                        dataset_id
                    )

                    st.write(
                        "**Research Information:**"
                    )

                    st.write(description)

                    st.write(
                        "**Data Source:** NASA OSDR"
                    )

                    st.write(
                        "**Dataset Type:**",
                        source.get("Data Source Type", "Not specified")
                    )

        else:

            st.warning("No matching datasets found.")

    except requests.exceptions.RequestException as e:

        st.error(f"NASA connection error: {e}")

    except (ValueError, AttributeError):

        st.error("Unable to read NASA research data.")

st.caption(
    "Source: NASA Open Science Data Repository. "
    "Research datasets are not live astronaut health measurements."
)



# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.markdown("### 🌌 AstroCare")

st.caption(
    "Astronaut Health Monitoring System | "
    "NASA Space Apps Challenge 2026"
)

st.caption(
    "Prototype using simulated health readings "
    "and publicly available NASA research data."
)
