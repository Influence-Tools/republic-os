---
type: Jurisdiction
title: "Bradford County, PA"
classification: county
fips: "42015"
state: "PA"
demographics:
  population: 59858
  population_under_18: 13248
  population_18_64: 33197
  population_65_plus: 13413
  median_household_income: 63675
  poverty_rate: 12.65
  homeownership_rate: 72.16
  unemployment_rate: 6.34
  median_home_value: 187500
  gini_index: 0.4465
  vacancy_rate: 16.54
  race_white: 56595
  race_black: 563
  race_asian: 327
  race_native: 39
  hispanic: 1011
  bachelors_plus: 12203
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/68"
    rel: in-district
    area_weight: 0.5013
  - to: "us/states/pa/districts/house/110"
    rel: in-district
    area_weight: 0.4985
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Bradford County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59858 |
| Under 18 | 13248 |
| 18–64 | 33197 |
| 65+ | 13413 |
| Median household income | 63675 |
| Poverty rate | 12.65 |
| Homeownership rate | 72.16 |
| Unemployment rate | 6.34 |
| Median home value | 187500 |
| Gini index | 0.4465 |
| Vacancy rate | 16.54 |
| White | 56595 |
| Black | 563 |
| Asian | 327 |
| Native | 39 |
| Hispanic/Latino | 1011 |
| Bachelor's or higher | 12203 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 23](/us/states/pa/districts/senate/23.md) — 100% (state senate)
- [PA House District 68](/us/states/pa/districts/house/68.md) — 50% (state house)
- [PA House District 110](/us/states/pa/districts/house/110.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
