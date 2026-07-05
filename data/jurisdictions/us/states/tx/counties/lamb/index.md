---
type: Jurisdiction
title: "Lamb County, TX"
classification: county
fips: "48279"
state: "TX"
demographics:
  population: 12828
  population_under_18: 3489
  population_18_64: 7142
  population_65_plus: 2197
  median_household_income: 60760
  poverty_rate: 15.03
  homeownership_rate: 74.04
  unemployment_rate: 2.06
  median_home_value: 82400
  gini_index: 0.4214
  vacancy_rate: 20.53
  race_white: 8771
  race_black: 473
  race_asian: 101
  race_native: 52
  hispanic: 7478
  bachelors_plus: 1540
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lamb County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12828 |
| Under 18 | 3489 |
| 18–64 | 7142 |
| 65+ | 2197 |
| Median household income | 60760 |
| Poverty rate | 15.03 |
| Homeownership rate | 74.04 |
| Unemployment rate | 2.06 |
| Median home value | 82400 |
| Gini index | 0.4214 |
| Vacancy rate | 20.53 |
| White | 8771 |
| Black | 473 |
| Asian | 101 |
| Native | 52 |
| Hispanic/Latino | 7478 |
| Bachelor's or higher | 1540 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
