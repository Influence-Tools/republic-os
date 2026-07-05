---
type: Jurisdiction
title: "Duplin County, NC"
classification: county
fips: "37061"
state: "NC"
demographics:
  population: 49335
  population_under_18: 11708
  population_18_64: 27812
  population_65_plus: 9815
  median_household_income: 55148
  poverty_rate: 20.46
  homeownership_rate: 70.34
  unemployment_rate: 5.32
  median_home_value: 137400
  gini_index: 0.4336
  vacancy_rate: 12.88
  race_white: 26427
  race_black: 10934
  race_asian: 288
  race_native: 273
  hispanic: 11496
  bachelors_plus: 7506
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/nc/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nc/districts/house/4"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Duplin County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49335 |
| Under 18 | 11708 |
| 18–64 | 27812 |
| 65+ | 9815 |
| Median household income | 55148 |
| Poverty rate | 20.46 |
| Homeownership rate | 70.34 |
| Unemployment rate | 5.32 |
| Median home value | 137400 |
| Gini index | 0.4336 |
| Vacancy rate | 12.88 |
| White | 26427 |
| Black | 10934 |
| Asian | 288 |
| Native | 273 |
| Hispanic/Latino | 11496 |
| Bachelor's or higher | 7506 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 100% (congressional)
- [NC Senate District 9](/us/states/nc/districts/senate/9.md) — 100% (state senate)
- [NC House District 4](/us/states/nc/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
