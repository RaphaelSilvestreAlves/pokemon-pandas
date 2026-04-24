<h1 align="center">Pokémon Gen 1 Data Pipeline with Python, Pandas and SQLite</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Requests-2A2A2A?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/PokeAPI-EF5350?style=for-the-badge&logoColor=white">
</p>

<p align="center">
  Data collection, transformation and persistence project using the first 151 Pokémon from PokeAPI.
</p>

---

## Overview

This project was built to practice a complete mini data workflow in Python:

- consuming external API data;
- handling nested JSON structures;
- transforming raw data into a structured pandas DataFrame;
- creating derived analytical fields;
- persisting the final dataset into a local SQLite database;
- querying the database with SQL and reading results back with pandas.

The dataset is based on the **first 151 Pokémon from Generation 1**, making the project both fun and technically useful for practicing real data handling concepts.

---

## Features

- Fetches the first 151 Pokémon from PokeAPI
- Requests detailed data for each Pokémon
- Extracts and structures relevant attributes
- Creates a pandas DataFrame for analysis
- Calculates `total_stats` for each Pokémon
- Saves the final dataset into a SQLite database
- Executes SQL queries for ranking and analysis

---

## Tech Stack

- **Python**
- **Pandas**
- **Requests**
- **SQLite**
- **PokeAPI**

---

## Data Model

Each Pokémon record contains the following fields:

- `id`
- `name`
- `height`
- `weight`
- `first_type`
- `second_type`
- `hp`
- `attack`
- `defense`
- `special_attack`
- `special_defense`
- `speed`
- `total_stats`

---

## Project Structure

```bash
pokemon_pandas/
├── pokemon_gen1_analysis.py
├── pokemon_gen1.db
└── README.md
