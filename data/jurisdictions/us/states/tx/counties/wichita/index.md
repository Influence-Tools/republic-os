---
type: Jurisdiction
title: "Wichita County, TX"
classification: county
fips: "48485"
state: "TX"
demographics:
  population: 129996
  population_under_18: 29645
  population_18_64: 80345
  population_65_plus: 20006
  median_household_income: 63524
  poverty_rate: 16.49
  homeownership_rate: 61.42
  unemployment_rate: 3.69
  median_home_value: 153700
  gini_index: 0.4629
  vacancy_rate: 12.08
  race_white: 92184
  race_black: 13745
  race_asian: 2976
  race_native: 947
  hispanic: 26848
  bachelors_plus: 28244
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.8524
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.1472
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Wichita County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 129996 |
| Under 18 | 29645 |
| 18–64 | 80345 |
| 65+ | 20006 |
| Median household income | 63524 |
| Poverty rate | 16.49 |
| Homeownership rate | 61.42 |
| Unemployment rate | 3.69 |
| Median home value | 153700 |
| Gini index | 0.4629 |
| Vacancy rate | 12.08 |
| White | 92184 |
| Black | 13745 |
| Asian | 2976 |
| Native | 947 |
| Hispanic/Latino | 26848 |
| Bachelor's or higher | 28244 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 85% (state senate)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 15% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
