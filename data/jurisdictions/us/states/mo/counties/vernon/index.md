---
type: Jurisdiction
title: "Vernon County, MO"
classification: county
fips: "29217"
state: "MO"
demographics:
  population: 19687
  population_under_18: 4694
  population_18_64: 10945
  population_65_plus: 4048
  median_household_income: 52230
  poverty_rate: 18.79
  homeownership_rate: 71.29
  unemployment_rate: 4.22
  median_home_value: 158800
  gini_index: 0.4049
  vacancy_rate: 13.15
  race_white: 18326
  race_black: 177
  race_asian: 155
  race_native: 24
  hispanic: 533
  bachelors_plus: 3026
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/125"
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

# Vernon County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19687 |
| Under 18 | 4694 |
| 18–64 | 10945 |
| 65+ | 4048 |
| Median household income | 52230 |
| Poverty rate | 18.79 |
| Homeownership rate | 71.29 |
| Unemployment rate | 4.22 |
| Median home value | 158800 |
| Gini index | 0.4049 |
| Vacancy rate | 13.15 |
| White | 18326 |
| Black | 177 |
| Asian | 155 |
| Native | 24 |
| Hispanic/Latino | 533 |
| Bachelor's or higher | 3026 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 125](/us/states/mo/districts/house/125.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
