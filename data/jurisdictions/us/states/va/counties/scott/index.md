---
type: Jurisdiction
title: "Scott County, VA"
classification: county
fips: "51169"
state: "VA"
demographics:
  population: 21479
  population_under_18: 4197
  population_18_64: 5903
  population_65_plus: 11379
  median_household_income: 46349
  poverty_rate: 20.2
  homeownership_rate: 77.01
  unemployment_rate: 2.83
  median_home_value: 143000
  gini_index: 0.4761
  vacancy_rate: 22.52
  race_white: 20570
  race_black: 274
  race_asian: 15
  race_native: 5
  hispanic: 329
  bachelors_plus: 3393
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/45"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Scott County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21479 |
| Under 18 | 4197 |
| 18–64 | 5903 |
| 65+ | 11379 |
| Median household income | 46349 |
| Poverty rate | 20.2 |
| Homeownership rate | 77.01 |
| Unemployment rate | 2.83 |
| Median home value | 143000 |
| Gini index | 0.4761 |
| Vacancy rate | 22.52 |
| White | 20570 |
| Black | 274 |
| Asian | 15 |
| Native | 5 |
| Hispanic/Latino | 329 |
| Bachelor's or higher | 3393 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 45](/us/states/va/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
