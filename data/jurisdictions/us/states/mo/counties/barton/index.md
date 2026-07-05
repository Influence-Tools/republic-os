---
type: Jurisdiction
title: "Barton County, MO"
classification: county
fips: "29011"
state: "MO"
demographics:
  population: 11690
  population_under_18: 2739
  population_18_64: 6450
  population_65_plus: 2501
  median_household_income: 51635
  poverty_rate: 20.18
  homeownership_rate: 68.12
  unemployment_rate: 3.26
  median_home_value: 136500
  gini_index: 0.4342
  vacancy_rate: 15.72
  race_white: 10659
  race_black: 27
  race_asian: 47
  race_native: 133
  hispanic: 357
  bachelors_plus: 1723
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/senate/20"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/127"
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

# Barton County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11690 |
| Under 18 | 2739 |
| 18–64 | 6450 |
| 65+ | 2501 |
| Median household income | 51635 |
| Poverty rate | 20.18 |
| Homeownership rate | 68.12 |
| Unemployment rate | 3.26 |
| Median home value | 136500 |
| Gini index | 0.4342 |
| Vacancy rate | 15.72 |
| White | 10659 |
| Black | 27 |
| Asian | 47 |
| Native | 133 |
| Hispanic/Latino | 357 |
| Bachelor's or higher | 1723 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 20](/us/states/mo/districts/senate/20.md) — 100% (state senate)
- [MO House District 127](/us/states/mo/districts/house/127.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
