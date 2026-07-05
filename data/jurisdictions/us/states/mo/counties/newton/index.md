---
type: Jurisdiction
title: "Newton County, MO"
classification: county
fips: "29145"
state: "MO"
demographics:
  population: 60118
  population_under_18: 14356
  population_18_64: 34434
  population_65_plus: 11328
  median_household_income: 66301
  poverty_rate: 13.48
  homeownership_rate: 76.62
  unemployment_rate: 5.92
  median_home_value: 190700
  gini_index: 0.4417
  vacancy_rate: 11.01
  race_white: 48846
  race_black: 567
  race_asian: 963
  race_native: 1019
  hispanic: 4058
  bachelors_plus: 12726
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/159"
    rel: in-district
    area_weight: 0.6076
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Newton County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60118 |
| Under 18 | 14356 |
| 18–64 | 34434 |
| 65+ | 11328 |
| Median household income | 66301 |
| Poverty rate | 13.48 |
| Homeownership rate | 76.62 |
| Unemployment rate | 5.92 |
| Median home value | 190700 |
| Gini index | 0.4417 |
| Vacancy rate | 11.01 |
| White | 48846 |
| Black | 567 |
| Asian | 963 |
| Native | 1019 |
| Hispanic/Latino | 4058 |
| Bachelor's or higher | 12726 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 32](/us/states/mo/districts/senate/32.md) — 100% (state senate)
- [MO House District 159](/us/states/mo/districts/house/159.md) — 61% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
