---
type: Jurisdiction
title: "Grand County, CO"
classification: county
fips: "08049"
state: "CO"
demographics:
  population: 15895
  population_under_18: 2535
  population_18_64: 10035
  population_65_plus: 3325
  median_household_income: 88612
  poverty_rate: 7.57
  homeownership_rate: 73.43
  unemployment_rate: 4.12
  median_home_value: 601500
  gini_index: 0.4064
  vacancy_rate: 57.09
  race_white: 12503
  race_black: 33
  race_asian: 113
  race_native: 285
  hispanic: 1614
  bachelors_plus: 7160
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/13"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Grand County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15895 |
| Under 18 | 2535 |
| 18–64 | 10035 |
| 65+ | 3325 |
| Median household income | 88612 |
| Poverty rate | 7.57 |
| Homeownership rate | 73.43 |
| Unemployment rate | 4.12 |
| Median home value | 601500 |
| Gini index | 0.4064 |
| Vacancy rate | 57.09 |
| White | 12503 |
| Black | 33 |
| Asian | 113 |
| Native | 285 |
| Hispanic/Latino | 1614 |
| Bachelor's or higher | 7160 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
