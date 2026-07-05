---
type: Jurisdiction
title: "Morgan County, AL"
classification: county
fips: "01103"
state: "AL"
demographics:
  population: 126084
  population_under_18: 31387
  population_18_64: 39243
  population_65_plus: 55454
  median_household_income: 68686
  poverty_rate: 16.84
  homeownership_rate: 71.7
  unemployment_rate: 4.58
  median_home_value: 226300
  gini_index: 0.4704
  vacancy_rate: 10.8
  race_white: 93378
  race_black: 16056
  race_asian: 1002
  race_native: 770
  hispanic: 14293
  bachelors_plus: 29912
districts:
  - to: "us/states/al/districts/05"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/al/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/9"
    rel: in-district
    area_weight: 0.6762
  - to: "us/states/al/districts/house/8"
    rel: in-district
    area_weight: 0.1594
  - to: "us/states/al/districts/house/4"
    rel: in-district
    area_weight: 0.1307
  - to: "us/states/al/districts/house/7"
    rel: in-district
    area_weight: 0.0336
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Morgan County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 126084 |
| Under 18 | 31387 |
| 18–64 | 39243 |
| 65+ | 55454 |
| Median household income | 68686 |
| Poverty rate | 16.84 |
| Homeownership rate | 71.7 |
| Unemployment rate | 4.58 |
| Median home value | 226300 |
| Gini index | 0.4704 |
| Vacancy rate | 10.8 |
| White | 93378 |
| Black | 16056 |
| Asian | 1002 |
| Native | 770 |
| Hispanic/Latino | 14293 |
| Bachelor's or higher | 29912 |

## Districts

- [AL-05](/us/states/al/districts/05.md) — 100% (congressional)
- [AL Senate District 3](/us/states/al/districts/senate/3.md) — 100% (state senate)
- [AL House District 9](/us/states/al/districts/house/9.md) — 68% (state house)
- [AL House District 8](/us/states/al/districts/house/8.md) — 16% (state house)
- [AL House District 4](/us/states/al/districts/house/4.md) — 13% (state house)
- [AL House District 7](/us/states/al/districts/house/7.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
