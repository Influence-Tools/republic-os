---
type: Jurisdiction
title: "Whitley County, IN"
classification: county
fips: "18183"
state: "IN"
demographics:
  population: 34618
  population_under_18: 7896
  population_18_64: 20080
  population_65_plus: 6642
  median_household_income: 78083
  poverty_rate: 9.92
  homeownership_rate: 81.84
  unemployment_rate: 3.28
  median_home_value: 219400
  gini_index: 0.3905
  vacancy_rate: 6.66
  race_white: 32025
  race_black: 56
  race_asian: 119
  race_native: 30
  hispanic: 964
  bachelors_plus: 7423
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/83"
    rel: in-district
    area_weight: 0.5354
  - to: "us/states/in/districts/house/18"
    rel: in-district
    area_weight: 0.4645
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Whitley County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34618 |
| Under 18 | 7896 |
| 18–64 | 20080 |
| 65+ | 6642 |
| Median household income | 78083 |
| Poverty rate | 9.92 |
| Homeownership rate | 81.84 |
| Unemployment rate | 3.28 |
| Median home value | 219400 |
| Gini index | 0.3905 |
| Vacancy rate | 6.66 |
| White | 32025 |
| Black | 56 |
| Asian | 119 |
| Native | 30 |
| Hispanic/Latino | 964 |
| Bachelor's or higher | 7423 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 16](/us/states/in/districts/senate/16.md) — 100% (state senate)
- [IN House District 83](/us/states/in/districts/house/83.md) — 54% (state house)
- [IN House District 18](/us/states/in/districts/house/18.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
