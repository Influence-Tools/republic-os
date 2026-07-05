---
type: Jurisdiction
title: "Tyler County, TX"
classification: county
fips: "48457"
state: "TX"
demographics:
  population: 20238
  population_under_18: 3885
  population_18_64: 11815
  population_65_plus: 4538
  median_household_income: 55396
  poverty_rate: 17.9
  homeownership_rate: 81.18
  unemployment_rate: 7.07
  median_home_value: 157300
  gini_index: 0.5007
  vacancy_rate: 24.93
  race_white: 15775
  race_black: 2157
  race_asian: 98
  race_native: 24
  hispanic: 1696
  bachelors_plus: 2377
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/9"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Tyler County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20238 |
| Under 18 | 3885 |
| 18–64 | 11815 |
| 65+ | 4538 |
| Median household income | 55396 |
| Poverty rate | 17.9 |
| Homeownership rate | 81.18 |
| Unemployment rate | 7.07 |
| Median home value | 157300 |
| Gini index | 0.5007 |
| Vacancy rate | 24.93 |
| White | 15775 |
| Black | 2157 |
| Asian | 98 |
| Native | 24 |
| Hispanic/Latino | 1696 |
| Bachelor's or higher | 2377 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
