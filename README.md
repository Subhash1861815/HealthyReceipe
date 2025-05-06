# HealthyRecipe App 🍽️ | GenAI + Streamlit + Google Gemini

A smart, AI-powered application that suggests healthy recipes based on the ingredients you have—just by uploading a photo.

## 📌 Overview

The **HealthyRecipe App** is a personal project built using **Streamlit** and **Google Gemini API**. It enables users to upload an image of their available ingredients, and in response, it suggests a healthy recipe complete with step-by-step cooking instructions.

This project was inspired by the everyday challenges faced by students and busy individuals who may lack time, resources, or cooking experience. By leveraging generative AI, the app provides accessible, quick, and nutritious meal suggestions tailored to what the user already has on hand.

## 🎯 Features

- 🖼️ **Image Upload**: Accepts an image of ingredients from the user's kitchen.
- 🧠 **AI Recipe Generation**: Uses the Google Gemini API to identify ingredients and generate a healthy recipe.
- 📋 **Step-by-Step Instructions**: Clear, easy-to-follow directions ideal for beginners.
- ⚡ **Fast & Simple UI**: Built using Streamlit for a responsive, interactive experience.

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **AI Integration**: Google Gemini API (Image + Text)
- **Programming Language**: Python 3.x

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A Google Gemini API key

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Subhash1861815/HealthyReceipe.git
   cd HealthyReceipe

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate #activate on MacOS/Linux
   venv\Scripts\activate #windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the App**
   ```bash
   streamlit run app.py

## 🔐 Set Up Environment Variables (API Key)

Create a `.env` file in the root directory and add your Gemini API key:

```ini
GEMINI_API_KEY=your_google_gemini_api_key_here



## 📜 License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software, provided that the original copyright and license
notice are included in all copies or substantial portions of the software.

