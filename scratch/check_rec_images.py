import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\tours"

img1 = os.path.join(base_dir, "images", "2-days-mount-toubkal")
img2 = os.path.join(base_dir, "images", "3days-merzouga-desert")
img3 = os.path.join(base_dir, "images", "2days-azzaden-valley")

print("Toubkal images:", os.listdir(img1) if os.path.exists(img1) else "NOT FOUND")
print("Merzouga images:", os.listdir(img2) if os.path.exists(img2) else "NOT FOUND")
print("Azzaden images:", os.listdir(img3) if os.path.exists(img3) else "NOT FOUND")
