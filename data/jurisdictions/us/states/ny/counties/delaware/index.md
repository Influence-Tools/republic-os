---
type: Jurisdiction
title: "Delaware County, NY"
classification: county
fips: "36025"
state: "NY"
demographics:
  population: 44487
  population_under_18: 7074
  population_18_64: 25666
  population_65_plus: 11747
  median_household_income: 63337
  poverty_rate: 14.41
  homeownership_rate: 77.25
  unemployment_rate: 6.45
  median_home_value: 183100
  gini_index: 0.4585
  vacancy_rate: 36.11
  race_white: 39970
  race_black: 481
  race_asian: 405
  race_native: 308
  hispanic: 2179
  bachelors_plus: 13217
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/house/102"
    rel: in-district
    area_weight: 0.4777
  - to: "us/states/ny/districts/house/101"
    rel: in-district
    area_weight: 0.3492
  - to: "us/states/ny/districts/house/121"
    rel: in-district
    area_weight: 0.1731
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Delaware County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44487 |
| Under 18 | 7074 |
| 18–64 | 25666 |
| 65+ | 11747 |
| Median household income | 63337 |
| Poverty rate | 14.41 |
| Homeownership rate | 77.25 |
| Unemployment rate | 6.45 |
| Median home value | 183100 |
| Gini index | 0.4585 |
| Vacancy rate | 36.11 |
| White | 39970 |
| Black | 481 |
| Asian | 405 |
| Native | 308 |
| Hispanic/Latino | 2179 |
| Bachelor's or higher | 13217 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 100% (state senate)
- [NY House District 102](/us/states/ny/districts/house/102.md) — 48% (state house)
- [NY House District 101](/us/states/ny/districts/house/101.md) — 35% (state house)
- [NY House District 121](/us/states/ny/districts/house/121.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
