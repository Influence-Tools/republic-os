---
type: Jurisdiction
title: "Kinney County, TX"
classification: county
fips: "48271"
state: "TX"
demographics:
  population: 3157
  population_under_18: 230
  population_18_64: 2091
  population_65_plus: 836
  median_household_income: 70000
  poverty_rate: 8.39
  homeownership_rate: 83.94
  unemployment_rate: 0.93
  median_home_value: 82000
  gini_index: 0.3618
  vacancy_rate: 22.27
  race_white: 1993
  race_black: 2
  race_asian: 0
  race_native: 65
  hispanic: 1814
  bachelors_plus: 344
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/74"
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

# Kinney County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3157 |
| Under 18 | 230 |
| 18–64 | 2091 |
| 65+ | 836 |
| Median household income | 70000 |
| Poverty rate | 8.39 |
| Homeownership rate | 83.94 |
| Unemployment rate | 0.93 |
| Median home value | 82000 |
| Gini index | 0.3618 |
| Vacancy rate | 22.27 |
| White | 1993 |
| Black | 2 |
| Asian | 0 |
| Native | 65 |
| Hispanic/Latino | 1814 |
| Bachelor's or higher | 344 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
