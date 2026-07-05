---
type: Jurisdiction
title: "Clay County, IA"
classification: county
fips: "19041"
state: "IA"
demographics:
  population: 16461
  population_under_18: 3841
  population_18_64: 8934
  population_65_plus: 3686
  median_household_income: 65428
  poverty_rate: 11.41
  homeownership_rate: 73.33
  unemployment_rate: 3.51
  median_home_value: 178600
  gini_index: 0.417
  vacancy_rate: 10.73
  race_white: 15285
  race_black: 45
  race_asian: 124
  race_native: 26
  hispanic: 781
  bachelors_plus: 3952
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/3"
    rel: in-district
    area_weight: 0.6351
  - to: "us/states/ia/districts/senate/5"
    rel: in-district
    area_weight: 0.3649
  - to: "us/states/ia/districts/house/6"
    rel: in-district
    area_weight: 0.6351
  - to: "us/states/ia/districts/house/10"
    rel: in-district
    area_weight: 0.3649
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Clay County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16461 |
| Under 18 | 3841 |
| 18–64 | 8934 |
| 65+ | 3686 |
| Median household income | 65428 |
| Poverty rate | 11.41 |
| Homeownership rate | 73.33 |
| Unemployment rate | 3.51 |
| Median home value | 178600 |
| Gini index | 0.417 |
| Vacancy rate | 10.73 |
| White | 15285 |
| Black | 45 |
| Asian | 124 |
| Native | 26 |
| Hispanic/Latino | 781 |
| Bachelor's or higher | 3952 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 3](/us/states/ia/districts/senate/3.md) — 64% (state senate)
- [IA Senate District 5](/us/states/ia/districts/senate/5.md) — 36% (state senate)
- [IA House District 6](/us/states/ia/districts/house/6.md) — 64% (state house)
- [IA House District 10](/us/states/ia/districts/house/10.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
