---
type: Jurisdiction
title: "Seneca County, NY"
classification: county
fips: "36099"
state: "NY"
demographics:
  population: 32920
  population_under_18: 6682
  population_18_64: 19134
  population_65_plus: 7104
  median_household_income: 68089
  poverty_rate: 13.47
  homeownership_rate: 70.95
  unemployment_rate: 4.52
  median_home_value: 155400
  gini_index: 0.4604
  vacancy_rate: 15.98
  race_white: 29103
  race_black: 1234
  race_asian: 201
  race_native: 36
  hispanic: 1436
  bachelors_plus: 8246
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/132"
    rel: in-district
    area_weight: 0.545
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.4549
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Seneca County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32920 |
| Under 18 | 6682 |
| 18–64 | 19134 |
| 65+ | 7104 |
| Median household income | 68089 |
| Poverty rate | 13.47 |
| Homeownership rate | 70.95 |
| Unemployment rate | 4.52 |
| Median home value | 155400 |
| Gini index | 0.4604 |
| Vacancy rate | 15.98 |
| White | 29103 |
| Black | 1234 |
| Asian | 201 |
| Native | 36 |
| Hispanic/Latino | 1436 |
| Bachelor's or higher | 8246 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 100% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 132](/us/states/ny/districts/house/132.md) — 55% (state house)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
