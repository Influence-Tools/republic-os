---
type: Jurisdiction
title: "Putnam County, TN"
classification: county
fips: "47141"
state: "TN"
demographics:
  population: 82558
  population_under_18: 17224
  population_18_64: 51711
  population_65_plus: 13623
  median_household_income: 58912
  poverty_rate: 18.37
  homeownership_rate: 61.19
  unemployment_rate: 3.73
  median_home_value: 282500
  gini_index: 0.4614
  vacancy_rate: 7.96
  race_white: 71624
  race_black: 2008
  race_asian: 947
  race_native: 213
  hispanic: 6928
  bachelors_plus: 22031
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/42"
    rel: in-district
    area_weight: 0.6689
  - to: "us/states/tn/districts/house/25"
    rel: in-district
    area_weight: 0.3305
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Putnam County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82558 |
| Under 18 | 17224 |
| 18–64 | 51711 |
| 65+ | 13623 |
| Median household income | 58912 |
| Poverty rate | 18.37 |
| Homeownership rate | 61.19 |
| Unemployment rate | 3.73 |
| Median home value | 282500 |
| Gini index | 0.4614 |
| Vacancy rate | 7.96 |
| White | 71624 |
| Black | 2008 |
| Asian | 947 |
| Native | 213 |
| Hispanic/Latino | 6928 |
| Bachelor's or higher | 22031 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 42](/us/states/tn/districts/house/42.md) — 67% (state house)
- [TN House District 25](/us/states/tn/districts/house/25.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
