---
type: Jurisdiction
title: "Edgar County, IL"
classification: county
fips: "17045"
state: "IL"
demographics:
  population: 16535
  population_under_18: 3275
  population_18_64: 9180
  population_65_plus: 4080
  median_household_income: 59941
  poverty_rate: 12.0
  homeownership_rate: 72.67
  unemployment_rate: 4.37
  median_home_value: 97300
  gini_index: 0.4221
  vacancy_rate: 7.88
  race_white: 15863
  race_black: 108
  race_asian: 47
  race_native: 13
  hispanic: 252
  bachelors_plus: 3067
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Edgar County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16535 |
| Under 18 | 3275 |
| 18–64 | 9180 |
| 65+ | 4080 |
| Median household income | 59941 |
| Poverty rate | 12.0 |
| Homeownership rate | 72.67 |
| Unemployment rate | 4.37 |
| Median home value | 97300 |
| Gini index | 0.4221 |
| Vacancy rate | 7.88 |
| White | 15863 |
| Black | 108 |
| Asian | 47 |
| Native | 13 |
| Hispanic/Latino | 252 |
| Bachelor's or higher | 3067 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
