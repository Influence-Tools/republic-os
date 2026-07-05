---
type: Jurisdiction
title: "Madison County, MT"
classification: county
fips: "30057"
state: "MT"
demographics:
  population: 9223
  population_under_18: 1504
  population_18_64: 4880
  population_65_plus: 2839
  median_household_income: 75250
  poverty_rate: 6.17
  homeownership_rate: 80.96
  unemployment_rate: 3.11
  median_home_value: 470100
  gini_index: 0.4285
  vacancy_rate: 41.53
  race_white: 8474
  race_black: 0
  race_asian: 42
  race_native: 84
  hispanic: 337
  bachelors_plus: 2942
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/senate/35"
    rel: in-district
    area_weight: 0.9906
  - to: "us/states/mt/districts/senate/30"
    rel: in-district
    area_weight: 0.0093
  - to: "us/states/mt/districts/house/69"
    rel: in-district
    area_weight: 0.9906
  - to: "us/states/mt/districts/house/60"
    rel: in-district
    area_weight: 0.0093
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Madison County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9223 |
| Under 18 | 1504 |
| 18–64 | 4880 |
| 65+ | 2839 |
| Median household income | 75250 |
| Poverty rate | 6.17 |
| Homeownership rate | 80.96 |
| Unemployment rate | 3.11 |
| Median home value | 470100 |
| Gini index | 0.4285 |
| Vacancy rate | 41.53 |
| White | 8474 |
| Black | 0 |
| Asian | 42 |
| Native | 84 |
| Hispanic/Latino | 337 |
| Bachelor's or higher | 2942 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 35](/us/states/mt/districts/senate/35.md) — 99% (state senate)
- [MT Senate District 30](/us/states/mt/districts/senate/30.md) — 1% (state senate)
- [MT House District 69](/us/states/mt/districts/house/69.md) — 99% (state house)
- [MT House District 60](/us/states/mt/districts/house/60.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
