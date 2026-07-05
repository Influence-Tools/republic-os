---
type: Jurisdiction
title: "Houston County, TX"
classification: county
fips: "48225"
state: "TX"
demographics:
  population: 22051
  population_under_18: 4479
  population_18_64: 12674
  population_65_plus: 4898
  median_household_income: 56531
  poverty_rate: 15.03
  homeownership_rate: 70.64
  unemployment_rate: 6.71
  median_home_value: 164900
  gini_index: 0.4682
  vacancy_rate: 26.34
  race_white: 13511
  race_black: 4609
  race_asian: 84
  race_native: 216
  hispanic: 3187
  bachelors_plus: 3214
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
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

# Houston County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22051 |
| Under 18 | 4479 |
| 18–64 | 12674 |
| 65+ | 4898 |
| Median household income | 56531 |
| Poverty rate | 15.03 |
| Homeownership rate | 70.64 |
| Unemployment rate | 6.71 |
| Median home value | 164900 |
| Gini index | 0.4682 |
| Vacancy rate | 26.34 |
| White | 13511 |
| Black | 4609 |
| Asian | 84 |
| Native | 216 |
| Hispanic/Latino | 3187 |
| Bachelor's or higher | 3214 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
