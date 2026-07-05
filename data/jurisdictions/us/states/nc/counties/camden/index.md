---
type: Jurisdiction
title: "Camden County, NC"
classification: county
fips: "37029"
state: "NC"
demographics:
  population: 10927
  population_under_18: 2528
  population_18_64: 6600
  population_65_plus: 1799
  median_household_income: 91078
  poverty_rate: 6.14
  homeownership_rate: 82.1
  unemployment_rate: 5.49
  median_home_value: 337100
  gini_index: 0.407
  vacancy_rate: 6.74
  race_white: 8536
  race_black: 1031
  race_asian: 127
  race_native: 8
  hispanic: 460
  bachelors_plus: 3038
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.7983
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.7849
  - to: "us/states/nc/districts/house/5"
    rel: in-district
    area_weight: 0.7847
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Camden County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10927 |
| Under 18 | 2528 |
| 18–64 | 6600 |
| 65+ | 1799 |
| Median household income | 91078 |
| Poverty rate | 6.14 |
| Homeownership rate | 82.1 |
| Unemployment rate | 5.49 |
| Median home value | 337100 |
| Gini index | 0.407 |
| Vacancy rate | 6.74 |
| White | 8536 |
| Black | 1031 |
| Asian | 127 |
| Native | 8 |
| Hispanic/Latino | 460 |
| Bachelor's or higher | 3038 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 80% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 78% (state senate)
- [NC House District 5](/us/states/nc/districts/house/5.md) — 78% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
