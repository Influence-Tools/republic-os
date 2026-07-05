---
type: Jurisdiction
title: "Howard County, IN"
classification: county
fips: "18067"
state: "IN"
demographics:
  population: 83752
  population_under_18: 19135
  population_18_64: 47985
  population_65_plus: 16632
  median_household_income: 64027
  poverty_rate: 13.41
  homeownership_rate: 70.57
  unemployment_rate: 5.83
  median_home_value: 165000
  gini_index: 0.4407
  vacancy_rate: 10.74
  race_white: 70905
  race_black: 6176
  race_asian: 1198
  race_native: 46
  hispanic: 3438
  bachelors_plus: 16136
districts:
  - to: "us/states/in/districts/05"
    rel: in-district
    area_weight: 0.9611
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.0389
  - to: "us/states/in/districts/senate/18"
    rel: in-district
    area_weight: 0.6897
  - to: "us/states/in/districts/senate/21"
    rel: in-district
    area_weight: 0.3102
  - to: "us/states/in/districts/house/30"
    rel: in-district
    area_weight: 0.5778
  - to: "us/states/in/districts/house/38"
    rel: in-district
    area_weight: 0.4221
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Howard County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83752 |
| Under 18 | 19135 |
| 18–64 | 47985 |
| 65+ | 16632 |
| Median household income | 64027 |
| Poverty rate | 13.41 |
| Homeownership rate | 70.57 |
| Unemployment rate | 5.83 |
| Median home value | 165000 |
| Gini index | 0.4407 |
| Vacancy rate | 10.74 |
| White | 70905 |
| Black | 6176 |
| Asian | 1198 |
| Native | 46 |
| Hispanic/Latino | 3438 |
| Bachelor's or higher | 16136 |

## Districts

- [IN-05](/us/states/in/districts/05.md) — 96% (congressional)
- [IN-04](/us/states/in/districts/04.md) — 4% (congressional)
- [IN Senate District 18](/us/states/in/districts/senate/18.md) — 69% (state senate)
- [IN Senate District 21](/us/states/in/districts/senate/21.md) — 31% (state senate)
- [IN House District 30](/us/states/in/districts/house/30.md) — 58% (state house)
- [IN House District 38](/us/states/in/districts/house/38.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
