---
type: Jurisdiction
title: "Upton County, TX"
classification: county
fips: "48461"
state: "TX"
demographics:
  population: 3191
  population_under_18: 751
  population_18_64: 1829
  population_65_plus: 611
  median_household_income: 49167
  poverty_rate: 16.04
  homeownership_rate: 77.21
  unemployment_rate: 3.53
  median_home_value: 109000
  gini_index: 0.445
  vacancy_rate: 19.19
  race_white: 1497
  race_black: 38
  race_asian: 36
  race_native: 5
  hispanic: 1747
  bachelors_plus: 249
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Upton County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3191 |
| Under 18 | 751 |
| 18–64 | 1829 |
| 65+ | 611 |
| Median household income | 49167 |
| Poverty rate | 16.04 |
| Homeownership rate | 77.21 |
| Unemployment rate | 3.53 |
| Median home value | 109000 |
| Gini index | 0.445 |
| Vacancy rate | 19.19 |
| White | 1497 |
| Black | 38 |
| Asian | 36 |
| Native | 5 |
| Hispanic/Latino | 1747 |
| Bachelor's or higher | 249 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
