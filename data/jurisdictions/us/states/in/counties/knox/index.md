---
type: Jurisdiction
title: "Knox County, IN"
classification: county
fips: "18083"
state: "IN"
demographics:
  population: 36007
  population_under_18: 7787
  population_18_64: 21343
  population_65_plus: 6877
  median_household_income: 61237
  poverty_rate: 13.69
  homeownership_rate: 67.8
  unemployment_rate: 3.12
  median_home_value: 137700
  gini_index: 0.4587
  vacancy_rate: 10.63
  race_white: 32307
  race_black: 604
  race_asian: 310
  race_native: 20
  hispanic: 1076
  bachelors_plus: 6314
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9936
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.0064
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/in/districts/house/64"
    rel: in-district
    area_weight: 0.5977
  - to: "us/states/in/districts/house/45"
    rel: in-district
    area_weight: 0.4016
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Knox County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36007 |
| Under 18 | 7787 |
| 18–64 | 21343 |
| 65+ | 6877 |
| Median household income | 61237 |
| Poverty rate | 13.69 |
| Homeownership rate | 67.8 |
| Unemployment rate | 3.12 |
| Median home value | 137700 |
| Gini index | 0.4587 |
| Vacancy rate | 10.63 |
| White | 32307 |
| Black | 604 |
| Asian | 310 |
| Native | 20 |
| Hispanic/Latino | 1076 |
| Bachelor's or higher | 6314 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 99% (congressional)
- [IL-12](/us/states/il/districts/12.md) — 1% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 100% (state senate)
- [IN House District 64](/us/states/in/districts/house/64.md) — 60% (state house)
- [IN House District 45](/us/states/in/districts/house/45.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
