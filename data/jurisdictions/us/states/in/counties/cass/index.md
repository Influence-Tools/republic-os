---
type: Jurisdiction
title: "Cass County, IN"
classification: county
fips: "18017"
state: "IN"
demographics:
  population: 37680
  population_under_18: 8683
  population_18_64: 21912
  population_65_plus: 7085
  median_household_income: 56403
  poverty_rate: 13.24
  homeownership_rate: 74.26
  unemployment_rate: 4.58
  median_home_value: 133800
  gini_index: 0.4061
  vacancy_rate: 8.24
  race_white: 28815
  race_black: 442
  race_asian: 542
  race_native: 263
  hispanic: 7000
  bachelors_plus: 5878
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.5744
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.4256
  - to: "us/states/in/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/23"
    rel: in-district
    area_weight: 0.8409
  - to: "us/states/in/districts/house/38"
    rel: in-district
    area_weight: 0.1591
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Cass County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37680 |
| Under 18 | 8683 |
| 18–64 | 21912 |
| 65+ | 7085 |
| Median household income | 56403 |
| Poverty rate | 13.24 |
| Homeownership rate | 74.26 |
| Unemployment rate | 4.58 |
| Median home value | 133800 |
| Gini index | 0.4061 |
| Vacancy rate | 8.24 |
| White | 28815 |
| Black | 442 |
| Asian | 542 |
| Native | 263 |
| Hispanic/Latino | 7000 |
| Bachelor's or higher | 5878 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 57% (congressional)
- [IN-04](/us/states/in/districts/04.md) — 43% (congressional)
- [IN Senate District 18](/us/states/in/districts/senate/18.md) — 100% (state senate)
- [IN House District 23](/us/states/in/districts/house/23.md) — 84% (state house)
- [IN House District 38](/us/states/in/districts/house/38.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
