---
type: Jurisdiction
title: "Guthrie County, IA"
classification: county
fips: "19077"
state: "IA"
demographics:
  population: 10688
  population_under_18: 2269
  population_18_64: 5828
  population_65_plus: 2591
  median_household_income: 77711
  poverty_rate: 9.88
  homeownership_rate: 84.0
  unemployment_rate: 3.22
  median_home_value: 180100
  gini_index: 0.4336
  vacancy_rate: 20.8
  race_white: 9931
  race_black: 60
  race_asian: 50
  race_native: 15
  hispanic: 331
  bachelors_plus: 2555
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Guthrie County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10688 |
| Under 18 | 2269 |
| 18–64 | 5828 |
| 65+ | 2591 |
| Median household income | 77711 |
| Poverty rate | 9.88 |
| Homeownership rate | 84.0 |
| Unemployment rate | 3.22 |
| Median home value | 180100 |
| Gini index | 0.4336 |
| Vacancy rate | 20.8 |
| White | 9931 |
| Black | 60 |
| Asian | 50 |
| Native | 15 |
| Hispanic/Latino | 331 |
| Bachelor's or higher | 2555 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 24](/us/states/ia/districts/senate/24.md) — 100% (state senate)
- [IA House District 47](/us/states/ia/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
