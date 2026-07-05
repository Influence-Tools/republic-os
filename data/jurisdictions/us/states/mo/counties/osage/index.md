---
type: Jurisdiction
title: "Osage County, MO"
classification: county
fips: "29151"
state: "MO"
demographics:
  population: 13402
  population_under_18: 3043
  population_18_64: 7910
  population_65_plus: 2449
  median_household_income: 76681
  poverty_rate: 8.61
  homeownership_rate: 79.42
  unemployment_rate: 1.69
  median_home_value: 223300
  gini_index: 0.4835
  vacancy_rate: 18.67
  race_white: 13061
  race_black: 37
  race_asian: 14
  race_native: 24
  hispanic: 149
  bachelors_plus: 2927
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/61"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Osage County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13402 |
| Under 18 | 3043 |
| 18–64 | 7910 |
| 65+ | 2449 |
| Median household income | 76681 |
| Poverty rate | 8.61 |
| Homeownership rate | 79.42 |
| Unemployment rate | 1.69 |
| Median home value | 223300 |
| Gini index | 0.4835 |
| Vacancy rate | 18.67 |
| White | 13061 |
| Black | 37 |
| Asian | 14 |
| Native | 24 |
| Hispanic/Latino | 149 |
| Bachelor's or higher | 2927 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 26](/us/states/mo/districts/senate/26.md) — 100% (state senate)
- [MO House District 61](/us/states/mo/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
