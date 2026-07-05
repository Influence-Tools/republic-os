---
type: Jurisdiction
title: "Pottawatomie County, OK"
classification: county
fips: "40125"
state: "OK"
demographics:
  population: 73463
  population_under_18: 16979
  population_18_64: 44245
  population_65_plus: 12239
  median_household_income: 61398
  poverty_rate: 15.89
  homeownership_rate: 70.39
  unemployment_rate: 5.29
  median_home_value: 165400
  gini_index: 0.4367
  vacancy_rate: 11.18
  race_white: 52298
  race_black: 2176
  race_asian: 739
  race_native: 8348
  hispanic: 4682
  bachelors_plus: 13288
districts:
  - to: "us/states/ok/districts/05"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ok/districts/senate/17"
    rel: in-district
    area_weight: 0.7923
  - to: "us/states/ok/districts/senate/28"
    rel: in-district
    area_weight: 0.2076
  - to: "us/states/ok/districts/house/28"
    rel: in-district
    area_weight: 0.4286
  - to: "us/states/ok/districts/house/27"
    rel: in-district
    area_weight: 0.3447
  - to: "us/states/ok/districts/house/26"
    rel: in-district
    area_weight: 0.1545
  - to: "us/states/ok/districts/house/25"
    rel: in-district
    area_weight: 0.0721
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Pottawatomie County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 73463 |
| Under 18 | 16979 |
| 18–64 | 44245 |
| 65+ | 12239 |
| Median household income | 61398 |
| Poverty rate | 15.89 |
| Homeownership rate | 70.39 |
| Unemployment rate | 5.29 |
| Median home value | 165400 |
| Gini index | 0.4367 |
| Vacancy rate | 11.18 |
| White | 52298 |
| Black | 2176 |
| Asian | 739 |
| Native | 8348 |
| Hispanic/Latino | 4682 |
| Bachelor's or higher | 13288 |

## Districts

- [OK-05](/us/states/ok/districts/05.md) — 100% (congressional)
- [OK Senate District 17](/us/states/ok/districts/senate/17.md) — 79% (state senate)
- [OK Senate District 28](/us/states/ok/districts/senate/28.md) — 21% (state senate)
- [OK House District 28](/us/states/ok/districts/house/28.md) — 43% (state house)
- [OK House District 27](/us/states/ok/districts/house/27.md) — 34% (state house)
- [OK House District 26](/us/states/ok/districts/house/26.md) — 15% (state house)
- [OK House District 25](/us/states/ok/districts/house/25.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
