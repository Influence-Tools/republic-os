---
type: Jurisdiction
title: "Winston County, AL"
classification: county
fips: "01133"
state: "AL"
demographics:
  population: 23682
  population_under_18: 5327
  population_18_64: 6396
  population_65_plus: 11959
  median_household_income: 57256
  poverty_rate: 18.66
  homeownership_rate: 75.8
  unemployment_rate: 3.58
  median_home_value: 118900
  gini_index: 0.4474
  vacancy_rate: 28.42
  race_white: 21573
  race_black: 237
  race_asian: 73
  race_native: 78
  hispanic: 880
  bachelors_plus: 3385
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/14"
    rel: in-district
    area_weight: 0.9743
  - to: "us/states/al/districts/house/17"
    rel: in-district
    area_weight: 0.0255
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Winston County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23682 |
| Under 18 | 5327 |
| 18–64 | 6396 |
| 65+ | 11959 |
| Median household income | 57256 |
| Poverty rate | 18.66 |
| Homeownership rate | 75.8 |
| Unemployment rate | 3.58 |
| Median home value | 118900 |
| Gini index | 0.4474 |
| Vacancy rate | 28.42 |
| White | 21573 |
| Black | 237 |
| Asian | 73 |
| Native | 78 |
| Hispanic/Latino | 880 |
| Bachelor's or higher | 3385 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 4](/us/states/al/districts/senate/4.md) — 100% (state senate)
- [AL House District 14](/us/states/al/districts/house/14.md) — 97% (state house)
- [AL House District 17](/us/states/al/districts/house/17.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
