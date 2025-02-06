import numpy as np
import pandas as pd
import streamlit as st

from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import GradientBoostingClassifier


DATA = "./data/mushrooms.csv"
COLS = [
    "class",
    "odor",
    "gill-size",
    "gill-color",
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",
    "stalk-color-below-ring",
    "ring-type",
    "spore-print-color",
]


@st.cache_data(show_spinner="Fetching data...")
def read_data(url, cols):
    df = pd.read_csv(url)
    df = df[cols]

    return df


@st.cache_resource
def get_target_encoder(data):
    label_encoder = LabelEncoder()
    label_encoder.fit(data["class"])

    return label_encoder


@st.cache_resource
def get_features_encoder(data):
    ordinal_encoder = OrdinalEncoder()
    cols = data.columns[1:]
    ordinal_encoder.fit(data[cols])

    return ordinal_encoder


@st.cache_data(show_spinner="Encoding data...")
def encode_data(data, _features_encoder, _target_encoder):
    data["class"] = _target_encoder.transform(data["class"])

    cols = data.columns[1:]
    data[cols] = _features_encoder.transform(data[cols])

    return data


@st.cache_resource(show_spinner="Training model...")
def train_model(data):
    x = data.drop(["class"], axis=1)
    y = data["class"]

    model = GradientBoostingClassifier(max_depth=5, random_state=42)

    model.fit(x, y)

    return model


@st.cache_data(show_spinner="Making a prediction...")
def make_prediction(_model, _features_encoder, x):
    features = [feature[0] for feature in x]
    features = np.array(features).reshape(1, -1)
    encoded_features = _features_encoder.transform(features)

    y_hat = _model.predict(encoded_features)

    return y_hat[0]


if __name__ == "__main__":
    # display project title
    st.title("Mushroom classifier 🍄")

    # fetch the data
    df = read_data(DATA, COLS)

    # display dashboard
    st.subheader("Step 1: Select the values for prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        odor = st.selectbox('Odor', ('a - almond', 'l - anisel', 'c - creosote', 'y - fishy', 'f - foul', 'm - musty', 'n - none', 'p - pungent', 's - spicy'))
        stalk_surface_above_ring = st.selectbox('Stalk surface above ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
        stalk_color_below_ring = st.selectbox('Stalk color below ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
    with col2:
        gill_size = st.selectbox('Gill size', ('b - broad', 'n - narrow'))
        stalk_surface_below_ring = st.selectbox('Stalk surface below ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
        ring_type = st.selectbox('Ring type', ('e - evanescente', 'f - flaring', 'l - large', 'n - none', 'p - pendant', 's - sheathing', 'z - zone'))
    with col3:
        gill_color = st.selectbox('Gill color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'g - gray', 'r - green', 'o - orange', 'p - pink', 'u - purple', 'e - red', 'w - white', 'y - yellow'))
        stalk_color_above_ring = st.selectbox('Stalk color above ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
        spore_print_color = st.selectbox('Spore print color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'r - green', 'o - orange', 'u - purple', 'w - white', 'y - yellow'))

    st.subheader("Step 2: Ask the model for a prediction")

    predict_btn = st.button("Predict", type="primary")

    if predict_btn:
        target_encoder = get_target_encoder(df)
        features_encoder = get_features_encoder(df)

        encoded_data = encode_data(df, features_encoder, target_encoder)

        model = train_model(encoded_data)

        x = [
            odor,
            gill_size,
            gill_color,
            stalk_surface_above_ring,
            stalk_surface_below_ring,
            stalk_color_above_ring,
            stalk_color_below_ring,
            ring_type,
            spore_print_color,
        ]

        y_hat = make_prediction(model, features_encoder, x)

        message = "The mushroom is poisonous 🤢" if y_hat == 1 else "The mushroom is edible 🍴"

        st.write(message)
