---
type: Jurisdiction
title: "Lincoln County, CO"
classification: county
fips: "08073"
state: "CO"
demographics:
  population: 5550
  population_under_18: 964
  population_18_64: 3572
  population_65_plus: 1014
  median_household_income: 62861
  poverty_rate: 9.82
  homeownership_rate: 71.74
  unemployment_rate: 1.4
  median_home_value: 246500
  gini_index: 0.4494
  vacancy_rate: 17.25
  race_white: 4346
  race_black: 304
  race_asian: 5
  race_native: 73
  hispanic: 845
  bachelors_plus: 1266
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/56"
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

# Lincoln County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5550 |
| Under 18 | 964 |
| 18–64 | 3572 |
| 65+ | 1014 |
| Median household income | 62861 |
| Poverty rate | 9.82 |
| Homeownership rate | 71.74 |
| Unemployment rate | 1.4 |
| Median home value | 246500 |
| Gini index | 0.4494 |
| Vacancy rate | 17.25 |
| White | 4346 |
| Black | 304 |
| Asian | 5 |
| Native | 73 |
| Hispanic/Latino | 845 |
| Bachelor's or higher | 1266 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 56](/us/states/co/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
