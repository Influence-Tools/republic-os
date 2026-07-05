---
type: Jurisdiction
title: "Hart County, KY"
classification: county
fips: "21099"
state: "KY"
demographics:
  population: 19603
  population_under_18: 4782
  population_18_64: 11372
  population_65_plus: 3449
  median_household_income: 52285
  poverty_rate: 19.31
  homeownership_rate: 72.44
  unemployment_rate: 3.75
  median_home_value: 146000
  gini_index: 0.4506
  vacancy_rate: 17.39
  race_white: 17892
  race_black: 577
  race_asian: 105
  race_native: 55
  hispanic: 412
  bachelors_plus: 2259
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/9"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/24"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Hart County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19603 |
| Under 18 | 4782 |
| 18–64 | 11372 |
| 65+ | 3449 |
| Median household income | 52285 |
| Poverty rate | 19.31 |
| Homeownership rate | 72.44 |
| Unemployment rate | 3.75 |
| Median home value | 146000 |
| Gini index | 0.4506 |
| Vacancy rate | 17.39 |
| White | 17892 |
| Black | 577 |
| Asian | 105 |
| Native | 55 |
| Hispanic/Latino | 412 |
| Bachelor's or higher | 2259 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 9](/us/states/ky/districts/senate/9.md) — 100% (state senate)
- [KY House District 24](/us/states/ky/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
