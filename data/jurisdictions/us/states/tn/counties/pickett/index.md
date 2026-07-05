---
type: Jurisdiction
title: "Pickett County, TN"
classification: county
fips: "47137"
state: "TN"
demographics:
  population: 5079
  population_under_18: 878
  population_18_64: 2780
  population_65_plus: 1421
  median_household_income: 49030
  poverty_rate: 23.91
  homeownership_rate: 83.43
  unemployment_rate: 6.76
  median_home_value: 178500
  gini_index: 0.4606
  vacancy_rate: 35.51
  race_white: 4837
  race_black: 7
  race_asian: 0
  race_native: 5
  hispanic: 106
  bachelors_plus: 993
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/house/38"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Pickett County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5079 |
| Under 18 | 878 |
| 18–64 | 2780 |
| 65+ | 1421 |
| Median household income | 49030 |
| Poverty rate | 23.91 |
| Homeownership rate | 83.43 |
| Unemployment rate | 6.76 |
| Median home value | 178500 |
| Gini index | 0.4606 |
| Vacancy rate | 35.51 |
| White | 4837 |
| Black | 7 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 106 |
| Bachelor's or higher | 993 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 38](/us/states/tn/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
