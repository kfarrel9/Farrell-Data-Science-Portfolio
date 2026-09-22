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

# introduce app and describe features
st.write(
    "Learn more about Adelie, Chinstrap, and Gentoo penguins. "
    "Filter the data and compare different characteristics between the species. "
    "Explore maps, summary statistics, and visualizations throughout the app."
)

# fun button for balloons!
if st.button("Click if you love penguins!"):
    st.balloons()

# Create tabs, one for each species
adelie_tab, chinstrap_tab, gentoo_tab = st.tabs(["Adelie", "Chinstrap", "Gentoo"])


# ADELIE TAB
##############################

with adelie_tab:

    st.header("Adelie Penguins")
    st.image("images/Adelie Penguin.png", width=300)

    # list of random adelie facts
    adelie_facts = ["Males build nests out of pebbles and will steal rocks from neighboring nests when nobody is looking.",
    "Their feces releases ammonia that helps form clouds and fertilizes the barren Antarctic ground.",
    "Despite their small size, they fearlessly fight predators or humans by slapping them with their flippers."]

    # show a random fact from list when button is clicked
    if st.button("Show Adelie Fact"):
        fact = random.choice(adelie_facts)
        st.toast(fact)

    # lets users rate adelie penguins for fun
    rating = st.slider("How much do you like Adelie penguins?", 0,10,5)
    st.write(f"You rated Adelie penguins {rating}/10!")

    # Keep only Adelie penguins
    adelie = penguins[penguins["species"] == "Adelie"]

    # Get islands where Adelie penguins are found
    adelie_islands = adelie["island"].dropna().unique()

    # Let user choose islands to look at
    selected_adelie_islands = st.multiselect(
        "Select island",
        options=adelie_islands,
        default=adelie_islands,
    )

    # update data based on isladns selected
    filtered_adelie = adelie[adelie["island"].isin(selected_adelie_islands)]

    # allows user to view the filtered data in a table
    if st.checkbox("Show Adelie Data"):
        st.dataframe(filtered_adelie) 

    #Shows some fun stats
    st.subheader("Quick Summary Statistics")

    # creates three columns
    column1, column2, column3 = st.columns(3)

    # Find the number of Adelie penguins
    number_adelie = len(filtered_adelie)

    # Find the average body mass
    average_mass = filtered_adelie["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_adelie["flipper_length_mm"].mean()


    # Display the statistics
    column1.metric( "Number of Penguins",number_adelie)

    column2.metric("Average Body Mass", str(round(average_mass)) + " g")

    column3.metric("Average Flipper Length", str(round(average_flipper, 1)) + " mm")


    # Scatterplot
    st.subheader("Explore Relationships Between Features Of Adelie Penguins")

    # lets user chose x axis to compare
    x_adelie = st.selectbox(
        "Choose x-axis",
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g"
        ],
    )

    # lets user chose y stat to explore
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

    # makes scatter plt
    fig, ax = plt.subplots()

    sns.scatterplot(
        data=filtered_adelie,
        x=x_adelie,
        y=y_adelie,
        hue="island",
        ax=ax
    )

    # plot 
    st.pyplot(fig)

    # Show where adelie islands are located
    st.subheader("Map Of Adelie Penguin Islands")

    # coordinates of these isaldns on world map
    adelie_map = pd.DataFrame({
        "island": ["Biscoe", "Dream", "Torgersen"],
        "lat": [-64.8131, -64.7268, -64.7731],
        "lon": [-63.7947, -64.2248, -64.0741]
    })

    # only shows isalnds rthat user selected above
    selected_map = adelie_map[
        adelie_map["island"].isin(selected_adelie_islands)
    ]

    # plots map
    st.map(
        selected_map,
        latitude="lat",
        longitude="lon"
    )

    st.write("Map shows the locations of the selected islands.")

# CHINSTRAP TAB
####################################

with chinstrap_tab:

    # introduce chinstrap penguins
    st.header("Chinstrap Penguins")
    st.image("images/Chinstrap Penguin.png", width=300)

    # list of chinstrap penguin facts
    chinstrap_facts = [
    "Chinstrap penguins take more than 10,000 tiny four-second naps a day during the breeding season!", 
    "People sometimes call them stonecracker penguins because their loud, piercing screech sounds like it could crack stone.",
    "Their poop is bright pink because they eat a diet rich in Antarctic krill. It is sometimes so bright that you can see it from space.",
    "Scientists consider them the most aggressive and grumpiest of all penguin species, often picking fights with neighbors, intruders, and even humans."]

    # randomly selcts a fact from list if button is clicked
    if st.button("Show Chinstrap Fact"):
        fact = random.choice(chinstrap_facts)
        st.toast(fact)

    # if check box is clicked, displays text
    if st.checkbox("I am a Chinstrap fan"):
        st.write("Welcome to the Chinstrap fan club ;)")

    # pulls out chinstrap penguin data
    chinstrap = penguins[
        penguins["species"] == "Chinstrap"
    ]

    # get the isalnds that chinstrap penguins live on
    chinstrap_islands = chinstrap["island"].dropna().unique()

    # let used choose which islands to look at
    selected_chinstrap_islands = st.multiselect(
        "Select island",
        options=chinstrap_islands,
        default=chinstrap_islands,
    )

    # update data based on the isaldns selected
    filtered_chinstrap = chinstrap[chinstrap["island"].isin(selected_chinstrap_islands)]

    # allows user to view the filtered data in a data frame
    if st.checkbox("Show Chinstrap Data"):
        st.dataframe(filtered_chinstrap) 

    # DISPLAY OF SUMMARY statistics
    st.subheader("Quick Summary Statistics")

    column1, column2, column3 = st.columns(3)

    # Find the number of Chinstrap penguins
    number_chinstrap = len(filtered_chinstrap)

    # Find the average body mass
    average_mass = filtered_chinstrap["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_chinstrap["flipper_length_mm"].mean()


    # Display the statistics
    column1.metric(
        "Number of Penguins",
        number_chinstrap
    )

    column2.metric(
        "Average Body Mass",
        str(round(average_mass)) + " g"
    )

    column3.metric(
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

    # introduce gentoo penuins
    st.header("Gentoo Penguins")
    st.image("images/Gentoo Penguin.png", width=300)

    # make list of fun facts about gentoo penguins
    gentoo_facts = ["Gentoo penguins are the fastest swimming penguins in the world!",
    "Male gentoos search for the smoothest, most attractive pebbles to present to females as a romantic gift and building material for their nests."
    "Once a year, they go through a catastrophic molt where they shed all their old feathers at once, making them look comically disheveled before new waterproof plumage grows in."]

    # randlomly displays a fact from list if bitton is selected
    if st.button("Show Gentoo Fact"):
            fact = random.choice(gentoo_facts)
            st.toast(fact)
   
    # makes it snow! fun button!
    if st.button("Click here to make it snow!"):
        st.snow()

    # pull out only the gentoo penguins
    gentoo = penguins[penguins["species"] == "Gentoo"]

    # gets the islands that gentoo penuins live on
    gentoo_islands = gentoo[ "island"].dropna().unique()

    # lets used chose wqhich islands to look at (if more than 1)
    selected_gentoo_islands = st.multiselect(
        "Select island",
        options=gentoo_islands,
        default=gentoo_islands,
    )

    # update the data based on the isaldns selected
    filtered_gentoo = gentoo[ gentoo["island"].isin(selected_gentoo_islands)]

    # allows user to view filtered data \
    if st.checkbox("Show Gentoo Data"):
        st.dataframe(filtered_gentoo) 

    # display summary statistics
    st.subheader("Quick Summary Statistics")

    column1, column2, column3 = st.columns(3)

   # Find the number of Gentoo penguins
    number_gentoo = len(filtered_gentoo)

    # Find the average body mass
    average_mass = filtered_gentoo["body_mass_g"].mean()

    # Find the average flipper length
    average_flipper = filtered_gentoo["flipper_length_mm"].mean()

    # Display the statistics
    column1.metric("Number of Penguins", number_gentoo)

    column2.metric("Average Body Mass", round(average_mass), "g")

    column3.metric("Average Flipper Length", round(average_flipper, 1), "mm")      

    st.subheader("Gentoo Body Mass Distribution")

    # Let the user choose which Gentoo penguins to look at, male female or both
    sex_choice = st.radio(
        "Choose which Gentoo penguins to view",
        ["All", "Male", "Female"]
    )

    # filters data based on users choice
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

    # creates histogram
    fig, ax = plt.subplots()

    sns.histplot(
        data=gentoo_graph,
        x="body_mass_g",
        bins=10,
        ax=ax
    )

    # set title, x and y labels
    ax.set_xlabel("Body Mass (g)")
    ax.set_ylabel("Number of Penguins")
    ax.set_title("Distribution of Gentoo Body Mass")

    # display graph
    st.pyplot(fig)