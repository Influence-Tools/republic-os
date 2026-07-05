---
type: Jurisdiction
title: "Love County, OK"
classification: county
fips: "40085"
state: "OK"
demographics:
  population: 10261
  population_under_18: 2474
  population_18_64: 5929
  population_65_plus: 1858
  median_household_income: 66580
  poverty_rate: 14.98
  homeownership_rate: 72.99
  unemployment_rate: 5.24
  median_home_value: 171000
  gini_index: 0.4393
  vacancy_rate: 17.6
  race_white: 7233
  race_black: 213
  race_asian: 79
  race_native: 438
  hispanic: 1867
  bachelors_plus: 1417
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/ok/districts/senate/31"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/ok/districts/house/49"
    rel: in-district
    area_weight: 0.9983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Love County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10261 |
| Under 18 | 2474 |
| 18–64 | 5929 |
| 65+ | 1858 |
| Median household income | 66580 |
| Poverty rate | 14.98 |
| Homeownership rate | 72.99 |
| Unemployment rate | 5.24 |
| Median home value | 171000 |
| Gini index | 0.4393 |
| Vacancy rate | 17.6 |
| White | 7233 |
| Black | 213 |
| Asian | 79 |
| Native | 438 |
| Hispanic/Latino | 1867 |
| Bachelor's or higher | 1417 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 31](/us/states/ok/districts/senate/31.md) — 100% (state senate)
- [OK House District 49](/us/states/ok/districts/house/49.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
