---
type: Jurisdiction
title: "Mason County, TX"
classification: county
fips: "48319"
state: "TX"
demographics:
  population: 3955
  population_under_18: 758
  population_18_64: 1805
  population_65_plus: 1392
  median_household_income: 74180
  poverty_rate: 6.99
  homeownership_rate: 79.72
  unemployment_rate: 3.03
  median_home_value: 293600
  gini_index: 0.4008
  vacancy_rate: 29.59
  race_white: 3340
  race_black: 2
  race_asian: 8
  race_native: 0
  hispanic: 749
  bachelors_plus: 1591
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/53"
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

# Mason County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3955 |
| Under 18 | 758 |
| 18–64 | 1805 |
| 65+ | 1392 |
| Median household income | 74180 |
| Poverty rate | 6.99 |
| Homeownership rate | 79.72 |
| Unemployment rate | 3.03 |
| Median home value | 293600 |
| Gini index | 0.4008 |
| Vacancy rate | 29.59 |
| White | 3340 |
| Black | 2 |
| Asian | 8 |
| Native | 0 |
| Hispanic/Latino | 749 |
| Bachelor's or higher | 1591 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
