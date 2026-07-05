---
type: Jurisdiction
title: "Niobrara County, WY"
classification: county
fips: "56027"
state: "WY"
demographics:
  population: 2368
  population_under_18: 248
  population_18_64: 1339
  population_65_plus: 781
  median_household_income: 64113
  poverty_rate: 12.02
  homeownership_rate: 61.78
  unemployment_rate: 2.47
  median_home_value: 221500
  gini_index: 0.4537
  vacancy_rate: 16.63
  race_white: 2177
  race_black: 82
  race_asian: 0
  race_native: 57
  hispanic: 133
  bachelors_plus: 535
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/house/2"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Niobrara County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2368 |
| Under 18 | 248 |
| 18–64 | 1339 |
| 65+ | 781 |
| Median household income | 64113 |
| Poverty rate | 12.02 |
| Homeownership rate | 61.78 |
| Unemployment rate | 2.47 |
| Median home value | 221500 |
| Gini index | 0.4537 |
| Vacancy rate | 16.63 |
| White | 2177 |
| Black | 82 |
| Asian | 0 |
| Native | 57 |
| Hispanic/Latino | 133 |
| Bachelor's or higher | 535 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 3](/us/states/wy/districts/senate/3.md) — 100% (state senate)
- [WY House District 2](/us/states/wy/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
