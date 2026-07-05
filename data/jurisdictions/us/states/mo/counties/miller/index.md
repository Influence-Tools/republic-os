---
type: Jurisdiction
title: "Miller County, MO"
classification: county
fips: "29131"
state: "MO"
demographics:
  population: 25269
  population_under_18: 5869
  population_18_64: 14328
  population_65_plus: 5072
  median_household_income: 56736
  poverty_rate: 14.37
  homeownership_rate: 73.86
  unemployment_rate: 5.3
  median_home_value: 192600
  gini_index: 0.4496
  vacancy_rate: 21.4
  race_white: 23799
  race_black: 279
  race_asian: 96
  race_native: 33
  hispanic: 547
  bachelors_plus: 4544
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/124"
    rel: in-district
    area_weight: 0.8501
  - to: "us/states/mo/districts/house/61"
    rel: in-district
    area_weight: 0.1498
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Miller County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25269 |
| Under 18 | 5869 |
| 18–64 | 14328 |
| 65+ | 5072 |
| Median household income | 56736 |
| Poverty rate | 14.37 |
| Homeownership rate | 73.86 |
| Unemployment rate | 5.3 |
| Median home value | 192600 |
| Gini index | 0.4496 |
| Vacancy rate | 21.4 |
| White | 23799 |
| Black | 279 |
| Asian | 96 |
| Native | 33 |
| Hispanic/Latino | 547 |
| Bachelor's or higher | 4544 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 6](/us/states/mo/districts/senate/6.md) — 100% (state senate)
- [MO House District 124](/us/states/mo/districts/house/124.md) — 85% (state house)
- [MO House District 61](/us/states/mo/districts/house/61.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
