---
type: Jurisdiction
title: "Kiowa County, CO"
classification: county
fips: "08061"
state: "CO"
demographics:
  population: 1376
  population_under_18: 298
  population_18_64: 775
  population_65_plus: 303
  median_household_income: 58618
  poverty_rate: 11.81
  homeownership_rate: 68.72
  unemployment_rate: 0.14
  median_home_value: 161500
  gini_index: 0.4272
  vacancy_rate: 20.95
  race_white: 1219
  race_black: 0
  race_asian: 20
  race_native: 6
  hispanic: 178
  bachelors_plus: 271
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Kiowa County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1376 |
| Under 18 | 298 |
| 18–64 | 775 |
| 65+ | 303 |
| Median household income | 58618 |
| Poverty rate | 11.81 |
| Homeownership rate | 68.72 |
| Unemployment rate | 0.14 |
| Median home value | 161500 |
| Gini index | 0.4272 |
| Vacancy rate | 20.95 |
| White | 1219 |
| Black | 0 |
| Asian | 20 |
| Native | 6 |
| Hispanic/Latino | 178 |
| Bachelor's or higher | 271 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
