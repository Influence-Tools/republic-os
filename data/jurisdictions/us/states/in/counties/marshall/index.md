---
type: Jurisdiction
title: "Marshall County, IN"
classification: county
fips: "18099"
state: "IN"
demographics:
  population: 46284
  population_under_18: 11317
  population_18_64: 26181
  population_65_plus: 8786
  median_household_income: 71808
  poverty_rate: 11.68
  homeownership_rate: 76.37
  unemployment_rate: 2.57
  median_home_value: 204900
  gini_index: 0.4177
  vacancy_rate: 11.7
  race_white: 40685
  race_black: 261
  race_asian: 306
  race_native: 120
  hispanic: 5506
  bachelors_plus: 8675
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/8"
    rel: in-district
    area_weight: 0.8616
  - to: "us/states/in/districts/senate/9"
    rel: in-district
    area_weight: 0.1383
  - to: "us/states/in/districts/house/17"
    rel: in-district
    area_weight: 0.9767
  - to: "us/states/in/districts/house/7"
    rel: in-district
    area_weight: 0.0232
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Marshall County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46284 |
| Under 18 | 11317 |
| 18–64 | 26181 |
| 65+ | 8786 |
| Median household income | 71808 |
| Poverty rate | 11.68 |
| Homeownership rate | 76.37 |
| Unemployment rate | 2.57 |
| Median home value | 204900 |
| Gini index | 0.4177 |
| Vacancy rate | 11.7 |
| White | 40685 |
| Black | 261 |
| Asian | 306 |
| Native | 120 |
| Hispanic/Latino | 5506 |
| Bachelor's or higher | 8675 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 8](/us/states/in/districts/senate/8.md) — 86% (state senate)
- [IN Senate District 9](/us/states/in/districts/senate/9.md) — 14% (state senate)
- [IN House District 17](/us/states/in/districts/house/17.md) — 98% (state house)
- [IN House District 7](/us/states/in/districts/house/7.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
