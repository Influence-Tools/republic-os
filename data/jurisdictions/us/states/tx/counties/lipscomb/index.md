---
type: Jurisdiction
title: "Lipscomb County, TX"
classification: county
fips: "48295"
state: "TX"
demographics:
  population: 2918
  population_under_18: 900
  population_18_64: 1476
  population_65_plus: 542
  median_household_income: 72560
  poverty_rate: 11.46
  homeownership_rate: 82.44
  unemployment_rate: 6.5
  median_home_value: 124300
  gini_index: 0.45
  vacancy_rate: 28.42
  race_white: 2069
  race_black: 1
  race_asian: 0
  race_native: 7
  hispanic: 1127
  bachelors_plus: 475
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/87"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lipscomb County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2918 |
| Under 18 | 900 |
| 18–64 | 1476 |
| 65+ | 542 |
| Median household income | 72560 |
| Poverty rate | 11.46 |
| Homeownership rate | 82.44 |
| Unemployment rate | 6.5 |
| Median home value | 124300 |
| Gini index | 0.45 |
| Vacancy rate | 28.42 |
| White | 2069 |
| Black | 1 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 1127 |
| Bachelor's or higher | 475 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
