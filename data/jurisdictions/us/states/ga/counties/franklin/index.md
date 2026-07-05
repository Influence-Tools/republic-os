---
type: Jurisdiction
title: "Franklin County, GA"
classification: county
fips: "13119"
state: "GA"
demographics:
  population: 24234
  population_under_18: 5381
  population_18_64: 14219
  population_65_plus: 4634
  median_household_income: 53046
  poverty_rate: 19.52
  homeownership_rate: 77.15
  unemployment_rate: 5.9
  median_home_value: 179000
  gini_index: 0.4959
  vacancy_rate: 17.52
  race_white: 19770
  race_black: 2134
  race_asian: 429
  race_native: 48
  hispanic: 1319
  bachelors_plus: 4207
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/33"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Franklin County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24234 |
| Under 18 | 5381 |
| 18–64 | 14219 |
| 65+ | 4634 |
| Median household income | 53046 |
| Poverty rate | 19.52 |
| Homeownership rate | 77.15 |
| Unemployment rate | 5.9 |
| Median home value | 179000 |
| Gini index | 0.4959 |
| Vacancy rate | 17.52 |
| White | 19770 |
| Black | 2134 |
| Asian | 429 |
| Native | 48 |
| Hispanic/Latino | 1319 |
| Bachelor's or higher | 4207 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 33](/us/states/ga/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
