---
type: Jurisdiction
title: "Pike County, MO"
classification: county
fips: "29163"
state: "MO"
demographics:
  population: 17711
  population_under_18: 3977
  population_18_64: 10357
  population_65_plus: 3377
  median_household_income: 54989
  poverty_rate: 15.97
  homeownership_rate: 73.3
  unemployment_rate: 3.94
  median_home_value: 146000
  gini_index: 0.4328
  vacancy_rate: 15.7
  race_white: 15843
  race_black: 878
  race_asian: 60
  race_native: 84
  hispanic: 439
  bachelors_plus: 2749
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Pike County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17711 |
| Under 18 | 3977 |
| 18–64 | 10357 |
| 65+ | 3377 |
| Median household income | 54989 |
| Poverty rate | 15.97 |
| Homeownership rate | 73.3 |
| Unemployment rate | 3.94 |
| Median home value | 146000 |
| Gini index | 0.4328 |
| Vacancy rate | 15.7 |
| White | 15843 |
| Black | 878 |
| Asian | 60 |
| Native | 84 |
| Hispanic/Latino | 439 |
| Bachelor's or higher | 2749 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 10](/us/states/mo/districts/senate/10.md) — 100% (state senate)
- [MO House District 40](/us/states/mo/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
