---
type: Jurisdiction
title: "Greene County, IN"
classification: county
fips: "18055"
state: "IN"
demographics:
  population: 31021
  population_under_18: 6626
  population_18_64: 18075
  population_65_plus: 6320
  median_household_income: 62094
  poverty_rate: 12.75
  homeownership_rate: 77.0
  unemployment_rate: 6.04
  median_home_value: 153200
  gini_index: 0.4454
  vacancy_rate: 8.7
  race_white: 29734
  race_black: 147
  race_asian: 75
  race_native: 26
  hispanic: 649
  bachelors_plus: 4690
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/45"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Greene County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31021 |
| Under 18 | 6626 |
| 18–64 | 18075 |
| 65+ | 6320 |
| Median household income | 62094 |
| Poverty rate | 12.75 |
| Homeownership rate | 77.0 |
| Unemployment rate | 6.04 |
| Median home value | 153200 |
| Gini index | 0.4454 |
| Vacancy rate | 8.7 |
| White | 29734 |
| Black | 147 |
| Asian | 75 |
| Native | 26 |
| Hispanic/Latino | 649 |
| Bachelor's or higher | 4690 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 100% (state senate)
- [IN House District 45](/us/states/in/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
