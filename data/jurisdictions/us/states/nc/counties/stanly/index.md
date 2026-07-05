---
type: Jurisdiction
title: "Stanly County, NC"
classification: county
fips: "37167"
state: "NC"
demographics:
  population: 64651
  population_under_18: 14002
  population_18_64: 38271
  population_65_plus: 12378
  median_household_income: 60704
  poverty_rate: 15.25
  homeownership_rate: 74.45
  unemployment_rate: 4.05
  median_home_value: 242400
  gini_index: 0.4312
  vacancy_rate: 11.85
  race_white: 51164
  race_black: 7259
  race_asian: 1222
  race_native: 59
  hispanic: 3685
  bachelors_plus: 11505
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/67"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Stanly County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64651 |
| Under 18 | 14002 |
| 18–64 | 38271 |
| 65+ | 12378 |
| Median household income | 60704 |
| Poverty rate | 15.25 |
| Homeownership rate | 74.45 |
| Unemployment rate | 4.05 |
| Median home value | 242400 |
| Gini index | 0.4312 |
| Vacancy rate | 11.85 |
| White | 51164 |
| Black | 7259 |
| Asian | 1222 |
| Native | 59 |
| Hispanic/Latino | 3685 |
| Bachelor's or higher | 11505 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 100% (congressional)
- [NC Senate District 33](/us/states/nc/districts/senate/33.md) — 100% (state senate)
- [NC House District 67](/us/states/nc/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
