---
type: Jurisdiction
title: "Lake County, MI"
classification: county
fips: "26085"
state: "MI"
demographics:
  population: 12563
  population_under_18: 1857
  population_18_64: 7283
  population_65_plus: 3423
  median_household_income: 50805
  poverty_rate: 20.52
  homeownership_rate: 81.98
  unemployment_rate: 7.39
  median_home_value: 133900
  gini_index: 0.4292
  vacancy_rate: 61.44
  race_white: 10038
  race_black: 1005
  race_asian: 38
  race_native: 147
  hispanic: 1163
  bachelors_plus: 1580
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/33"
    rel: in-district
    area_weight: 0.6265
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.3734
  - to: "us/states/mi/districts/house/101"
    rel: in-district
    area_weight: 0.7502
  - to: "us/states/mi/districts/house/100"
    rel: in-district
    area_weight: 0.2497
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Lake County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12563 |
| Under 18 | 1857 |
| 18–64 | 7283 |
| 65+ | 3423 |
| Median household income | 50805 |
| Poverty rate | 20.52 |
| Homeownership rate | 81.98 |
| Unemployment rate | 7.39 |
| Median home value | 133900 |
| Gini index | 0.4292 |
| Vacancy rate | 61.44 |
| White | 10038 |
| Black | 1005 |
| Asian | 38 |
| Native | 147 |
| Hispanic/Latino | 1163 |
| Bachelor's or higher | 1580 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 33](/us/states/mi/districts/senate/33.md) — 63% (state senate)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 37% (state senate)
- [MI House District 101](/us/states/mi/districts/house/101.md) — 75% (state house)
- [MI House District 100](/us/states/mi/districts/house/100.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
