---
type: Jurisdiction
title: "Clear Creek County, CO"
classification: county
fips: "08019"
state: "CO"
demographics:
  population: 9262
  population_under_18: 1370
  population_18_64: 5790
  population_65_plus: 2102
  median_household_income: 94577
  poverty_rate: 6.39
  homeownership_rate: 81.61
  unemployment_rate: 4.8
  median_home_value: 608500
  gini_index: 0.4582
  vacancy_rate: 19.56
  race_white: 8089
  race_black: 10
  race_asian: 170
  race_native: 106
  hispanic: 722
  bachelors_plus: 6217
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/co/districts/house/49"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Clear Creek County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9262 |
| Under 18 | 1370 |
| 18–64 | 5790 |
| 65+ | 2102 |
| Median household income | 94577 |
| Poverty rate | 6.39 |
| Homeownership rate | 81.61 |
| Unemployment rate | 4.8 |
| Median home value | 608500 |
| Gini index | 0.4582 |
| Vacancy rate | 19.56 |
| White | 8089 |
| Black | 10 |
| Asian | 170 |
| Native | 106 |
| Hispanic/Latino | 722 |
| Bachelor's or higher | 6217 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 49](/us/states/co/districts/house/49.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
