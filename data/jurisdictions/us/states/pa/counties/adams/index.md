---
type: Jurisdiction
title: "Adams County, PA"
classification: county
fips: "42001"
state: "PA"
demographics:
  population: 106115
  population_under_18: 20638
  population_18_64: 62347
  population_65_plus: 23130
  median_household_income: 84092
  poverty_rate: 8.19
  homeownership_rate: 78.88
  unemployment_rate: 3.36
  median_home_value: 268500
  gini_index: 0.3994
  vacancy_rate: 6.48
  race_white: 94377
  race_black: 1952
  race_asian: 1000
  race_native: 347
  hispanic: 8213
  bachelors_plus: 27421
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/pa/districts/senate/33"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/house/91"
    rel: in-district
    area_weight: 0.6218
  - to: "us/states/pa/districts/house/193"
    rel: in-district
    area_weight: 0.3777
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Adams County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106115 |
| Under 18 | 20638 |
| 18–64 | 62347 |
| 65+ | 23130 |
| Median household income | 84092 |
| Poverty rate | 8.19 |
| Homeownership rate | 78.88 |
| Unemployment rate | 3.36 |
| Median home value | 268500 |
| Gini index | 0.3994 |
| Vacancy rate | 6.48 |
| White | 94377 |
| Black | 1952 |
| Asian | 1000 |
| Native | 347 |
| Hispanic/Latino | 8213 |
| Bachelor's or higher | 27421 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 33](/us/states/pa/districts/senate/33.md) — 100% (state senate)
- [PA House District 91](/us/states/pa/districts/house/91.md) — 62% (state house)
- [PA House District 193](/us/states/pa/districts/house/193.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
