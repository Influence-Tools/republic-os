---
type: Jurisdiction
title: "Newton County, TX"
classification: county
fips: "48351"
state: "TX"
demographics:
  population: 12093
  population_under_18: 2323
  population_18_64: 6931
  population_65_plus: 2839
  median_household_income: 42618
  poverty_rate: 18.96
  homeownership_rate: 82.85
  unemployment_rate: 8.26
  median_home_value: 103100
  gini_index: 0.4824
  vacancy_rate: 25.43
  race_white: 9019
  race_black: 2097
  race_asian: 86
  race_native: 111
  hispanic: 439
  bachelors_plus: 816
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.005
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/tx/districts/house/11"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Newton County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12093 |
| Under 18 | 2323 |
| 18–64 | 6931 |
| 65+ | 2839 |
| Median household income | 42618 |
| Poverty rate | 18.96 |
| Homeownership rate | 82.85 |
| Unemployment rate | 8.26 |
| Median home value | 103100 |
| Gini index | 0.4824 |
| Vacancy rate | 25.43 |
| White | 9019 |
| Black | 2097 |
| Asian | 86 |
| Native | 111 |
| Hispanic/Latino | 439 |
| Bachelor's or higher | 816 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 99% (congressional)
- [LA-04](/us/states/la/districts/04.md) — 0% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
