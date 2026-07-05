---
type: Jurisdiction
title: "St. Bernard Parish, LA"
classification: county
fips: "22087"
state: "LA"
demographics:
  population: 44419
  population_under_18: 11514
  population_18_64: 26977
  population_65_plus: 5928
  median_household_income: 58651
  poverty_rate: 22.96
  homeownership_rate: 70.15
  unemployment_rate: 7.57
  median_home_value: 202500
  gini_index: 0.4802
  vacancy_rate: 11.12
  race_white: 25906
  race_black: 10591
  race_asian: 864
  race_native: 362
  hispanic: 6167
  bachelors_plus: 6913
districts:
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.2963
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.0076
  - to: "us/states/la/districts/senate/1"
    rel: in-district
    area_weight: 0.2685
  - to: "us/states/la/districts/senate/3"
    rel: in-district
    area_weight: 0.0176
  - to: "us/states/la/districts/house/103"
    rel: in-district
    area_weight: 0.2861
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Bernard Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44419 |
| Under 18 | 11514 |
| 18–64 | 26977 |
| 65+ | 5928 |
| Median household income | 58651 |
| Poverty rate | 22.96 |
| Homeownership rate | 70.15 |
| Unemployment rate | 7.57 |
| Median home value | 202500 |
| Gini index | 0.4802 |
| Vacancy rate | 11.12 |
| White | 25906 |
| Black | 10591 |
| Asian | 864 |
| Native | 362 |
| Hispanic/Latino | 6167 |
| Bachelor's or higher | 6913 |

## Districts

- [LA-01](/us/states/la/districts/01.md) — 30% (congressional)
- [LA-02](/us/states/la/districts/02.md) — 1% (congressional)
- [LA Senate District 1](/us/states/la/districts/senate/1.md) — 27% (state senate)
- [LA Senate District 3](/us/states/la/districts/senate/3.md) — 2% (state senate)
- [LA House District 103](/us/states/la/districts/house/103.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
