import streamlit as st

# Sample recipe data with categories
recipes = {
    "Breakfast Dishes": {
        "Idli": ["rice", "urad dal", "salt"],
        "Dosa": ["rice", "urad dal", "salt", "ghee"],
        "Uttapam": ["dosa batter", "onions", "tomatoes", "green chilies", "coriander"],
        "Pongal": ["rice", "moong dal", "pepper", "cumin", "ghee", "ginger"],
        "Upma": ["semolina", "mustard seeds", "curry leaves", "vegetables", "water"],
        "Aloo Paratha": ["potatoes", "flour", "spices", "butter"],
        "Poha": ["flattened rice", "onions", "peas", "spices"],
        "Rawa Idli": ["semolina", "yogurt", "salt"],
        "Vegetable Omelette": ["eggs", "vegetables", "spices"],
        "Masala Dosa": ["dosa batter", "spiced potatoes"]
    },
    "Snacks & Appetizers": {
        "Vada": ["urad dal", "onion", "green chilies", "salt", "oil"],
        "Medu Vada": ["urad dal", "pepper", "curry leaves", "salt"],
        "Samosa": ["potatoes", "peas", "spices", "flour"],
        "Chaat": ["potatoes", "chickpeas", "spices", "yogurt"],
        "Onion Pakora": ["onions", "besan", "spices", "oil"],
        "Vegetable Spring Rolls": ["spring roll sheets", "mixed vegetables", "spices"],
        "Pani Puri": ["puri", "spiced water", "potatoes", "chickpeas"],
        "Masala Papad": ["papad", "spices", "onions", "tomatoes"],
        "Bhel Puri": ["puffed rice", "vegetables", "chutneys"],
        "Chivda": ["flattened rice", "peanuts", "spices"]
    },
    "Soups & Curries": {
        "Sambar": ["toor dal", "tamarind", "vegetables", "sambar powder", "mustard seeds"],
        "Rasam": ["tamarind", "tomatoes", "rasam powder", "mustard seeds", "curry leaves"],
        "Vegetable Kurma": ["mixed vegetables", "coconut", "spices"],
        "Paneer Butter Masala": ["paneer", "tomatoes", "cream", "spices"],
        "Chana Masala": ["chickpeas", "tomatoes", "spices"],
        "Kootu": ["vegetables", "moong dal", "coconut"],
        "Dal Tadka": ["toor dal", "onion", "spices", "ghee"],
        "Vegetable Korma": ["mixed vegetables", "yogurt", "spices"],
        "Methi Malai Murg": ["chicken", "fenugreek", "cream", "spices"],
        "Aloo Gobi": ["potatoes", "cauliflower", "spices"]
    },
    "Main Dishes": {
        "Bisi Bele Bath": ["rice", "toor dal", "mixed vegetables", "bisi bele bath powder"],
        "Khichdi": ["rice", "moong dal", "spices"],
        "Lemon Rice": ["rice", "lemon juice", "turmeric", "mustard seeds"],
        "Coconut Rice": ["rice", "coconut", "spices"],
        "Vegetable Pulao": ["rice", "mixed vegetables", "spices"],
        "Hyderabadi Biryani": ["basmati rice", "meat", "spices"],
        "Chicken Biryani": ["rice", "chicken", "spices"],
        "Egg Curry": ["eggs", "onions", "tomatoes", "spices"],
        "Fish Curry": ["fish", "coconut milk", "spices"],
        "Palak Paneer": ["paneer", "spinach", "cream", "spices"]
    },
    "Salads & Sides": {
        "Curd Rice": ["cooked rice", "yogurt", "mustard seeds", "curry leaves"],
        "Raita": ["yogurt", "vegetables", "spices"],
        "Koshimbir": ["cucumber", "carrot", "spices"],
        "Beetroot Salad": ["beetroot", "yogurt", "spices"],
        "Cabbage Salad": ["cabbage", "carrot", "dressing"],
        "Carrot Salad": ["carrots", "lemon", "salt"],
        "Tomato Onion Salad": ["tomatoes", "onions", "coriander"],
        "Chickpea Salad": ["chickpeas", "onions", "spices"],
        "Vegetable Raita": ["yogurt", "mixed vegetables", "spices"],
        "Potato Salad": ["potatoes", "mayonnaise", "spices"]
    },
    "Breads": {
        "Chapati": ["whole wheat flour", "water", "salt"],
        "Naan": ["all-purpose flour", "yeast", "yogurt"],
        "Parotta": ["flour", "ghee", "water"],
        "Roti": ["whole wheat flour", "water"],
        "Appam": ["rice flour", "coconut milk"],
        "Bhakri": ["jowar flour", "water"],
        "Puri": ["flour", "water", "salt"],
        "Missi Roti": ["besan", "whole wheat flour", "spices"],
        "Garlic Naan": ["all-purpose flour", "garlic", "yogurt"],
        "Malabar Paratha": ["flour", "ghee", "water"]
    },
    "Desserts": {
        "Gulab Jamun": ["milk powder", "flour", "sugar", "ghee"],
        "Rasgulla": ["chhena", "sugar", "water"],
        "Kheer": ["rice", "milk", "sugar", "cardamom"],
        "Payasam": ["vermicelli", "milk", "sugar", "cardamom"],
        "Coconut Burfi": ["coconut", "sugar", "milk"],
        "Ladoo": ["besan", "sugar", "ghee"],
        "Halwa": ["semolina", "sugar", "ghee", "nuts"],
        "Mysore Pak": ["gram flour", "ghee", "sugar"],
        "Sooji Halwa": ["semolina", "sugar", "ghee"],
        "Rawa Kesari": ["semolina", "sugar", "ghee", "saffron"]
    },
    "Beverages": {
        "Masala Chai": ["tea leaves", "spices", "milk", "sugar"],
        "Filter Coffee": ["coffee powder", "water", "milk", "sugar"],
        "Buttermilk": ["yogurt", "water", "spices"],
        "Mango Lassi": ["mango", "yogurt", "sugar"],
        "Coconut Water": ["coconut"],
        "Lemonade": ["lemon", "water", "sugar"],
        "Sweet Lime Juice": ["sweet lime", "water", "sugar"],
        "Nannari Syrup": ["nannari", "water", "sugar"],
        "Jaljeera": ["cumin", "water", "spices"],
        "Neer Mor": ["buttermilk", "ginger", "spices"]
    },
    "Regional Specialties": {
        "Puttu": ["rice flour", "coconut", "water"],
        "Appam": ["rice flour", "coconut milk", "yeast"],
        "Dhokla": ["besan", "yogurt", "spices"],
        "Thepla": ["whole wheat flour", "spices", "yogurt"],
        "Khandvi": ["gram flour", "yogurt", "spices"],
        "Pongal": ["rice", "moong dal", "spices"],
        "Akki Roti": ["rice flour", "onions", "spices"],
        "Ragi Mudde": ["ragi flour", "water"],
        "Ambadi Bhaji": ["ambadi leaves", "spices"],
        "Misal Pav": ["mixed sprouts", "pav", "spices"]
    },
    "Miscellaneous": {
        "Vegetable Stir Fry": ["mixed vegetables", "soy sauce", "spices"],
        "Garlic Bread": ["bread", "garlic", "butter"],
        "Spinach Quiche": ["spinach", "eggs", "cheese", "crust"],
        "Bruschetta": ["bread", "tomatoes", "basil", "olive oil"],
        "Vegetable Fried Rice": ["rice", "mixed vegetables", "soy sauce"],
        "Paneer Tikka": ["paneer", "spices", "yogurt"],
        "Stuffed Bell Peppers": ["bell peppers", "rice", "spices"],
        "Thai Green Curry": ["coconut milk", "green curry paste", "vegetables"],
        "Stuffed Zucchini": ["zucchini", "cheese", "spices"],
        "Zucchini Noodles": ["zucchini", "olive oil", "spices"]
    }
}

# Set the title and layout
st.set_page_config(page_title="AI Ingredients Generator", layout="wide")
st.title("✨ AI Ingredients Generator ✨")

# Sidebar for navigation
st.sidebar.header("Recipe Categories")
categories = list(recipes.keys())
selected_category = st.sidebar.selectbox("Choose a category", categories)

# Display selected category recipes
st.subheader(f"Recipes in {selected_category}")
for recipe in recipes[selected_category]:
    st.write(f"🔹 {recipe}")

# User input for recipe name
st.markdown("<h2 style='text-align: center;'>Enter a Recipe Name:</h2>", unsafe_allow_html=True)
recipe_name = st.text_input("Recipe name:")

if recipe_name:
    recipe_name_lower = recipe_name.strip().lower()
    found = False

    # Logic to find ingredients for the entered recipe name
    for category, dishes in recipes.items():
        for dish in dishes:
            if dish.lower() == recipe_name_lower:  # Case insensitive comparison
                st.markdown(f"<h3 style='text-align: center;'>Ingredients for {dish}:</h3>", unsafe_allow_html=True)
                st.write(", ".join(dishes[dish]))
                found = True
                break
        if found:
            break

    if not found:
        st.markdown("<h3 style='text-align: center; color: red;'>Recipe not found.</h3>", unsafe_allow_html=True)

# Footer
st.markdown("<footer style='text-align: center;'>Made with ❤️ by Gokul Nath</footer>", unsafe_allow_html=True)

# Additional styling
st.markdown("""
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f9f9f9;
        color: #333;
    }
    .stTextInput {
        margin: auto;
        text-align: center;
    }
    footer {
        margin-top: 50px;
        font-size: 12px;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)
