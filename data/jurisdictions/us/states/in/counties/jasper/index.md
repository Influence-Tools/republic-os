---
type: Jurisdiction
title: "Jasper County, IN"
classification: county
fips: "18073"
state: "IN"
demographics:
  population: 33234
  population_under_18: 7650
  population_18_64: 19378
  population_65_plus: 6206
  median_household_income: 77314
  poverty_rate: 8.39
  homeownership_rate: 83.57
  unemployment_rate: 4.89
  median_home_value: 221500
  gini_index: 0.4137
  vacancy_rate: 7.49
  race_white: 29174
  race_black: 238
  race_asian: 58
  race_native: 15
  hispanic: 2526
  bachelors_plus: 5881
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/6"
    rel: in-district
    area_weight: 0.5014
  - to: "us/states/in/districts/senate/5"
    rel: in-district
    area_weight: 0.4985
  - to: "us/states/in/districts/house/16"
    rel: in-district
    area_weight: 0.7431
  - to: "us/states/in/districts/house/11"
    rel: in-district
    area_weight: 0.1639
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.093
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Jasper County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33234 |
| Under 18 | 7650 |
| 18–64 | 19378 |
| 65+ | 6206 |
| Median household income | 77314 |
| Poverty rate | 8.39 |
| Homeownership rate | 83.57 |
| Unemployment rate | 4.89 |
| Median home value | 221500 |
| Gini index | 0.4137 |
| Vacancy rate | 7.49 |
| White | 29174 |
| Black | 238 |
| Asian | 58 |
| Native | 15 |
| Hispanic/Latino | 2526 |
| Bachelor's or higher | 5881 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 6](/us/states/in/districts/senate/6.md) — 50% (state senate)
- [IN Senate District 5](/us/states/in/districts/senate/5.md) — 50% (state senate)
- [IN House District 16](/us/states/in/districts/house/16.md) — 74% (state house)
- [IN House District 11](/us/states/in/districts/house/11.md) — 16% (state house)
- [IN House District 13](/us/states/in/districts/house/13.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
