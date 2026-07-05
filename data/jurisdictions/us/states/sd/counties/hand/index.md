---
type: Jurisdiction
title: "Hand County, SD"
classification: county
fips: "46059"
state: "SD"
demographics:
  population: 3140
  population_under_18: 794
  population_18_64: 1587
  population_65_plus: 759
  median_household_income: 74635
  poverty_rate: 5.15
  homeownership_rate: 65.48
  unemployment_rate: 0.78
  median_home_value: 159300
  gini_index: 0.4713
  vacancy_rate: 18.27
  race_white: 2899
  race_black: 15
  race_asian: 3
  race_native: 45
  hispanic: 65
  bachelors_plus: 728
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Hand County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3140 |
| Under 18 | 794 |
| 18–64 | 1587 |
| 65+ | 759 |
| Median household income | 74635 |
| Poverty rate | 5.15 |
| Homeownership rate | 65.48 |
| Unemployment rate | 0.78 |
| Median home value | 159300 |
| Gini index | 0.4713 |
| Vacancy rate | 18.27 |
| White | 2899 |
| Black | 15 |
| Asian | 3 |
| Native | 45 |
| Hispanic/Latino | 65 |
| Bachelor's or higher | 728 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
