---
type: Jurisdiction
title: "Alamosa County, CO"
classification: county
fips: "08003"
state: "CO"
demographics:
  population: 16581
  population_under_18: 3939
  population_18_64: 10135
  population_65_plus: 2507
  median_household_income: 55397
  poverty_rate: 17.22
  homeownership_rate: 55.94
  unemployment_rate: 3.66
  median_home_value: 239100
  gini_index: 0.4585
  vacancy_rate: 8.19
  race_white: 9586
  race_black: 309
  race_asian: 188
  race_native: 681
  hispanic: 7989
  bachelors_plus: 4834
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Alamosa County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16581 |
| Under 18 | 3939 |
| 18–64 | 10135 |
| 65+ | 2507 |
| Median household income | 55397 |
| Poverty rate | 17.22 |
| Homeownership rate | 55.94 |
| Unemployment rate | 3.66 |
| Median home value | 239100 |
| Gini index | 0.4585 |
| Vacancy rate | 8.19 |
| White | 9586 |
| Black | 309 |
| Asian | 188 |
| Native | 681 |
| Hispanic/Latino | 7989 |
| Bachelor's or higher | 4834 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
