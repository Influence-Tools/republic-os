---
type: Jurisdiction
title: "Pontotoc County, OK"
classification: county
fips: "40123"
state: "OK"
demographics:
  population: 38235
  population_under_18: 9550
  population_18_64: 22181
  population_65_plus: 6504
  median_household_income: 63017
  poverty_rate: 12.57
  homeownership_rate: 66.01
  unemployment_rate: 3.66
  median_home_value: 175400
  gini_index: 0.4245
  vacancy_rate: 13.67
  race_white: 24372
  race_black: 960
  race_asian: 416
  race_native: 6978
  hispanic: 2503
  bachelors_plus: 10598
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/ok/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/25"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Pontotoc County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38235 |
| Under 18 | 9550 |
| 18–64 | 22181 |
| 65+ | 6504 |
| Median household income | 63017 |
| Poverty rate | 12.57 |
| Homeownership rate | 66.01 |
| Unemployment rate | 3.66 |
| Median home value | 175400 |
| Gini index | 0.4245 |
| Vacancy rate | 13.67 |
| White | 24372 |
| Black | 960 |
| Asian | 416 |
| Native | 6978 |
| Hispanic/Latino | 2503 |
| Bachelor's or higher | 10598 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 13](/us/states/ok/districts/senate/13.md) — 100% (state senate)
- [OK House District 25](/us/states/ok/districts/house/25.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
