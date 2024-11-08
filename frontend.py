import streamlit as st
import plotly.graph_objects as go
import base64
import requests

# Set up page config
st.set_page_config(page_title="Iris Species Prediction Dashboard", page_icon="🌸", layout="wide")

# Load and encode image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Set background image using base64
bg_image_path = "Image.jpg"  # Ensure Image.jpg is in the same directory
bg_image_base64 = get_base64_image(bg_image_path)

# Read the CSS file
with open("style.css", "r") as css_file:
    css_content = css_file.read()

# Replace the placeholder in CSS with the base64 image string
css_content = css_content.replace("{bg_image_base64}", bg_image_base64)

# Apply CSS
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Apply overlay
st.markdown("<div class='overlay'>", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: white;'>🌸 Iris Species Prediction Dashboard 🌸</h1>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header("Input Flower Measurements")
sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.0, 8.0, 5.8)
sepal_width = st.sidebar.slider('Sepal Width (cm)', 2.0, 5.0, 3.0)
petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 6.9, 4.3)
petal_width = st.sidebar.slider('Petal Width (cm)', 0.0, 2.5, 1.2)

# Input data for prediction
input_data = [sepal_length, sepal_width, petal_length, petal_width]

# Default content before prediction is made
# st.markdown("### Please enter the flower measurements on the sidebar and click 'Predict Species' to see the prediction results.")

# Predict button
if st.sidebar.button("Predict Species"):
    with st.spinner("Predicting..."):
        try:
            # Send the data to the FastAPI backend
            response = requests.post('http://localhost:8000/predict/', json={"features": input_data})
            response.raise_for_status()
            prediction = response.json()['class']
            st.markdown(f"<h2 style='text-align: center; color: lightgreen;'>Predicted Species: {prediction}</h2>", unsafe_allow_html=True)
        except requests.exceptions.RequestException as e:
            st.error("Error: Could not get prediction. Please ensure the server is running.")

        # Placeholder species averages (for demonstration purposes)
        species_means = {
            "Setosa": [5.0, 3.4, 1.5, 0.2],
            "Versicolor": [5.9, 2.8, 4.2, 1.3],
            "Virginica": [6.5, 3.0, 5.6, 2.0]
        }

        # Dashboard Summary Section
        st.success("### Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Sepal Length", f"{sepal_length} cm")
        col2.metric("Sepal Width", f"{sepal_width} cm")
        col3.metric("Petal Length", f"{petal_length} cm")
        col4.metric("Petal Width", f"{petal_width} cm")

        # Analytics Overview Section
        st.markdown("## Analytics Overview")

        # Layout for analytics charts
        col1, col2 = st.columns(2)

        # Bar Chart: Input values vs Species Averages
        with col1:
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(
                name="Input Values",
                x=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
                y=input_data,
                marker_color="cyan"
            ))

            for species, means in species_means.items():
                fig1.add_trace(go.Bar(
                    name=f"{species} Mean",
                    x=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
                    y=means,
                    opacity=0.6
                ))

            fig1.update_layout(
                title="Input Values vs Species Averages",
                barmode="group",
                paper_bgcolor="rgba(255,255,255,0.2)",  # Lighter background for better visibility
                plot_bgcolor="rgba(255,255,255,0.2)",   # Lighter plot area
                font=dict(color="#f0f0f0"),
                yaxis_title="Measurement (cm)",
                legend=dict(font=dict(color="#f0f0f0"))
            )
            st.plotly_chart(fig1, use_container_width=True, height=400)

        # Line Chart: Comparison of input dimensions across species
        with col2:
            fig2 = go.Figure()

            fig2.add_trace(go.Scatter(
                x=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
                y=input_data,
                mode="lines+markers",
                name="Input",
                line=dict(color="cyan", width=4)
            ))

            for species, means in species_means.items():
                fig2.add_trace(go.Scatter(
                    x=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
                    y=means,
                    mode="lines",
                    name=f"{species} Mean",
                    line=dict(width=2, dash='dash')
                ))

            fig2.update_layout(
                title="Input vs Species Dimension Trends",
                paper_bgcolor="rgba(255,255,255,0.2)",  # Lighter background for better visibility
                plot_bgcolor="rgba(255,255,255,0.2)",
                font=dict(color="#f0f0f0"),
                xaxis_title="Dimensions",
                yaxis_title="Measurement (cm)"
            )
            st.plotly_chart(fig2, use_container_width=True, height=400)
else:
    # Display message when the prediction button has not been clicked yet
    st.warning("### Please enter the measurements and click the 'Predict Species' button.")