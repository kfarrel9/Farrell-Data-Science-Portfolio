import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps
import random # allows use of random generation

#########################################
# Load the data
penguins = pd.read_csv("data/penguins.csv")

# Title and description
st.title("Palmer Penguins Explorer")

st.write(
    "Learn more about Adelie, Chinstrap, and Gentoo penguins. "
    "Filter the data and compare different characteristics between the species. "
    "Explore maps, summary statistics, and visualizations throughout the app."
)

if st.button("Click if you love penguins!"):
    st.balloons()

# Create tabs
adelie_tab, chinstrap_tab, gentoo_tab = st.tabs(["Adelie", "Chinstrap", "Gentoo"])


# ADELIE TAB
##############################

with adelie_tab:

    st.header("Adelie Penguins")
    st.image("images/Adelie Penguin.png", width=300)

    adelie_facts = ["Males build nests out of pebbles and will steal rocks from neighboring nests when nobody is looking.",
    "Their feces releases ammonia that helps form clouds and fertilizes the barren Antarctic ground.",
    "Despite their small size, they fearlessly fight predators or humans by slapping them with their flippers."]
        
    if st.button("Show Adelie Fact"):
        fact = random.choice(adelie_facts)
        st.toast(fact)

    rating = st.slider("How much do you like Adelie penguins?", 0,10,5)
    st.write(f"You rated Adelie penguins {rating}/10!")

    # Keep only Adelie penguins
    adelie = penguins[penguins["species"] == "Adelie"]

    # Get islands where Adelie penguins are found
    adelie_islands = adelie["island"].dropna().unique()

    # Let user choose islands
    selected_adelie_islands = st.multiselect(
        "Select island",
        options=adelie_islands,
        default=adelie_islands,
    )

    # Filter Adelie penguins by selected islands
    filtered_adelie = adelie[adelie["island"].isin(selected_adelie_islands)]

    # Quick summary
    st.subheader("Quick Summary Statistics")

    col1, col2, col3 = st.columns(3)

    # Find the number of Adelie penguins
    number_adelie = len(filtered_adelie)

    # Find the average body mass
    average_mass = filtered_adelie["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_adelie["flipper_length_mm"].mean()


    # Display the statistics
    col1.metric( "Number of Penguins",number_adelie)

    col2.metric("Average Body Mass", str(round(average_mass)) + " g")

    col3.metric("Average Flipper Length", str(round(average_flipper, 1)) + " mm")


    # Scatterplot
    st.subheader("Explore Relationships Between Features Of Adelie Penguins")

    x_adelie = st.selectbox(
        "Choose x-axis",
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ],
    )

    y_adelie = st.selectbox(
        "Choose y-axis",
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ],
        index=3,
    )

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=filtered_adelie,
        x=x_adelie,
        y=y_adelie,
        hue="island",
        ax=ax
    )

    st.pyplot(fig)

    # Map
    st.subheader("Map Of Adelie Penguin Islands")

    adelie_map = pd.DataFrame({
        "island": ["Biscoe", "Dream", "Torgersen"],
        "lat": [-64.8131, -64.7268, -64.7731],
        "lon": [-63.7947, -64.2248, -64.0741]
    })

    selected_map = adelie_map[
        adelie_map["island"].isin(selected_adelie_islands)
    ]

    st.map(
        selected_map,
        latitude="lat",
        longitude="lon"
    )

    st.write("Map shows the locations of the selected islands.")

# CHINSTRAP TAB
####################################

with chinstrap_tab:

    st.header("Chinstrap Penguins")
    st.image("images/Chinstrap Penguin.png", width=300)

    chinstrap_facts = [
    "Chinstrap penguins take more than 10,000 tiny four-second naps a day during the breeding season!", 
    "People sometimes call them stonecracker penguins because their loud, piercing screech sounds like it could crack stone.",
    "Their poop is bright pink because they eat a diet rich in Antarctic krill. It is sometimes so bright that you can see it from space.",
    "Scientists consider them the most aggressive and grumpiest of all penguin species, often picking fights with neighbors, intruders, and even humans."]

    if st.button("Show Chinstrap Fact"):
        fact = random.choice(chinstrap_facts)
        st.toast(fact)

    if st.checkbox("I am a Chinstrap fan"):
        st.write("Welcome to the Chinstrap fan club ;)")

    chinstrap = penguins[
        penguins["species"] == "Chinstrap"
    ]

    chinstrap_islands = chinstrap["island"].dropna().unique()

    selected_chinstrap_islands = st.multiselect(
        "Select island",
        options=chinstrap_islands,
        default=chinstrap_islands,
    )

    filtered_chinstrap = chinstrap[chinstrap["island"].isin(selected_chinstrap_islands)]

    st.subheader("Quick Summary Statistics")

    col1, col2, col3 = st.columns(3)

   # Find the number of Chinstrap penguins
    number_chinstrap = len(filtered_chinstrap)

    # Find the average body mass
    average_mass = filtered_chinstrap["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_chinstrap["flipper_length_mm"].mean()


    # Display the statistics
    col1.metric(
        "Number of Penguins",
        number_chinstrap
    )

    col2.metric(
        "Average Body Mass",
        str(round(average_mass)) + " g"
    )

    col3.metric(
        "Average Flipper Length",
        str(round(average_flipper, 1)) + " mm"
    )

    st.subheader("Compare Male vs. Female Chinstrap Penguins")

    # Let the user choose which measurement to compare
    measurement = st.selectbox(
        "Choose a characteristic",
        [
            "body_mass_g",
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm"
        ]
    )

    # Create the box plot
    fig, ax = plt.subplots()

    sns.boxplot(
        data=filtered_chinstrap,
        x="sex",
        y=measurement,
        palette={
            "male": "blue",
            "female": "pink"
        },
        ax=ax
    )

    st.pyplot(fig)

# GENTOO TAB
###################################

with gentoo_tab:

    st.header("Gentoo Penguins")
    st.image("images/Gentoo Penguin.png", width=300)


    gentoo_facts = ["Gentoo penguins are the fastest swimming penguins in the world!",
    "Male gentoos search for the smoothest, most attractive pebbles to present to females as a romantic gift and building material for their nests."
    "Once a year, they go through a catastrophic molt where they shed all their old feathers at once, making them look comically disheveled before new waterproof plumage grows in."]
    
    if st.button("Show Gentoo Fact"):
            fact = random.choice(gentoo_facts)
            st.toast(fact)
   

    if st.button("Click here to make it snow!"):
        st.snow()


    gentoo = penguins[penguins["species"] == "Gentoo"]

    gentoo_islands = gentoo[ "island"].dropna().unique()

    selected_gentoo_islands = st.multiselect(
        "Select island",
        options=gentoo_islands,
        default=gentoo_islands,
    )

    filtered_gentoo = gentoo[ gentoo["island"].isin(selected_gentoo_islands)]

    st.subheader("Quick Summary Statistics")

    col1, col2, col3 = st.columns(3)

   # Find the number of Gentoo penguins
    number_gentoo = len(filtered_gentoo)

    # Find the average body mass
    average_mass = filtered_gentoo["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_gentoo["flipper_length_mm"].mean()

    # Display the statistics
    col1.metric("Number of Penguins", number_gentoo)

    col2.metric("Average Body Mass", round(average_mass), "g")

    col3.metric("Average Flipper Length", round(average_flipper, 1), "mm")      

    st.subheader("Gentoo Body Mass Distribution")

    sex_choice = st.radio(
        "Choose which Gentoo penguins to view",
        ["All", "Male", "Female"]
    )

    if sex_choice == "Male":
        gentoo_graph = filtered_gentoo[
            filtered_gentoo["sex"] == "male"
        ]

    elif sex_choice == "Female":
        gentoo_graph = filtered_gentoo[
            filtered_gentoo["sex"] == "female"
        ]

    else:
        gentoo_graph = filtered_gentoo


    fig, ax = plt.subplots()

    sns.histplot(
        data=gentoo_graph,
        x="body_mass_g",
        bins=10,
        ax=ax
    )

    ax.set_xlabel("Body Mass (g)")
    ax.set_ylabel("Number of Penguins")
    ax.set_title("Distribution of Gentoo Body Mass")

    st.pyplot(fig)