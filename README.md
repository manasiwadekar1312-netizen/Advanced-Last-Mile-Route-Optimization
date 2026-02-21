# 🚚 Advanced Last-Mile Route Optimization System

### Traffic-Aware Delivery Planning using OR-Tools

---

## 📌 Project Overview

The Advanced Last-Mile Route Optimization System is a Data Science & Analytics project designed to improve delivery efficiency using combinatorial optimization techniques.

This system calculates the most efficient delivery sequence using Google OR-Tools and generates interactive HTML map outputs that open directly in a web browser.

---

## 🎯 Objective

- Optimize delivery routes using advanced optimization algorithms
- Minimize travel distance and delivery time
- Simulate traffic impact on routes
- Generate multiple analytical outputs
- Provide browser-based interactive visualization

---

## ❗ Problem Statement

In real-world logistics operations:

- Poor route planning increases delivery delays
- Traffic congestion affects delivery efficiency
- Manual planning leads to higher fuel consumption
- Lack of visual comparison between normal and traffic-aware routes

This project solves these challenges using Vehicle Routing Problem (VRP) optimization techniques.

---

## 🛠️ Tools & Technologies Used

- Python  
- NumPy  
- Pandas  
- Folium  
- OR-Tools  

---

## ⚙️ Methodology

1. Load warehouse and delivery stop data  
2. Create distance matrix using NumPy  
3. Apply OR-Tools VRP algorithm  
4. Simulate traffic conditions (Low / Medium / High)  
5. Generate optimized route  
6. Export interactive HTML maps  

---

## 🗂️ Project Outputs

### 🟢 1. Normal Route Map

- Optimized route without traffic simulation  
- Saved as `.html` file  
- Opens automatically in web browser  

### 🔴 2. Traffic-Aware Route Map

- Route adjusted based on traffic levels  
- Color-coded visualization  
- Opens directly in web browser  

### 📄 3. Text Report

- Total distance covered  
- Delivery sequence order  
- Traffic impact comparison  
- Saved as `.txt` file  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

After execution, the generated HTML files will automatically open in your default web browser.

---

## ✨ Key Features

- Advanced VRP optimization  
- Traffic simulation logic  
- Multiple output generation  
- Interactive browser-based maps  
- Real-world logistics application  

---

## 🚀 Future Scope

- Real-time traffic API integration  
- Multi-vehicle optimization  
- Time-window delivery constraints  
- Web-based dashboard deployment  

---

## 📊 Internship Domain

Machine Learning with Python 
Year: 2026

