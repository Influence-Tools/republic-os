---
type: Jurisdiction
title: "Inyo County, CA"
classification: county
fips: "06027"
state: "CA"
demographics:
  population: 18739
  population_under_18: 3781
  population_18_64: 10283
  population_65_plus: 4675
  median_household_income: 73991
  poverty_rate: 10.88
  homeownership_rate: 66.41
  unemployment_rate: 2.48
  median_home_value: 348700
  gini_index: 0.4459
  vacancy_rate: 15.58
  race_white: 11541
  race_black: 98
  race_asian: 279
  race_native: 2113
  hispanic: 4529
  bachelors_plus: 6057
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/8"
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

# Inyo County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18739 |
| Under 18 | 3781 |
| 18–64 | 10283 |
| 65+ | 4675 |
| Median household income | 73991 |
| Poverty rate | 10.88 |
| Homeownership rate | 66.41 |
| Unemployment rate | 2.48 |
| Median home value | 348700 |
| Gini index | 0.4459 |
| Vacancy rate | 15.58 |
| White | 11541 |
| Black | 98 |
| Asian | 279 |
| Native | 2113 |
| Hispanic/Latino | 4529 |
| Bachelor's or higher | 6057 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
