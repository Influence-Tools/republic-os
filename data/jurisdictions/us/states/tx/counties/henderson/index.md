---
type: Jurisdiction
title: "Henderson County, TX"
classification: county
fips: "48213"
state: "TX"
demographics:
  population: 84862
  population_under_18: 18164
  population_18_64: 47562
  population_65_plus: 19136
  median_household_income: 65179
  poverty_rate: 14.73
  homeownership_rate: 77.81
  unemployment_rate: 4.91
  median_home_value: 211300
  gini_index: 0.4549
  vacancy_rate: 19.78
  race_white: 65819
  race_black: 4308
  race_asian: 667
  race_native: 259
  hispanic: 12555
  bachelors_plus: 16540
districts:
  - to: "us/states/tx/districts/05"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/8"
    rel: in-district
    area_weight: 0.6137
  - to: "us/states/tx/districts/house/4"
    rel: in-district
    area_weight: 0.3861
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Henderson County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84862 |
| Under 18 | 18164 |
| 18–64 | 47562 |
| 65+ | 19136 |
| Median household income | 65179 |
| Poverty rate | 14.73 |
| Homeownership rate | 77.81 |
| Unemployment rate | 4.91 |
| Median home value | 211300 |
| Gini index | 0.4549 |
| Vacancy rate | 19.78 |
| White | 65819 |
| Black | 4308 |
| Asian | 667 |
| Native | 259 |
| Hispanic/Latino | 12555 |
| Bachelor's or higher | 16540 |

## Districts

- [TX-05](/us/states/tx/districts/05.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 8](/us/states/tx/districts/house/8.md) — 61% (state house)
- [TX House District 4](/us/states/tx/districts/house/4.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
