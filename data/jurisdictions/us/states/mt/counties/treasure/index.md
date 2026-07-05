---
type: Jurisdiction
title: "Treasure County, MT"
classification: county
fips: "30103"
state: "MT"
demographics:
  population: 732
  population_under_18: 128
  population_18_64: 437
  population_65_plus: 167
  median_household_income: 67917
  poverty_rate: 12.3
  homeownership_rate: 68.33
  unemployment_rate: 1.01
  median_home_value: 230300
  gini_index: 0.4988
  vacancy_rate: 21.74
  race_white: 686
  race_black: 0
  race_asian: 7
  race_native: 1
  hispanic: 38
  bachelors_plus: 248
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/house/35"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Treasure County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 732 |
| Under 18 | 128 |
| 18–64 | 437 |
| 65+ | 167 |
| Median household income | 67917 |
| Poverty rate | 12.3 |
| Homeownership rate | 68.33 |
| Unemployment rate | 1.01 |
| Median home value | 230300 |
| Gini index | 0.4988 |
| Vacancy rate | 21.74 |
| White | 686 |
| Black | 0 |
| Asian | 7 |
| Native | 1 |
| Hispanic/Latino | 38 |
| Bachelor's or higher | 248 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 18](/us/states/mt/districts/senate/18.md) — 100% (state senate)
- [MT House District 35](/us/states/mt/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
