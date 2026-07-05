---
type: Jurisdiction
title: "Monroe County, AR"
classification: county
fips: "05095"
state: "AR"
demographics:
  population: 6589
  population_under_18: 1552
  population_18_64: 3491
  population_65_plus: 1546
  median_household_income: 43214
  poverty_rate: 20.57
  homeownership_rate: 62.58
  unemployment_rate: 9.83
  median_home_value: 88700
  gini_index: 0.4804
  vacancy_rate: 27.14
  race_white: 3519
  race_black: 2651
  race_asian: 48
  race_native: 0
  hispanic: 193
  bachelors_plus: 721
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.5594
  - to: "us/states/ar/districts/house/61"
    rel: in-district
    area_weight: 0.4406
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Monroe County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6589 |
| Under 18 | 1552 |
| 18–64 | 3491 |
| 65+ | 1546 |
| Median household income | 43214 |
| Poverty rate | 20.57 |
| Homeownership rate | 62.58 |
| Unemployment rate | 9.83 |
| Median home value | 88700 |
| Gini index | 0.4804 |
| Vacancy rate | 27.14 |
| White | 3519 |
| Black | 2651 |
| Asian | 48 |
| Native | 0 |
| Hispanic/Latino | 193 |
| Bachelor's or higher | 721 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 100% (state senate)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 56% (state house)
- [AR House District 61](/us/states/ar/districts/house/61.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
