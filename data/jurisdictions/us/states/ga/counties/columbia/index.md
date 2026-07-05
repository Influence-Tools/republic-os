---
type: Jurisdiction
title: "Columbia County, GA"
classification: county
fips: "13073"
state: "GA"
demographics:
  population: 162434
  population_under_18: 40356
  population_18_64: 97523
  population_65_plus: 24555
  median_household_income: 95592
  poverty_rate: 7.47
  homeownership_rate: 78.14
  unemployment_rate: 4.8
  median_home_value: 305300
  gini_index: 0.4087
  vacancy_rate: 10.57
  race_white: 106632
  race_black: 30909
  race_asian: 7859
  race_native: 434
  hispanic: 12985
  bachelors_plus: 60398
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.6988
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.301
  - to: "us/states/ga/districts/house/125"
    rel: in-district
    area_weight: 0.5943
  - to: "us/states/ga/districts/house/123"
    rel: in-district
    area_weight: 0.1984
  - to: "us/states/ga/districts/house/131"
    rel: in-district
    area_weight: 0.1347
  - to: "us/states/ga/districts/house/127"
    rel: in-district
    area_weight: 0.0724
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Columbia County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 162434 |
| Under 18 | 40356 |
| 18–64 | 97523 |
| 65+ | 24555 |
| Median household income | 95592 |
| Poverty rate | 7.47 |
| Homeownership rate | 78.14 |
| Unemployment rate | 4.8 |
| Median home value | 305300 |
| Gini index | 0.4087 |
| Vacancy rate | 10.57 |
| White | 106632 |
| Black | 30909 |
| Asian | 7859 |
| Native | 434 |
| Hispanic/Latino | 12985 |
| Bachelor's or higher | 60398 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 70% (state senate)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 30% (state senate)
- [GA House District 125](/us/states/ga/districts/house/125.md) — 59% (state house)
- [GA House District 123](/us/states/ga/districts/house/123.md) — 20% (state house)
- [GA House District 131](/us/states/ga/districts/house/131.md) — 13% (state house)
- [GA House District 127](/us/states/ga/districts/house/127.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
