---
type: Jurisdiction
title: "Glenn County, CA"
classification: county
fips: "06021"
state: "CA"
demographics:
  population: 28494
  population_under_18: 7622
  population_18_64: 15979
  population_65_plus: 4893
  median_household_income: 67139
  poverty_rate: 15.95
  homeownership_rate: 61.18
  unemployment_rate: 8.02
  median_home_value: 352400
  gini_index: 0.434
  vacancy_rate: 11.41
  race_white: 15749
  race_black: 62
  race_asian: 856
  race_native: 434
  hispanic: 12820
  bachelors_plus: 3333
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Glenn County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28494 |
| Under 18 | 7622 |
| 18–64 | 15979 |
| 65+ | 4893 |
| Median household income | 67139 |
| Poverty rate | 15.95 |
| Homeownership rate | 61.18 |
| Unemployment rate | 8.02 |
| Median home value | 352400 |
| Gini index | 0.434 |
| Vacancy rate | 11.41 |
| White | 15749 |
| Black | 62 |
| Asian | 856 |
| Native | 434 |
| Hispanic/Latino | 12820 |
| Bachelor's or higher | 3333 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
