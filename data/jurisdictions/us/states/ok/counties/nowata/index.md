---
type: Jurisdiction
title: "Nowata County, OK"
classification: county
fips: "40105"
state: "OK"
demographics:
  population: 9435
  population_under_18: 2171
  population_18_64: 5383
  population_65_plus: 1881
  median_household_income: 54333
  poverty_rate: 17.22
  homeownership_rate: 73.55
  unemployment_rate: 4.52
  median_home_value: 137800
  gini_index: 0.4657
  vacancy_rate: 15.5
  race_white: 6174
  race_black: 165
  race_asian: 66
  race_native: 1475
  hispanic: 300
  bachelors_plus: 1403
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/10"
    rel: in-district
    area_weight: 0.7258
  - to: "us/states/ok/districts/house/6"
    rel: in-district
    area_weight: 0.2741
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Nowata County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9435 |
| Under 18 | 2171 |
| 18–64 | 5383 |
| 65+ | 1881 |
| Median household income | 54333 |
| Poverty rate | 17.22 |
| Homeownership rate | 73.55 |
| Unemployment rate | 4.52 |
| Median home value | 137800 |
| Gini index | 0.4657 |
| Vacancy rate | 15.5 |
| White | 6174 |
| Black | 165 |
| Asian | 66 |
| Native | 1475 |
| Hispanic/Latino | 300 |
| Bachelor's or higher | 1403 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 29](/us/states/ok/districts/senate/29.md) — 100% (state senate)
- [OK House District 10](/us/states/ok/districts/house/10.md) — 73% (state house)
- [OK House District 6](/us/states/ok/districts/house/6.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
