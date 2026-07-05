---
type: Jurisdiction
title: "James City County, VA"
classification: county
fips: "51095"
state: "VA"
demographics:
  population: 81013
  population_under_18: 15833
  population_18_64: 43318
  population_65_plus: 21862
  median_household_income: 109985
  poverty_rate: 6.84
  homeownership_rate: 76.72
  unemployment_rate: 2.75
  median_home_value: 447200
  gini_index: 0.4217
  vacancy_rate: 7.88
  race_white: 59107
  race_black: 10046
  race_asian: 2063
  race_native: 22
  hispanic: 5793
  bachelors_plus: 45261
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.8683
  - to: "us/states/va/districts/senate/26"
    rel: in-district
    area_weight: 0.8227
  - to: "us/states/va/districts/senate/24"
    rel: in-district
    area_weight: 0.0492
  - to: "us/states/va/districts/house/71"
    rel: in-district
    area_weight: 0.703
  - to: "us/states/va/districts/house/69"
    rel: in-district
    area_weight: 0.1689
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# James City County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 81013 |
| Under 18 | 15833 |
| 18–64 | 43318 |
| 65+ | 21862 |
| Median household income | 109985 |
| Poverty rate | 6.84 |
| Homeownership rate | 76.72 |
| Unemployment rate | 2.75 |
| Median home value | 447200 |
| Gini index | 0.4217 |
| Vacancy rate | 7.88 |
| White | 59107 |
| Black | 10046 |
| Asian | 2063 |
| Native | 22 |
| Hispanic/Latino | 5793 |
| Bachelor's or higher | 45261 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 87% (congressional)
- [VA Senate District 26](/us/states/va/districts/senate/26.md) — 82% (state senate)
- [VA Senate District 24](/us/states/va/districts/senate/24.md) — 5% (state senate)
- [VA House District 71](/us/states/va/districts/house/71.md) — 70% (state house)
- [VA House District 69](/us/states/va/districts/house/69.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
