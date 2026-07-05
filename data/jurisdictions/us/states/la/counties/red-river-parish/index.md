---
type: Jurisdiction
title: "Red River Parish, LA"
classification: county
fips: "22081"
state: "LA"
demographics:
  population: 7443
  population_under_18: 1744
  population_18_64: 4216
  population_65_plus: 1483
  median_household_income: 49167
  poverty_rate: 25.77
  homeownership_rate: 77.32
  unemployment_rate: 3.64
  median_home_value: 119700
  gini_index: 0.4709
  vacancy_rate: 14.25
  race_white: 4242
  race_black: 2998
  race_asian: 0
  race_native: 0
  hispanic: 138
  bachelors_plus: 904
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.995
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.005
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/house/5"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Red River Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7443 |
| Under 18 | 1744 |
| 18–64 | 4216 |
| 65+ | 1483 |
| Median household income | 49167 |
| Poverty rate | 25.77 |
| Homeownership rate | 77.32 |
| Unemployment rate | 3.64 |
| Median home value | 119700 |
| Gini index | 0.4709 |
| Vacancy rate | 14.25 |
| White | 4242 |
| Black | 2998 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 138 |
| Bachelor's or higher | 904 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA-06](/us/states/la/districts/06.md) — 0% (congressional)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 100% (state senate)
- [LA House District 5](/us/states/la/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
