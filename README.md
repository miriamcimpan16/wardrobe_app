# 🧥 Your AI Wardrobe Assistant

A desktop application built with Python and `tkinter` that helps you organize your digital closet, filter clothes by weather and style, and randomly generate complete outfits instantly!

---

## 🌟 Features

*   **Welcome Guide:** Clear instructions on how to structure and name your clothing image files.
*   **Dynamic Filtering:** Filter clothing items by **Weather** (`warm`, `cold`, `rainy`) and **Style** (`casual`, `elegant`, `sport`), or leave them on **"Any"**.
*   **Smart Fallback System:** If no exact matches are found for a specific filter, the app automatically falls back to random selection so your outfit generation never breaks.
*   **Visual Preview:** Displays resized images and filenames for your generated Top, Bottom, and Shoes combination.
*   **Custom Background Support:** Automatically loads a custom background (`background.jpg`) if available.

---

## 📂 File Naming Convention

To ensure the app correctly categorizes your clothes, name your image files using English keywords separated by underscores (`_`):

1.  **Tops:** `top`, `tshirt`, `shirt`, `jacket`, `hoodie`, `blouse`, `sweater`
2.  **Bottoms:** `pants`, `jeans`, `skirt`, `trousers`, `shorts`, `tights`
3.  **Shoes:** `shoes`, `sneakers`, `boots`, `slippers`, `heels`
4.  **Tags (Optional):** `warm`, `cold`, `rainy`, `casual`, `elegant`, `sport`

> **Example:** `tshirt_casual_warm.jpg`

---

## ⚙️ Prerequisites & Installation

Make sure you have Python installed along with the required libraries.

1.  **Clone or download** this project into your workspace (e.g., PyCharm).
2.  **Install Pillow** (Python Imaging Library) if you haven't already by running this command in your terminal/command prompt:
    ```bash
    pip install Pillow
    ```

---

## 🚀 How to Run the App

1.  Open the project in **PyCharm** (or any Python IDE/terminal).
2.  Run the main script:
    ```bash
    python your_script_name.py
    ```
3.  Read the welcome guide and click **"Got it! Let's Start"**.
4.  Click **"Select folder with pictures"** and choose the folder where your clothing images are saved.
5.  Choose your desired **Weather** and **Style**, then click **"Generate outfit"**!

---

## 🛠️ Built With

*   **Python** - Core programming language
*   **Tkinter** - GUI (Graphical User Interface) framework
*   **Pillow (PIL)** - Image processing and resizing

<img width="651" height="631" alt="image" src="https://github.com/user-attachments/assets/797f700f-cdb0-4fa6-ad4b-593ea644a51e" />


<img width="816" height="977" alt="image" src="https://github.com/user-attachments/assets/4092564a-0699-4ebc-bf74-a4fad2a1175e" />

<img width="817" height="972" alt="image" src="https://github.com/user-attachments/assets/a3d2e238-05a3-44d6-87fa-cd36fae8ac39" />

