---
type: Jurisdiction
title: "Wilkinson County, MS"
classification: county
fips: "28157"
state: "MS"
demographics:
  population: 8162
  population_under_18: 1640
  population_18_64: 4917
  population_65_plus: 1605
  median_household_income: 35311
  poverty_rate: 27.45
  homeownership_rate: 78.4
  unemployment_rate: 13.37
  median_home_value: 90000
  gini_index: 0.5158
  vacancy_rate: 30.88
  race_white: 2322
  race_black: 5482
  race_asian: 0
  race_native: 0
  hispanic: 67
  bachelors_plus: 694
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/38"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/house/96"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Wilkinson County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8162 |
| Under 18 | 1640 |
| 18–64 | 4917 |
| 65+ | 1605 |
| Median household income | 35311 |
| Poverty rate | 27.45 |
| Homeownership rate | 78.4 |
| Unemployment rate | 13.37 |
| Median home value | 90000 |
| Gini index | 0.5158 |
| Vacancy rate | 30.88 |
| White | 2322 |
| Black | 5482 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 67 |
| Bachelor's or higher | 694 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 38](/us/states/ms/districts/senate/38.md) — 100% (state senate)
- [MS House District 96](/us/states/ms/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
