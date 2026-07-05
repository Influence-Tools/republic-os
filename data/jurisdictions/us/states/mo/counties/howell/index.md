---
type: Jurisdiction
title: "Howell County, MO"
classification: county
fips: "29091"
state: "MO"
demographics:
  population: 40383
  population_under_18: 9741
  population_18_64: 22596
  population_65_plus: 8046
  median_household_income: 50993
  poverty_rate: 20.31
  homeownership_rate: 70.3
  unemployment_rate: 4.98
  median_home_value: 173000
  gini_index: 0.4605
  vacancy_rate: 12.03
  race_white: 37171
  race_black: 216
  race_asian: 183
  race_native: 107
  hispanic: 1042
  bachelors_plus: 6833
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/154"
    rel: in-district
    area_weight: 0.9696
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.0303
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Howell County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40383 |
| Under 18 | 9741 |
| 18–64 | 22596 |
| 65+ | 8046 |
| Median household income | 50993 |
| Poverty rate | 20.31 |
| Homeownership rate | 70.3 |
| Unemployment rate | 4.98 |
| Median home value | 173000 |
| Gini index | 0.4605 |
| Vacancy rate | 12.03 |
| White | 37171 |
| Black | 216 |
| Asian | 183 |
| Native | 107 |
| Hispanic/Latino | 1042 |
| Bachelor's or higher | 6833 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 154](/us/states/mo/districts/house/154.md) — 97% (state house)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
