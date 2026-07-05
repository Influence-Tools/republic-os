---
type: Jurisdiction
title: "Williams County, ND"
classification: county
fips: "38105"
state: "ND"
demographics:
  population: 39555
  population_under_18: 11934
  population_18_64: 23687
  population_65_plus: 3934
  median_household_income: 85595
  poverty_rate: 8.64
  homeownership_rate: 52.98
  unemployment_rate: 4.36
  median_home_value: 284800
  gini_index: 0.4595
  vacancy_rate: 25.63
  race_white: 31591
  race_black: 1858
  race_asian: 481
  race_native: 1218
  hispanic: 4028
  bachelors_plus: 7721
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/2"
    rel: in-district
    area_weight: 0.9026
  - to: "us/states/nd/districts/senate/23"
    rel: in-district
    area_weight: 0.0898
  - to: "us/states/nd/districts/senate/1"
    rel: in-district
    area_weight: 0.0075
  - to: "us/states/nd/districts/house/2"
    rel: in-district
    area_weight: 0.9026
  - to: "us/states/nd/districts/house/23"
    rel: in-district
    area_weight: 0.0898
  - to: "us/states/nd/districts/house/1"
    rel: in-district
    area_weight: 0.0075
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Williams County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39555 |
| Under 18 | 11934 |
| 18–64 | 23687 |
| 65+ | 3934 |
| Median household income | 85595 |
| Poverty rate | 8.64 |
| Homeownership rate | 52.98 |
| Unemployment rate | 4.36 |
| Median home value | 284800 |
| Gini index | 0.4595 |
| Vacancy rate | 25.63 |
| White | 31591 |
| Black | 1858 |
| Asian | 481 |
| Native | 1218 |
| Hispanic/Latino | 4028 |
| Bachelor's or higher | 7721 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 2](/us/states/nd/districts/senate/2.md) — 90% (state senate)
- [ND Senate District 23](/us/states/nd/districts/senate/23.md) — 9% (state senate)
- [ND Senate District 1](/us/states/nd/districts/senate/1.md) — 1% (state senate)
- [ND House District 2](/us/states/nd/districts/house/2.md) — 90% (state house)
- [ND House District 23](/us/states/nd/districts/house/23.md) — 9% (state house)
- [ND House District 1](/us/states/nd/districts/house/1.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
