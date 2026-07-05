---
type: Jurisdiction
title: "Mercer County, MO"
classification: county
fips: "29129"
state: "MO"
demographics:
  population: 3482
  population_under_18: 854
  population_18_64: 1851
  population_65_plus: 777
  median_household_income: 62679
  poverty_rate: 13.46
  homeownership_rate: 81.03
  unemployment_rate: 3.46
  median_home_value: 104900
  gini_index: 0.3875
  vacancy_rate: 31.55
  race_white: 3218
  race_black: 6
  race_asian: 31
  race_native: 23
  hispanic: 167
  bachelors_plus: 557
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/3"
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

# Mercer County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3482 |
| Under 18 | 854 |
| 18–64 | 1851 |
| 65+ | 777 |
| Median household income | 62679 |
| Poverty rate | 13.46 |
| Homeownership rate | 81.03 |
| Unemployment rate | 3.46 |
| Median home value | 104900 |
| Gini index | 0.3875 |
| Vacancy rate | 31.55 |
| White | 3218 |
| Black | 6 |
| Asian | 31 |
| Native | 23 |
| Hispanic/Latino | 167 |
| Bachelor's or higher | 557 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 3](/us/states/mo/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
