---
type: Jurisdiction
title: "La Salle County, TX"
classification: county
fips: "48283"
state: "TX"
demographics:
  population: 6839
  population_under_18: 1501
  population_18_64: 4241
  population_65_plus: 1097
  median_household_income: 57716
  poverty_rate: 21.45
  homeownership_rate: 76.02
  unemployment_rate: 1.82
  median_home_value: 97800
  gini_index: 0.4083
  vacancy_rate: 27.48
  race_white: 2277
  race_black: 400
  race_asian: 6
  race_native: 36
  hispanic: 4910
  bachelors_plus: 747
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# La Salle County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6839 |
| Under 18 | 1501 |
| 18–64 | 4241 |
| 65+ | 1097 |
| Median household income | 57716 |
| Poverty rate | 21.45 |
| Homeownership rate | 76.02 |
| Unemployment rate | 1.82 |
| Median home value | 97800 |
| Gini index | 0.4083 |
| Vacancy rate | 27.48 |
| White | 2277 |
| Black | 400 |
| Asian | 6 |
| Native | 36 |
| Hispanic/Latino | 4910 |
| Bachelor's or higher | 747 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
