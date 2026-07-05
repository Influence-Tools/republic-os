---
type: Jurisdiction
title: "Oconto County, WI"
classification: county
fips: "55083"
state: "WI"
demographics:
  population: 39589
  population_under_18: 7789
  population_18_64: 22825
  population_65_plus: 8975
  median_household_income: 75049
  poverty_rate: 8.2
  homeownership_rate: 85.02
  unemployment_rate: 2.0
  median_home_value: 231400
  gini_index: 0.4051
  vacancy_rate: 30.16
  race_white: 37016
  race_black: 57
  race_asian: 140
  race_native: 539
  hispanic: 903
  bachelors_plus: 7121
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.8849
  - to: "us/states/wi/districts/senate/2"
    rel: in-district
    area_weight: 0.5167
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.3678
  - to: "us/states/wi/districts/house/36"
    rel: in-district
    area_weight: 0.3308
  - to: "us/states/wi/districts/house/4"
    rel: in-district
    area_weight: 0.3305
  - to: "us/states/wi/districts/house/6"
    rel: in-district
    area_weight: 0.1861
  - to: "us/states/wi/districts/house/35"
    rel: in-district
    area_weight: 0.037
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Oconto County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39589 |
| Under 18 | 7789 |
| 18–64 | 22825 |
| 65+ | 8975 |
| Median household income | 75049 |
| Poverty rate | 8.2 |
| Homeownership rate | 85.02 |
| Unemployment rate | 2.0 |
| Median home value | 231400 |
| Gini index | 0.4051 |
| Vacancy rate | 30.16 |
| White | 37016 |
| Black | 57 |
| Asian | 140 |
| Native | 539 |
| Hispanic/Latino | 903 |
| Bachelor's or higher | 7121 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 88% (congressional)
- [WI Senate District 2](/us/states/wi/districts/senate/2.md) — 52% (state senate)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 37% (state senate)
- [WI House District 36](/us/states/wi/districts/house/36.md) — 33% (state house)
- [WI House District 4](/us/states/wi/districts/house/4.md) — 33% (state house)
- [WI House District 6](/us/states/wi/districts/house/6.md) — 19% (state house)
- [WI House District 35](/us/states/wi/districts/house/35.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
