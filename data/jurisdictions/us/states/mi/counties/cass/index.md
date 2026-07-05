---
type: Jurisdiction
title: "Cass County, MI"
classification: county
fips: "26027"
state: "MI"
demographics:
  population: 51520
  population_under_18: 10397
  population_18_64: 29503
  population_65_plus: 11620
  median_household_income: 70443
  poverty_rate: 11.9
  homeownership_rate: 81.64
  unemployment_rate: 5.02
  median_home_value: 218000
  gini_index: 0.4628
  vacancy_rate: 17.42
  race_white: 43705
  race_black: 2110
  race_asian: 414
  race_native: 613
  hispanic: 2329
  bachelors_plus: 11093
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/36"
    rel: in-district
    area_weight: 0.6748
  - to: "us/states/mi/districts/house/37"
    rel: in-district
    area_weight: 0.3252
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Cass County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51520 |
| Under 18 | 10397 |
| 18–64 | 29503 |
| 65+ | 11620 |
| Median household income | 70443 |
| Poverty rate | 11.9 |
| Homeownership rate | 81.64 |
| Unemployment rate | 5.02 |
| Median home value | 218000 |
| Gini index | 0.4628 |
| Vacancy rate | 17.42 |
| White | 43705 |
| Black | 2110 |
| Asian | 414 |
| Native | 613 |
| Hispanic/Latino | 2329 |
| Bachelor's or higher | 11093 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 100% (state senate)
- [MI House District 36](/us/states/mi/districts/house/36.md) — 67% (state house)
- [MI House District 37](/us/states/mi/districts/house/37.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
