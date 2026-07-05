---
type: Jurisdiction
title: "Daviess County, MO"
classification: county
fips: "29061"
state: "MO"
demographics:
  population: 8477
  population_under_18: 2101
  population_18_64: 4538
  population_65_plus: 1838
  median_household_income: 63984
  poverty_rate: 11.44
  homeownership_rate: 79.14
  unemployment_rate: 1.38
  median_home_value: 161800
  gini_index: 0.4459
  vacancy_rate: 26.73
  race_white: 8101
  race_black: 82
  race_asian: 18
  race_native: 10
  hispanic: 151
  bachelors_plus: 1453
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/2"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Daviess County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8477 |
| Under 18 | 2101 |
| 18–64 | 4538 |
| 65+ | 1838 |
| Median household income | 63984 |
| Poverty rate | 11.44 |
| Homeownership rate | 79.14 |
| Unemployment rate | 1.38 |
| Median home value | 161800 |
| Gini index | 0.4459 |
| Vacancy rate | 26.73 |
| White | 8101 |
| Black | 82 |
| Asian | 18 |
| Native | 10 |
| Hispanic/Latino | 151 |
| Bachelor's or higher | 1453 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 2](/us/states/mo/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
