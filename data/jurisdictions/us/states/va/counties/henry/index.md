---
type: Jurisdiction
title: "Henry County, VA"
classification: county
fips: "51089"
state: "VA"
demographics:
  population: 49980
  population_under_18: 9623
  population_18_64: 27924
  population_65_plus: 12433
  median_household_income: 50760
  poverty_rate: 16.02
  homeownership_rate: 75.17
  unemployment_rate: 4.06
  median_home_value: 134800
  gini_index: 0.4523
  vacancy_rate: 17.17
  race_white: 34448
  race_black: 11123
  race_asian: 260
  race_native: 127
  hispanic: 3476
  bachelors_plus: 7719
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/48"
    rel: in-district
    area_weight: 0.6943
  - to: "us/states/va/districts/house/47"
    rel: in-district
    area_weight: 0.3054
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Henry County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49980 |
| Under 18 | 9623 |
| 18–64 | 27924 |
| 65+ | 12433 |
| Median household income | 50760 |
| Poverty rate | 16.02 |
| Homeownership rate | 75.17 |
| Unemployment rate | 4.06 |
| Median home value | 134800 |
| Gini index | 0.4523 |
| Vacancy rate | 17.17 |
| White | 34448 |
| Black | 11123 |
| Asian | 260 |
| Native | 127 |
| Hispanic/Latino | 3476 |
| Bachelor's or higher | 7719 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 48](/us/states/va/districts/house/48.md) — 69% (state house)
- [VA House District 47](/us/states/va/districts/house/47.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
