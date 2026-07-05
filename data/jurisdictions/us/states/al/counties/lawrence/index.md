---
type: Jurisdiction
title: "Lawrence County, AL"
classification: county
fips: "01079"
state: "AL"
demographics:
  population: 33276
  population_under_18: 7240
  population_18_64: 19700
  population_65_plus: 6336
  median_household_income: 66071
  poverty_rate: 13.31
  homeownership_rate: 81.67
  unemployment_rate: 1.96
  median_home_value: 172300
  gini_index: 0.4275
  vacancy_rate: 11.53
  race_white: 25268
  race_black: 3110
  race_asian: 135
  race_native: 1237
  hispanic: 1044
  bachelors_plus: 4782
districts:
  - to: "us/states/al/districts/05"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/al/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/7"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Lawrence County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33276 |
| Under 18 | 7240 |
| 18–64 | 19700 |
| 65+ | 6336 |
| Median household income | 66071 |
| Poverty rate | 13.31 |
| Homeownership rate | 81.67 |
| Unemployment rate | 1.96 |
| Median home value | 172300 |
| Gini index | 0.4275 |
| Vacancy rate | 11.53 |
| White | 25268 |
| Black | 3110 |
| Asian | 135 |
| Native | 1237 |
| Hispanic/Latino | 1044 |
| Bachelor's or higher | 4782 |

## Districts

- [AL-05](/us/states/al/districts/05.md) — 100% (congressional)
- [AL Senate District 6](/us/states/al/districts/senate/6.md) — 100% (state senate)
- [AL House District 7](/us/states/al/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
