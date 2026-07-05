---
type: Jurisdiction
title: "Terry County, TX"
classification: county
fips: "48445"
state: "TX"
demographics:
  population: 11629
  population_under_18: 3217
  population_18_64: 6530
  population_65_plus: 1882
  median_household_income: 44100
  poverty_rate: 18.33
  homeownership_rate: 66.51
  unemployment_rate: 4.47
  median_home_value: 105400
  gini_index: 0.4484
  vacancy_rate: 10.27
  race_white: 5475
  race_black: 389
  race_asian: 20
  race_native: 76
  hispanic: 6619
  bachelors_plus: 931
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/83"
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

# Terry County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11629 |
| Under 18 | 3217 |
| 18–64 | 6530 |
| 65+ | 1882 |
| Median household income | 44100 |
| Poverty rate | 18.33 |
| Homeownership rate | 66.51 |
| Unemployment rate | 4.47 |
| Median home value | 105400 |
| Gini index | 0.4484 |
| Vacancy rate | 10.27 |
| White | 5475 |
| Black | 389 |
| Asian | 20 |
| Native | 76 |
| Hispanic/Latino | 6619 |
| Bachelor's or higher | 931 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
