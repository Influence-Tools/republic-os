---
type: Jurisdiction
title: "Throckmorton County, TX"
classification: county
fips: "48447"
state: "TX"
demographics:
  population: 1639
  population_under_18: 347
  population_18_64: 858
  population_65_plus: 434
  median_household_income: 59216
  poverty_rate: 24.22
  homeownership_rate: 67.98
  unemployment_rate: 8.25
  median_home_value: 89500
  gini_index: 0.4722
  vacancy_rate: 25.63
  race_white: 1456
  race_black: 0
  race_asian: 13
  race_native: 0
  hispanic: 168
  bachelors_plus: 345
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Throckmorton County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1639 |
| Under 18 | 347 |
| 18–64 | 858 |
| 65+ | 434 |
| Median household income | 59216 |
| Poverty rate | 24.22 |
| Homeownership rate | 67.98 |
| Unemployment rate | 8.25 |
| Median home value | 89500 |
| Gini index | 0.4722 |
| Vacancy rate | 25.63 |
| White | 1456 |
| Black | 0 |
| Asian | 13 |
| Native | 0 |
| Hispanic/Latino | 168 |
| Bachelor's or higher | 345 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
