# Satellite Imagery–Based Property Valuation

A multimodal machine learning project that predicts property prices by combining **tabular real estate features** with **satellite imagery**. The system evaluates whether visual environmental context adds value beyond strong structured data, and provides **model explainability** using Grad-CAM.

---

## 🔍 Project Overview

Traditional property valuation models rely on structured attributes such as size, quality, and location. This project extends that approach by integrating **satellite images** to capture neighborhood-level cues like greenery, road density, and proximity to water.

The pipeline includes:
- A **tabular MLP baseline** for high-accuracy prediction
- A **CNN-based image encoder** for satellite imagery
- A **multimodal fusion model** for joint learning
- **Grad-CAM** for visual explainability

---

## 📁 Repository Structure

```
IIT_Roorkee_Project/
│
├── data/
│   ├── X_train.csv
│   ├── X_val.csv
│   ├── y_train.csv
│   ├── y_val.csv
│   ├── image_ids.csv
│   ├── train.xlsx
│   ├── test.xlsx
│   ├── test_processed.csv
│   ├── mlp_tabular_baseline.pth
│   ├── mlp_tabular_shallow.pth
│   ├── multimodal_fusion_model.pth
│   ├── tabular_scaler.pkl
│   └── tabular_scaler_shallow.pkl
│
├── notebooks/
│   ├── 01_preprocessing_EDA.ipynb
│   ├── 02_tabular_mlp_baseline.ipynb
│   ├── 02a_tabular_mlp_shallow.ipynb
│   ├── 03_image_embeddings.ipynb
│   ├── 04_multimodal_model.ipynb
│   ├── 04b_multimodal_shallow_fusion.ipynb
│   ├── 05_explainability_gradcam.ipynb
│   └── 06_prediction_csv.ipynb
|
├── 23118067_final.csv
├── 23118067_report.pdf
├── README.md
├── data_fetcher.py
└── satellite_images/
   └── https://drive.google.com/drive/folders/1YM3P6C1Ai8Vw9GnNHpldONYOKTXwRLBh
       
      

```

---

## 🧠 Models Used

### 1️⃣ Tabular MLP (Baseline & Production Model)
- Input: Structured numerical features only (no `id`)
- Architecture: Fully connected neural network with BatchNorm & Dropout
- Performance (Validation):
  - **R² ≈ 0.87**
- Used for **final prediction CSV**

### 2️⃣ Multimodal Model (Analysis & Explainability)
- Inputs:
  - Tabular features
  - Satellite image embeddings (ResNet18)
- Performance (Validation):
  - **R² ≈ 0.83**
- Used for:
  - Grad-CAM visualizations
  - Environmental insight analysis

---

## 🛰️ Satellite Image Processing

- Images fetched using latitude and longitude
- Preprocessing:
  - Resize to 224×224
  - ImageNet normalization
- Feature extraction:
  - Pretrained **ResNet18** (weights frozen)
  - 512-dimensional embeddings per property

---

## 🔎 Explainability (Grad-CAM)

Grad-CAM is applied to the CNN backbone to visualize which regions of the satellite images influence the model.

Observed focus areas include:
- Road networks
- Green cover
- Urban density
- Water bodies

This satisfies the explainability requirement even when accuracy gains are limited.

---

## ▶️ How to Run the Project

### Step 1: Preprocessing & EDA
```
Run: notebooks/01_preprocessing_EDA.ipynb
```
- Cleans data
- Handles missing values
- Saves train/validation CSVs

### Step 2: Train Tabular Baseline
```
Run: notebooks/02_tabular_mlp_baseline.ipynb
```
- Drops `id`
- Fits scaler
- Trains MLP
- Saves model and scaler

### Step 3: Extract Image Embeddings (GPU Required)
```
Run: notebooks/03_image_embeddings.ipynb
```
- Uses ResNet18
- Saves embeddings

### Step 4: Multimodal Fusion (GPU Required)
```
Run: notebooks/04_multimodal_fusion.ipynb
```
- Aligns data by `id`
- Trains multimodal model

### Step 5: Grad-CAM Explainability
```
Run: notebooks/05_gradcam_explainability.ipynb
```
- Generates visual explanations

### Step 6: Generate Prediction CSV
```
Run: notebooks/06_prediction_csv.ipynb
```
- Uses tabular MLP
- Outputs `predictions.csv`

---

## 📤 Output

- **predictions.csv**
  ```
  id, predicted_price
  ```
- **report.pdf**: Detailed methodology, results, and analysis

---

## 🧪 Key Findings

- Tabular features already capture most price-determining factors
- Satellite imagery does **not significantly improve accuracy**
- Imagery provides **valuable interpretability** via Grad-CAM

This reflects real-world ML systems where explainability and transparency are as important as raw performance.

---

## 📌 Notes

- GPU (T4) is required for CNN and Grad-CAM notebooks
- CPU is sufficient for preprocessing and tabular models
- The `id` column is used **only for alignment**, never as a feature

---

## 📄 License

This project is for academic and educational use.

---

**Author:** Ritesh
**Institution:** IIT Roorkee

