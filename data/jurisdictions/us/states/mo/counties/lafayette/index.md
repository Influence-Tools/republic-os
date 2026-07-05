---
type: Jurisdiction
title: "Lafayette County, MO"
classification: county
fips: "29107"
state: "MO"
demographics:
  population: 33115
  population_under_18: 7607
  population_18_64: 19115
  population_65_plus: 6393
  median_household_income: 80612
  poverty_rate: 9.29
  homeownership_rate: 75.75
  unemployment_rate: 3.05
  median_home_value: 216500
  gini_index: 0.3937
  vacancy_rate: 11.57
  race_white: 30066
  race_black: 514
  race_asian: 123
  race_native: 80
  hispanic: 1155
  bachelors_plus: 8210
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/51"
    rel: in-district
    area_weight: 0.6173
  - to: "us/states/mo/districts/house/53"
    rel: in-district
    area_weight: 0.3826
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Lafayette County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33115 |
| Under 18 | 7607 |
| 18–64 | 19115 |
| 65+ | 6393 |
| Median household income | 80612 |
| Poverty rate | 9.29 |
| Homeownership rate | 75.75 |
| Unemployment rate | 3.05 |
| Median home value | 216500 |
| Gini index | 0.3937 |
| Vacancy rate | 11.57 |
| White | 30066 |
| Black | 514 |
| Asian | 123 |
| Native | 80 |
| Hispanic/Latino | 1155 |
| Bachelor's or higher | 8210 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 100% (state senate)
- [MO House District 51](/us/states/mo/districts/house/51.md) — 62% (state house)
- [MO House District 53](/us/states/mo/districts/house/53.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
