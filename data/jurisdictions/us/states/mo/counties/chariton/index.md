---
type: Jurisdiction
title: "Chariton County, MO"
classification: county
fips: "29041"
state: "MO"
demographics:
  population: 7390
  population_under_18: 1718
  population_18_64: 3832
  population_65_plus: 1840
  median_household_income: 71520
  poverty_rate: 8.78
  homeownership_rate: 83.48
  unemployment_rate: 3.48
  median_home_value: 160900
  gini_index: 0.4145
  vacancy_rate: 29.22
  race_white: 6892
  race_black: 140
  race_asian: 14
  race_native: 47
  hispanic: 111
  bachelors_plus: 1572
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/48"
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

# Chariton County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7390 |
| Under 18 | 1718 |
| 18–64 | 3832 |
| 65+ | 1840 |
| Median household income | 71520 |
| Poverty rate | 8.78 |
| Homeownership rate | 83.48 |
| Unemployment rate | 3.48 |
| Median home value | 160900 |
| Gini index | 0.4145 |
| Vacancy rate | 29.22 |
| White | 6892 |
| Black | 140 |
| Asian | 14 |
| Native | 47 |
| Hispanic/Latino | 111 |
| Bachelor's or higher | 1572 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 48](/us/states/mo/districts/house/48.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
