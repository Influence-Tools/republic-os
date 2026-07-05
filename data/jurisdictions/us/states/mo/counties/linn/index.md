---
type: Jurisdiction
title: "Linn County, MO"
classification: county
fips: "29115"
state: "MO"
demographics:
  population: 11852
  population_under_18: 2764
  population_18_64: 6508
  population_65_plus: 2580
  median_household_income: 61635
  poverty_rate: 13.74
  homeownership_rate: 78.53
  unemployment_rate: 3.15
  median_home_value: 123300
  gini_index: 0.4362
  vacancy_rate: 19.82
  race_white: 11194
  race_black: 97
  race_asian: 52
  race_native: 33
  hispanic: 352
  bachelors_plus: 2205
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/7"
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

# Linn County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11852 |
| Under 18 | 2764 |
| 18–64 | 6508 |
| 65+ | 2580 |
| Median household income | 61635 |
| Poverty rate | 13.74 |
| Homeownership rate | 78.53 |
| Unemployment rate | 3.15 |
| Median home value | 123300 |
| Gini index | 0.4362 |
| Vacancy rate | 19.82 |
| White | 11194 |
| Black | 97 |
| Asian | 52 |
| Native | 33 |
| Hispanic/Latino | 352 |
| Bachelor's or higher | 2205 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 7](/us/states/mo/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
