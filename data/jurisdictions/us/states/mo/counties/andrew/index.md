---
type: Jurisdiction
title: "Andrew County, MO"
classification: county
fips: "29003"
state: "MO"
demographics:
  population: 18065
  population_under_18: 4052
  population_18_64: 10211
  population_65_plus: 3802
  median_household_income: 75625
  poverty_rate: 6.19
  homeownership_rate: 76.72
  unemployment_rate: 3.57
  median_home_value: 215400
  gini_index: 0.3997
  vacancy_rate: 7.54
  race_white: 16854
  race_black: 242
  race_asian: 146
  race_native: 8
  hispanic: 470
  bachelors_plus: 5068
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/9"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Andrew County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18065 |
| Under 18 | 4052 |
| 18–64 | 10211 |
| 65+ | 3802 |
| Median household income | 75625 |
| Poverty rate | 6.19 |
| Homeownership rate | 76.72 |
| Unemployment rate | 3.57 |
| Median home value | 215400 |
| Gini index | 0.3997 |
| Vacancy rate | 7.54 |
| White | 16854 |
| Black | 242 |
| Asian | 146 |
| Native | 8 |
| Hispanic/Latino | 470 |
| Bachelor's or higher | 5068 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 9](/us/states/mo/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
