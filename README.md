# 🏙️ Jacksonville Apartment Price Analysis

This project analyzes apartment rental data in Jacksonville, Florida to explore spatial, economic, and social patterns affecting rent prices. Using clustering, geospatial analysis, and predictive modeling, it identifies rental trends and evaluates affordability against local income data.

---

## 📌 Objectives

- Analyze apartment rental patterns using spatial and tabular data
- Predict apartment rental prices based on features like location, square footage, beds, and baths
- Identify neighborhoods using clustering algorithms
- Assess rental affordability compared to local income levels
- Explore relationships between rent pricing and crime density

---

## 📊 Key Features

- **K-Means Clustering** to define informal neighborhoods from apartment locations
- **Price Prediction Models** including Random Forest Regressors
- **Geospatial Visualization** with KDE plots and folium maps
- **Affordability Analysis** comparing median rents to local income thresholds
- **Data Cleaning & Feature Engineering** to prepare raw scraped data for modeling

---

---

## 🧪 Tools & Libraries

- **Python** (pandas, numpy, scikit-learn)
- **Geospatial**: seaborn, folium, geopandas, plotly
- **ML**: scikit-learn (RandomForestRegressor, KMeans)
- **EDA & Viz**: matplotlib, seaborn, plotly
- **Notebook Environment**: Jupyter

---

## 📈 Results Summary

- Random Forest achieved the best performance in predicting rent prices
- Certain "hot zones" of high rent were identified despite moderate square footage
- Many apartments were found to be unaffordable given average local income
- Crime density showed slight correlation with lower rental prices in specific clusters

---

## 🔐 Data Note

> **Disclaimer**: Data used in this project was collected from publicly available apartment rental sources and has been anonymized where appropriate. No private user data is included.

---

## ✨ Future Improvements

- Incorporate temporal data to model rent trends over time
- Integrate transit accessibility and school zone ratings
- Use XGBoost or LightGBM for enhanced performance
- Create an interactive dashboard for rent and crime overlay maps

---
