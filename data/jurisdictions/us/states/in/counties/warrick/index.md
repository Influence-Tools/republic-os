---
type: Jurisdiction
title: "Warrick County, IN"
classification: county
fips: "18173"
state: "IN"
demographics:
  population: 65261
  population_under_18: 15035
  population_18_64: 38029
  population_65_plus: 12197
  median_household_income: 89844
  poverty_rate: 7.0
  homeownership_rate: 82.41
  unemployment_rate: 3.12
  median_home_value: 242500
  gini_index: 0.4516
  vacancy_rate: 6.42
  race_white: 58989
  race_black: 1297
  race_asian: 1139
  race_native: 182
  hispanic: 1630
  bachelors_plus: 22168
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/50"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/house/75"
    rel: in-district
    area_weight: 0.9803
  - to: "us/states/in/districts/house/78"
    rel: in-district
    area_weight: 0.0192
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Warrick County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65261 |
| Under 18 | 15035 |
| 18–64 | 38029 |
| 65+ | 12197 |
| Median household income | 89844 |
| Poverty rate | 7.0 |
| Homeownership rate | 82.41 |
| Unemployment rate | 3.12 |
| Median home value | 242500 |
| Gini index | 0.4516 |
| Vacancy rate | 6.42 |
| White | 58989 |
| Black | 1297 |
| Asian | 1139 |
| Native | 182 |
| Hispanic/Latino | 1630 |
| Bachelor's or higher | 22168 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 50](/us/states/in/districts/senate/50.md) — 100% (state senate)
- [IN House District 75](/us/states/in/districts/house/75.md) — 98% (state house)
- [IN House District 78](/us/states/in/districts/house/78.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
