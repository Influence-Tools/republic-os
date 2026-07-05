---
type: Jurisdiction
title: "Christian County, KY"
classification: county
fips: "21047"
state: "KY"
demographics:
  population: 72069
  population_under_18: 20421
  population_18_64: 42480
  population_65_plus: 9168
  median_household_income: 55494
  poverty_rate: 17.12
  homeownership_rate: 50.04
  unemployment_rate: 6.32
  median_home_value: 173600
  gini_index: 0.4365
  vacancy_rate: 12.39
  race_white: 48400
  race_black: 13549
  race_asian: 896
  race_native: 146
  hispanic: 6267
  bachelors_plus: 10882
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/senate/3"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/8"
    rel: in-district
    area_weight: 0.4116
  - to: "us/states/ky/districts/house/9"
    rel: in-district
    area_weight: 0.323
  - to: "us/states/ky/districts/house/16"
    rel: in-district
    area_weight: 0.2651
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Christian County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 72069 |
| Under 18 | 20421 |
| 18–64 | 42480 |
| 65+ | 9168 |
| Median household income | 55494 |
| Poverty rate | 17.12 |
| Homeownership rate | 50.04 |
| Unemployment rate | 6.32 |
| Median home value | 173600 |
| Gini index | 0.4365 |
| Vacancy rate | 12.39 |
| White | 48400 |
| Black | 13549 |
| Asian | 896 |
| Native | 146 |
| Hispanic/Latino | 6267 |
| Bachelor's or higher | 10882 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 3](/us/states/ky/districts/senate/3.md) — 100% (state senate)
- [KY House District 8](/us/states/ky/districts/house/8.md) — 41% (state house)
- [KY House District 9](/us/states/ky/districts/house/9.md) — 32% (state house)
- [KY House District 16](/us/states/ky/districts/house/16.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
