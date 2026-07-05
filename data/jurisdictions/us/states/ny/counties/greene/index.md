---
type: Jurisdiction
title: "Greene County, NY"
classification: county
fips: "36039"
state: "NY"
demographics:
  population: 47409
  population_under_18: 7671
  population_18_64: 28296
  population_65_plus: 11442
  median_household_income: 77945
  poverty_rate: 9.88
  homeownership_rate: 77.23
  unemployment_rate: 3.94
  median_home_value: 271600
  gini_index: 0.4671
  vacancy_rate: 35.78
  race_white: 40117
  race_black: 2251
  race_asian: 575
  race_native: 24
  hispanic: 3212
  bachelors_plus: 15297
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/ny/districts/senate/41"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/102"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Greene County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47409 |
| Under 18 | 7671 |
| 18–64 | 28296 |
| 65+ | 11442 |
| Median household income | 77945 |
| Poverty rate | 9.88 |
| Homeownership rate | 77.23 |
| Unemployment rate | 3.94 |
| Median home value | 271600 |
| Gini index | 0.4671 |
| Vacancy rate | 35.78 |
| White | 40117 |
| Black | 2251 |
| Asian | 575 |
| Native | 24 |
| Hispanic/Latino | 3212 |
| Bachelor's or higher | 15297 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 41](/us/states/ny/districts/senate/41.md) — 100% (state senate)
- [NY House District 102](/us/states/ny/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
