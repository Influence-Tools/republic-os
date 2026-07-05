---
type: Jurisdiction
title: "Phillips County, CO"
classification: county
fips: "08095"
state: "CO"
demographics:
  population: 4496
  population_under_18: 1145
  population_18_64: 2427
  population_65_plus: 924
  median_household_income: 64674
  poverty_rate: 16.84
  homeownership_rate: 71.88
  unemployment_rate: 2.92
  median_home_value: 258200
  gini_index: 0.5407
  vacancy_rate: 9.8
  race_white: 3516
  race_black: 0
  race_asian: 6
  race_native: 72
  hispanic: 1298
  bachelors_plus: 1336
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Phillips County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4496 |
| Under 18 | 1145 |
| 18–64 | 2427 |
| 65+ | 924 |
| Median household income | 64674 |
| Poverty rate | 16.84 |
| Homeownership rate | 71.88 |
| Unemployment rate | 2.92 |
| Median home value | 258200 |
| Gini index | 0.5407 |
| Vacancy rate | 9.8 |
| White | 3516 |
| Black | 0 |
| Asian | 6 |
| Native | 72 |
| Hispanic/Latino | 1298 |
| Bachelor's or higher | 1336 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
