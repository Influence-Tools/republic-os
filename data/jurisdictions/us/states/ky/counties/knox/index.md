---
type: Jurisdiction
title: "Knox County, KY"
classification: county
fips: "21121"
state: "KY"
demographics:
  population: 29865
  population_under_18: 7053
  population_18_64: 17609
  population_65_plus: 5203
  median_household_income: 32527
  poverty_rate: 36.9
  homeownership_rate: 65.32
  unemployment_rate: 8.14
  median_home_value: 118700
  gini_index: 0.5246
  vacancy_rate: 15.54
  race_white: 28593
  race_black: 312
  race_asian: 57
  race_native: 7
  hispanic: 389
  bachelors_plus: 4168
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/86"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Knox County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29865 |
| Under 18 | 7053 |
| 18–64 | 17609 |
| 65+ | 5203 |
| Median household income | 32527 |
| Poverty rate | 36.9 |
| Homeownership rate | 65.32 |
| Unemployment rate | 8.14 |
| Median home value | 118700 |
| Gini index | 0.5246 |
| Vacancy rate | 15.54 |
| White | 28593 |
| Black | 312 |
| Asian | 57 |
| Native | 7 |
| Hispanic/Latino | 389 |
| Bachelor's or higher | 4168 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 25](/us/states/ky/districts/senate/25.md) — 100% (state senate)
- [KY House District 86](/us/states/ky/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
