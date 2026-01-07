# -*- coding: utf-8 -*-
"""data_fetcher.ipynb


Original file is located at
    https://colab.research.google.com/drive/1s7h2tDpQPwXVEbHjeAeMiqNIELhRqWlg

DATA FETCHER (MAPBOX SATELLITE DOWNLOADER)
"""

import os
import pandas as pd
import requests
import time
from tqdm.notebook import tqdm
from google.colab import drive

# 1. Mount Google Drive
drive.mount('/content/drive')

# --- CONFIGURATION ---
MAPBOX_KEY = "pk.eyJ1Ijoicml0ZXNoaWl0ciIsImEiOiJjbWp6bjYydWI2YjZkM2ZzNWRnZWZ4bzRmIn0.6Jh2ozJzSwCr-I3jihYI0w"
PROJECT_PATH = "/content/drive/MyDrive/IIT_Roorkee_Project"
SAVE_DIR = os.path.join(PROJECT_PATH, "images") # All images go here

# Mapbox Settings
ZOOM_LEVEL = 18
IMAGE_SIZE = "600x600"
STYLE_ID = "mapbox/satellite-v9"

# 2. Setup Single Directory
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
    print(f"📂 Created Unified Directory: {SAVE_DIR}")
else:
    print(f"📂 Target Directory: {SAVE_DIR}")

# 3. Load & Combine Data
print("📄 Loading Train & Test files...")
try:
    df_train = pd.read_excel(os.path.join(PROJECT_PATH, "train.xlsx"))
    df_test = pd.read_excel(os.path.join(PROJECT_PATH, "test.xlsx"))

    # Select only what we need
    df_train = df_train[['id', 'lat', 'long']]
    df_test = df_test[['id', 'lat', 'long']]

    # Combine into one big list
    df_all = pd.concat([df_train, df_test], ignore_index=True)

    # Remove duplicates (just in case an ID appears in both)
    df_all = df_all.drop_duplicates(subset=['id'])

    print(f"✅ Ready to process: {len(df_all)} unique properties.")

except Exception as e:
    print(f"❌ Error loading files: {e}")
    df_all = pd.DataFrame()

# 4. Download Function
def download_images(df):
    if df.empty: return

    success_count = 0
    skip_count = 0
    error_count = 0

    # Iterate with a progress bar
    for index, row in tqdm(df.iterrows(), total=len(df), desc="Downloading to 'images/'"):

        # Clean ID to ensure safe filename
        img_id = str(row['id']).replace('.0', '').strip()
        lat = row['lat']
        lon = row['long']

        file_name = f"{img_id}.jpg"
        save_path = os.path.join(SAVE_DIR, file_name)

        # SKIP if file already exists in the folder
        if os.path.exists(save_path):
            skip_count += 1
            continue

        url = f"https://api.mapbox.com/styles/v1/{STYLE_ID}/static/{lon},{lat},{ZOOM_LEVEL}/{IMAGE_SIZE}?access_token={MAPBOX_KEY}"

        try:
            response = requests.get(url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                success_count += 1
            else:
                error_count += 1
        except:
            error_count += 1

    print(f"\n✅ Finished! All images are in: {SAVE_DIR}")
    print(f"📥 New Downloads: {success_count}")
    print(f"⏭️ Skipped (Already there): {skip_count}")

# 5. Run it
download_images(df_all)
