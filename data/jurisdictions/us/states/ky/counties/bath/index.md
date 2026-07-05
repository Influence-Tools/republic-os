---
type: Jurisdiction
title: "Bath County, KY"
classification: county
fips: "21011"
state: "KY"
demographics:
  population: 12851
  population_under_18: 3271
  population_18_64: 7359
  population_65_plus: 2221
  median_household_income: 56541
  poverty_rate: 25.31
  homeownership_rate: 74.71
  unemployment_rate: 2.55
  median_home_value: 129800
  gini_index: 0.5405
  vacancy_rate: 14.57
  race_white: 12231
  race_black: 90
  race_asian: 5
  race_native: 5
  hispanic: 235
  bachelors_plus: 1502
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.5425
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.4575
  - to: "us/states/ky/districts/senate/28"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/house/74"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Bath County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12851 |
| Under 18 | 3271 |
| 18–64 | 7359 |
| 65+ | 2221 |
| Median household income | 56541 |
| Poverty rate | 25.31 |
| Homeownership rate | 74.71 |
| Unemployment rate | 2.55 |
| Median home value | 129800 |
| Gini index | 0.5405 |
| Vacancy rate | 14.57 |
| White | 12231 |
| Black | 90 |
| Asian | 5 |
| Native | 5 |
| Hispanic/Latino | 235 |
| Bachelor's or higher | 1502 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 54% (congressional)
- [KY-06](/us/states/ky/districts/06.md) — 46% (congressional)
- [KY Senate District 28](/us/states/ky/districts/senate/28.md) — 100% (state senate)
- [KY House District 74](/us/states/ky/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
