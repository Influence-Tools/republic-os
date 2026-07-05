---
type: Jurisdiction
title: "Indiana County, PA"
classification: county
fips: "42063"
state: "PA"
demographics:
  population: 83042
  population_under_18: 14946
  population_18_64: 51020
  population_65_plus: 17076
  median_household_income: 60208
  poverty_rate: 13.98
  homeownership_rate: 72.14
  unemployment_rate: 6.74
  median_home_value: 152800
  gini_index: 0.4511
  vacancy_rate: 13.66
  race_white: 76532
  race_black: 1886
  race_asian: 743
  race_native: 16
  hispanic: 1546
  bachelors_plus: 20792
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.7487
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.251
  - to: "us/states/pa/districts/senate/41"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/62"
    rel: in-district
    area_weight: 0.5972
  - to: "us/states/pa/districts/house/66"
    rel: in-district
    area_weight: 0.4026
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Indiana County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83042 |
| Under 18 | 14946 |
| 18–64 | 51020 |
| 65+ | 17076 |
| Median household income | 60208 |
| Poverty rate | 13.98 |
| Homeownership rate | 72.14 |
| Unemployment rate | 6.74 |
| Median home value | 152800 |
| Gini index | 0.4511 |
| Vacancy rate | 13.66 |
| White | 76532 |
| Black | 1886 |
| Asian | 743 |
| Native | 16 |
| Hispanic/Latino | 1546 |
| Bachelor's or higher | 20792 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 75% (congressional)
- [PA-15](/us/states/pa/districts/15.md) — 25% (congressional)
- [PA Senate District 41](/us/states/pa/districts/senate/41.md) — 100% (state senate)
- [PA House District 62](/us/states/pa/districts/house/62.md) — 60% (state house)
- [PA House District 66](/us/states/pa/districts/house/66.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
