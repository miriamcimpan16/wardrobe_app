import os  # for folders and files
import random  # for choosing random clothes
import tkinter as tk  # for the visual window
from tkinter import filedialog  # window when I want to choose a folder
from PIL import Image, ImageTk  # opens a picture from the hard disk and resizes it


# NOTE: Clothing images in the folder must be named like "tshirt_casual_warm.jpg"

#1. WELCOME WINDOW
class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Your Wardrobe Assistant")
        self.root.geometry("520x470")
        self.root.resizable(False, False)

        lbl_title = tk.Label(root, text="Welcome to Your AI Outfit Assistant!", font=("Arial", 14, "bold"))
        lbl_title.pack(pady=15)

        rules_text = (
            "Before we start, please make sure your folder meets these rules:\n\n"
            "1. The folder must contain clothing images in format:\n"
            "   (.png, .jpg, .jpeg).\n\n"
            "2. Name your files in English so the app can recognize them:\n"
            "   • Tops: 'top', 'tshirt', 'shirt', 'jacket', 'hoodie', 'blouse'\n"
            "   • Bottoms: 'pants', 'jeans', 'skirt', 'trousers', 'shorts'\n"
            "   • Shoes: 'shoes', 'sneakers', 'boots', 'slippers'\n\n"
            "3. Optional tags for Weather & Style:\n"
            "   • Weather: 'warm', 'cold', 'rainy'\n"
            "   • Style: 'casual', 'elegant', 'sport'\n"
            "   (Example: tshirt_casual_warm.jpg)"
        )

        lbl_rules = tk.Label(root, text=rules_text, font=("Arial", 10), justify="left")
        lbl_rules.pack(pady=10, padx=20)

        btn_start = tk.Button(root, text="Got it! Let's Start", font=("Arial", 12, "bold"),
                              command=self.open_main_app, bg="black", fg="white", padx=10, pady=5)
        btn_start.pack(pady=15)

    def open_main_app(self):
        self.root.destroy()
        main_root = tk.Tk()
        app = AplicatieHaine(main_root)
        main_root.mainloop()


#2. MAIN APPLICATION
class AplicatieHaine:
    # Method with the buttons and labels of the application
    def __init__(self, root):
        self.root = root  # root is actually the window
        self.root.title("Your Wardrobe Assistant")
        self.root.geometry("650x750")  # window dimensions
        self.root.resizable(False, False)

        self.folderul_selectat = ""
        self.toate_pozele = []

        try:
            self.bg_img_raw = Image.open("background.jpg")
            self.bg_img_raw = self.bg_img_raw.resize((650, 750))
            self.bg_image_tk = ImageTk.PhotoImage(self.bg_img_raw)
            self.lbl_background = tk.Label(root, image=self.bg_image_tk)
            self.lbl_background.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Background image background.jpg not found, running without background", e)

        self.titlu = tk.Label(root, text="Welcome! Let's pick your outfit :)", font=("Arial", 16, "bold"), bg="#f4ecd8",
                              fg="black")
        self.titlu.pack(pady=10)  # paste the label onto the window

        # Folder button
        self.btn_folder = tk.Button(root, text="Select folder with pictures", font=("Arial", 14, "bold"),
                                    command=self.alege_folder, bg="black", fg="white")
        # when clicking the button it reaches the choice command (meaning the alege_folder method is executed)
        # bg->background fg->foreground (the text)
        self.btn_folder.pack(pady=5)

        # Selected folder info label
        self.lbl_folder_info = tk.Button(root, text="No folder selected", font=("Arial", 12, "bold"), fg="gray")
        self.lbl_folder_info.pack(pady=5)
        # if not selected, default text appears

        # SELECTION MENU
        self.cadru_optiuni = tk.Frame(root, bg="#f4ecd8")
        self.cadru_optiuni.pack(pady=5)

        self.lbl_vreme = tk.Label(self.cadru_optiuni, text="Weather:", font=("Arial", 10, "bold"), bg="#f4ecd8")
        self.lbl_vreme.grid(row=0, column=0, padx=5)
        self.vreme_var = tk.StringVar(root)
        self.vreme_var.set("Any")  # Default value
        self.meniu_vreme = tk.OptionMenu(self.cadru_optiuni, self.vreme_var, "Any", "warm", "cold", "rainy")
        self.meniu_vreme.config(bg="white", fg="black", font=("Arial", 9))
        self.meniu_vreme.grid(row=0, column=1, padx=5)

        # Style / Occasion
        self.lbl_stil = tk.Label(self.cadru_optiuni, text="Style:", font=("Arial", 10, "bold"), bg="#f4ecd8")
        self.lbl_stil.grid(row=0, column=2, padx=5)
        self.stil_var = tk.StringVar(root)
        self.stil_var.set("Any")
        self.meniu_stil = tk.OptionMenu(self.cadru_optiuni, self.stil_var, "Any", "casual", "elegant", "sport")
        self.meniu_stil.config(bg="white", fg="black", font=("Arial", 9))
        self.meniu_stil.grid(row=0, column=3, padx=5)

        # Generate outfit button
        self.btn_genereaza = tk.Button(root, text="Generate outfit", font=("Arial", 12, "bold"),
                                       command=self.genereaza_outfit, bg="beige", fg="black", state=tk.DISABLED)
        # disabled --> activates only when a folder has been chosen
        self.btn_genereaza.pack(pady=5)

        # Image display section
        self.cadru_imagini = tk.Frame(root, bg="#f4ecd8")
        self.cadru_imagini.pack(pady=10)
        # create a sort of table where we will place the outfit pieces

        self.lbl_sus = tk.Label(self.cadru_imagini, text="Top part", font=("Arial", 10, "bold"), bg="#f4ecd8")
        self.lbl_sus.grid(row=0, column=0, padx=10)

        # where we will put the image
        self.img_sus_label = tk.Label(self.cadru_imagini, bg="#f4ecd8")
        self.img_sus_label.grid(row=1, column=0, padx=10, pady=2)

        self.lbl_jos = tk.Label(self.cadru_imagini, text="Bottom part", font=("Arial", 10, "bold"), bg="#f4ecd8")
        self.lbl_jos.grid(row=2, column=0, padx=10)

        self.img_jos_label = tk.Label(self.cadru_imagini, bg="#f4ecd8")
        self.img_jos_label.grid(row=3, column=0, padx=10, pady=2)

        self.lbl_pantofi = tk.Label(self.cadru_imagini, text="Shoes", font=("Arial", 10, "bold"), bg="#f4ecd8")
        self.lbl_pantofi.grid(row=4, column=0, padx=10)

        self.img_pantofi_label = tk.Label(self.cadru_imagini, bg="#f4ecd8")
        self.img_pantofi_label.grid(row=5, column=0, padx=10, pady=2)

    def alege_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folderul_selectat = folder
            self.lbl_folder_info.config(text=f"Folder: {folder}", fg="black")
            fisiere = os.listdir(folder)
            self.toate_pozele = [f for f in fisiere if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if self.toate_pozele:
                self.btn_genereaza.config(state=tk.NORMAL)
                self.titlu.config(text=f"Found {len(self.toate_pozele)} pictures!")
            else:
                self.titlu.config(text="The folder is empty or has no pictures!")

    def genereaza_outfit(self):
        # To prevent the program from crashing if no folder is chosen
        if not self.toate_pozele:
            return

        vreme_selectata = self.vreme_var.get().lower()
        stil_selectat = self.stil_var.get().lower()

        haine_sus = []
        haine_jos = []
        incaltaminte = []

        # Keywords in English matching user rules
        cuvinte_sus = ['top', 'tshirt', 'shirt', 'jacket', 'hoodie', 'blouse', 'sweater']
        cuvinte_jos = ['pants', 'jeans', 'skirt', 'trousers', 'shorts', 'tights']
        cuvinte_pantofi = ['shoes', 'sneakers', 'boots', 'slippers', 'heels']

        # Step 1: Filter clothes based on user selection
        for p in self.toate_pozele:
            poza = p.lower()

            # If "Any" is selected, we don't filter by that criteria
            if vreme_selectata != "any" and vreme_selectata not in poza:
                continue
            if stil_selectat != "any" and stil_selectat not in poza:
                continue

            # Categorize the matching items
            if any(cuvant in poza for cuvant in cuvinte_sus):
                haine_sus.append(p)
            elif any(cuvant in poza for cuvant in cuvinte_jos):
                haine_jos.append(p)
            elif any(cuvant in poza for cuvant in cuvinte_pantofi):
                incaltaminte.append(p)

        # Step 2: Choose pieces. If a specific filter was used but no items matched,
        # we pick randomly from all items in that category and notify the user.

        # --- TOP PART ---
        all_possible_tops = [p for p in self.toate_pozele if any(c in p.lower() for c in cuvinte_sus)]
        if haine_sus:
            ales_sus = random.choice(haine_sus)
            mesaj_sus = f"Top: {ales_sus}"
        else:
            # Filter failed or empty, fallback to random and notify if a filter was active
            ales_sus = random.choice(all_possible_tops) if all_possible_tops else None
            if vreme_selectata != "any" or stil_selectat != "any":
                mesaj_sus = f"Top: {ales_sus} (Random - no filter match)"
            else:
                mesaj_sus = f"Top: {ales_sus}"

        # --- BOTTOM PART ---
        all_possible_bottoms = [p for p in self.toate_pozele if any(c in p.lower() for c in cuvinte_jos)]
        if haine_jos:
            ales_jos = random.choice(haine_jos)
            mesaj_jos = f"Bottom: {ales_jos}"
        else:
            ales_jos = random.choice(all_possible_bottoms) if all_possible_bottoms else None
            if vreme_selectata != "any" or stil_selectat != "any":
                mesaj_jos = f"Bottom: {ales_jos} (Random - no filter match)"
            else:
                mesaj_jos = f"Bottom: {ales_jos}"

        # --- SHOES ---
        all_possible_shoes = [p for p in self.toate_pozele if any(c in p.lower() for c in cuvinte_pantofi)]
        if incaltaminte:
            ales_incaltaminte = random.choice(incaltaminte)
            mesaj_pantofi = f"Shoes: {ales_incaltaminte}"
        else:
            ales_incaltaminte = random.choice(all_possible_shoes) if all_possible_shoes else None
            if vreme_selectata != "any" or stil_selectat != "any":
                mesaj_pantofi = f"Shoes: {ales_incaltaminte} (Random - no filter match)"
            else:
                mesaj_pantofi = f"Shoes: {ales_incaltaminte}"

        # Step 3: Send everything to be displayed in the interface
        if ales_sus:
            self.afiseaza_imagine(os.path.join(self.folderul_selectat, ales_sus), self.img_sus_label, self.lbl_sus,
                                  mesaj_sus)
        else:
            self.img_sus_label.config(image='')
            self.lbl_sus.config(text="No top clothing found in folder")

        if ales_jos:
            self.afiseaza_imagine(os.path.join(self.folderul_selectat, ales_jos), self.img_jos_label, self.lbl_jos,
                                  mesaj_jos)
        else:
            self.img_jos_label.config(image='')
            self.lbl_jos.config(text="No bottom clothing found in folder")

        if ales_incaltaminte:
            self.afiseaza_imagine(os.path.join(self.folderul_selectat, ales_incaltaminte), self.img_pantofi_label,
                                  self.lbl_pantofi, mesaj_pantofi)
        else:
            self.img_pantofi_label.config(image='')
            self.lbl_pantofi.config(text="No shoes found in folder")
    # The function that takes each image and resizes it
    def afiseaza_imagine(self, cale_fisier, widget_label, widget_text, text_eticheta):
        try:
            # to open the picture I use Pillow
            img = Image.open(cale_fisier)
            img = img.resize((110, 110))
            img_tk = ImageTk.PhotoImage(img)  # so tkinter can display it on screen

            widget_label.config(image=img_tk, bg="#f4ecd8")
            widget_label.image = img_tk
            widget_text.config(text=text_eticheta)
        except Exception as e:
            widget_text.config(text="Display error")


if __name__ == "__main__":
    welcome_root = tk.Tk()
    welcome_app = WelcomeWindow(welcome_root)
    welcome_root.mainloop()