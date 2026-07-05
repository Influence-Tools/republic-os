---
type: Jurisdiction
title: "Ozark County, MO"
classification: county
fips: "29153"
state: "MO"
demographics:
  population: 8873
  population_under_18: 1687
  population_18_64: 4583
  population_65_plus: 2603
  median_household_income: 44163
  poverty_rate: 21.47
  homeownership_rate: 82.1
  unemployment_rate: 5.0
  median_home_value: 168600
  gini_index: 0.5115
  vacancy_rate: 26.26
  race_white: 8333
  race_black: 24
  race_asian: 0
  race_native: 6
  hispanic: 188
  bachelors_plus: 1414
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/155"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Ozark County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8873 |
| Under 18 | 1687 |
| 18–64 | 4583 |
| 65+ | 2603 |
| Median household income | 44163 |
| Poverty rate | 21.47 |
| Homeownership rate | 82.1 |
| Unemployment rate | 5.0 |
| Median home value | 168600 |
| Gini index | 0.5115 |
| Vacancy rate | 26.26 |
| White | 8333 |
| Black | 24 |
| Asian | 0 |
| Native | 6 |
| Hispanic/Latino | 188 |
| Bachelor's or higher | 1414 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 155](/us/states/mo/districts/house/155.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
