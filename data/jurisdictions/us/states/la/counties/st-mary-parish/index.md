---
type: Jurisdiction
title: "St. Mary Parish, LA"
classification: county
fips: "22101"
state: "LA"
demographics:
  population: 47828
  population_under_18: 11697
  population_18_64: 27360
  population_65_plus: 8771
  median_household_income: 52576
  poverty_rate: 20.79
  homeownership_rate: 68.64
  unemployment_rate: 5.37
  median_home_value: 138900
  gini_index: 0.4733
  vacancy_rate: 17.97
  race_white: 27202
  race_black: 13832
  race_asian: 466
  race_native: 731
  hispanic: 4705
  bachelors_plus: 5778
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.6595
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.6158
  - to: "us/states/la/districts/house/50"
    rel: in-district
    area_weight: 0.5594
  - to: "us/states/la/districts/house/51"
    rel: in-district
    area_weight: 0.0564
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Mary Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47828 |
| Under 18 | 11697 |
| 18–64 | 27360 |
| 65+ | 8771 |
| Median household income | 52576 |
| Poverty rate | 20.79 |
| Homeownership rate | 68.64 |
| Unemployment rate | 5.37 |
| Median home value | 138900 |
| Gini index | 0.4733 |
| Vacancy rate | 17.97 |
| White | 27202 |
| Black | 13832 |
| Asian | 466 |
| Native | 731 |
| Hispanic/Latino | 4705 |
| Bachelor's or higher | 5778 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 66% (congressional)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 62% (state senate)
- [LA House District 50](/us/states/la/districts/house/50.md) — 56% (state house)
- [LA House District 51](/us/states/la/districts/house/51.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
