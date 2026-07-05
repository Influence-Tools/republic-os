---
type: Jurisdiction
title: "Glades County, FL"
classification: county
fips: "12043"
state: "FL"
demographics:
  population: 12563
  population_under_18: 1887
  population_18_64: 4214
  population_65_plus: 6462
  median_household_income: 45870
  poverty_rate: 17.21
  homeownership_rate: 85.09
  unemployment_rate: 7.13
  median_home_value: 137000
  gini_index: 0.464
  vacancy_rate: 32.74
  race_white: 7912
  race_black: 1849
  race_asian: 57
  race_native: 459
  hispanic: 3225
  bachelors_plus: 1593
districts:
  - to: "us/states/fl/districts/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/fl/districts/senate/29"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/83"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Glades County, FL

County jurisdiction — 21 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12563 |
| Under 18 | 1887 |
| 18–64 | 4214 |
| 65+ | 6462 |
| Median household income | 45870 |
| Poverty rate | 17.21 |
| Homeownership rate | 85.09 |
| Unemployment rate | 7.13 |
| Median home value | 137000 |
| Gini index | 0.464 |
| Vacancy rate | 32.74 |
| White | 7912 |
| Black | 1849 |
| Asian | 57 |
| Native | 459 |
| Hispanic/Latino | 3225 |
| Bachelor's or higher | 1593 |

## Districts

- [FL-18](/us/states/fl/districts/18.md) — 100% (congressional)
- [FL Senate District 29](/us/states/fl/districts/senate/29.md) — 100% (state senate)
- [FL House District 83](/us/states/fl/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
