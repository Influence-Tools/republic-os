---
type: Jurisdiction
title: "Morgan County, MO"
classification: county
fips: "29141"
state: "MO"
demographics:
  population: 21717
  population_under_18: 4958
  population_18_64: 11548
  population_65_plus: 5211
  median_household_income: 53412
  poverty_rate: 18.32
  homeownership_rate: 79.68
  unemployment_rate: 2.89
  median_home_value: 194400
  gini_index: 0.5132
  vacancy_rate: 42.68
  race_white: 20126
  race_black: 51
  race_asian: 78
  race_native: 11
  hispanic: 569
  bachelors_plus: 3404
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/58"
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

# Morgan County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21717 |
| Under 18 | 4958 |
| 18–64 | 11548 |
| 65+ | 5211 |
| Median household income | 53412 |
| Poverty rate | 18.32 |
| Homeownership rate | 79.68 |
| Unemployment rate | 2.89 |
| Median home value | 194400 |
| Gini index | 0.5132 |
| Vacancy rate | 42.68 |
| White | 20126 |
| Black | 51 |
| Asian | 78 |
| Native | 11 |
| Hispanic/Latino | 569 |
| Bachelor's or higher | 3404 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 6](/us/states/mo/districts/senate/6.md) — 100% (state senate)
- [MO House District 58](/us/states/mo/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
