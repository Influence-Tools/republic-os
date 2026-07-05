---
type: Jurisdiction
title: "Las Animas County, CO"
classification: county
fips: "08071"
state: "CO"
demographics:
  population: 14413
  population_under_18: 2592
  population_18_64: 8070
  population_65_plus: 3751
  median_household_income: 52074
  poverty_rate: 18.71
  homeownership_rate: 68.57
  unemployment_rate: 5.64
  median_home_value: 237600
  gini_index: 0.4528
  vacancy_rate: 20.28
  race_white: 9922
  race_black: 247
  race_asian: 195
  race_native: 624
  hispanic: 5587
  bachelors_plus: 2665
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Las Animas County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14413 |
| Under 18 | 2592 |
| 18–64 | 8070 |
| 65+ | 3751 |
| Median household income | 52074 |
| Poverty rate | 18.71 |
| Homeownership rate | 68.57 |
| Unemployment rate | 5.64 |
| Median home value | 237600 |
| Gini index | 0.4528 |
| Vacancy rate | 20.28 |
| White | 9922 |
| Black | 247 |
| Asian | 195 |
| Native | 624 |
| Hispanic/Latino | 5587 |
| Bachelor's or higher | 2665 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
