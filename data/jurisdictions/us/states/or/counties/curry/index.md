---
type: Jurisdiction
title: "Curry County, OR"
classification: county
fips: "41015"
state: "OR"
demographics:
  population: 23381
  population_under_18: 3290
  population_18_64: 11521
  population_65_plus: 8570
  median_household_income: 62244
  poverty_rate: 15.21
  homeownership_rate: 74.16
  unemployment_rate: 5.76
  median_home_value: 381300
  gini_index: 0.4335
  vacancy_rate: 15.56
  race_white: 19620
  race_black: 5
  race_asian: 217
  race_native: 298
  hispanic: 1809
  bachelors_plus: 5817
districts:
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.8196
  - to: "us/states/or/districts/senate/1"
    rel: in-district
    area_weight: 0.8223
  - to: "us/states/or/districts/house/1"
    rel: in-district
    area_weight: 0.8223
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Curry County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23381 |
| Under 18 | 3290 |
| 18–64 | 11521 |
| 65+ | 8570 |
| Median household income | 62244 |
| Poverty rate | 15.21 |
| Homeownership rate | 74.16 |
| Unemployment rate | 5.76 |
| Median home value | 381300 |
| Gini index | 0.4335 |
| Vacancy rate | 15.56 |
| White | 19620 |
| Black | 5 |
| Asian | 217 |
| Native | 298 |
| Hispanic/Latino | 1809 |
| Bachelor's or higher | 5817 |

## Districts

- [OR-04](/us/states/or/districts/04.md) — 82% (congressional)
- [OR Senate District 1](/us/states/or/districts/senate/1.md) — 82% (state senate)
- [OR House District 1](/us/states/or/districts/house/1.md) — 82% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
