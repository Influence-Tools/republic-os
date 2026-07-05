---
type: Jurisdiction
title: "Schuyler County, MO"
classification: county
fips: "29197"
state: "MO"
demographics:
  population: 4038
  population_under_18: 1111
  population_18_64: 2152
  population_65_plus: 775
  median_household_income: 61205
  poverty_rate: 8.56
  homeownership_rate: 79.88
  unemployment_rate: 3.75
  median_home_value: 137500
  gini_index: 0.3757
  vacancy_rate: 31.17
  race_white: 3833
  race_black: 8
  race_asian: 22
  race_native: 10
  hispanic: 29
  bachelors_plus: 429
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Schuyler County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4038 |
| Under 18 | 1111 |
| 18–64 | 2152 |
| 65+ | 775 |
| Median household income | 61205 |
| Poverty rate | 8.56 |
| Homeownership rate | 79.88 |
| Unemployment rate | 3.75 |
| Median home value | 137500 |
| Gini index | 0.3757 |
| Vacancy rate | 31.17 |
| White | 3833 |
| Black | 8 |
| Asian | 22 |
| Native | 10 |
| Hispanic/Latino | 29 |
| Bachelor's or higher | 429 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
