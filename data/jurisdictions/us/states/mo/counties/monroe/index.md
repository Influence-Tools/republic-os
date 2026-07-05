---
type: Jurisdiction
title: "Monroe County, MO"
classification: county
fips: "29137"
state: "MO"
demographics:
  population: 8734
  population_under_18: 1916
  population_18_64: 4638
  population_65_plus: 2180
  median_household_income: 54516
  poverty_rate: 14.18
  homeownership_rate: 74.31
  unemployment_rate: 1.78
  median_home_value: 149300
  gini_index: 0.4411
  vacancy_rate: 22.36
  race_white: 8101
  race_black: 309
  race_asian: 34
  race_native: 37
  hispanic: 160
  bachelors_plus: 1442
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/43"
    rel: in-district
    area_weight: 0.8587
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.1411
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Monroe County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8734 |
| Under 18 | 1916 |
| 18–64 | 4638 |
| 65+ | 2180 |
| Median household income | 54516 |
| Poverty rate | 14.18 |
| Homeownership rate | 74.31 |
| Unemployment rate | 1.78 |
| Median home value | 149300 |
| Gini index | 0.4411 |
| Vacancy rate | 22.36 |
| White | 8101 |
| Black | 309 |
| Asian | 34 |
| Native | 37 |
| Hispanic/Latino | 160 |
| Bachelor's or higher | 1442 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 43](/us/states/mo/districts/house/43.md) — 86% (state house)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
