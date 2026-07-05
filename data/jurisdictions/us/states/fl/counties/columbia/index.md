---
type: Jurisdiction
title: "Columbia County, FL"
classification: county
fips: "12023"
state: "FL"
demographics:
  population: 71789
  population_under_18: 17451
  population_18_64: 21889
  population_65_plus: 32449
  median_household_income: 59205
  poverty_rate: 16.67
  homeownership_rate: 72.5
  unemployment_rate: 5.33
  median_home_value: 194900
  gini_index: 0.4492
  vacancy_rate: 9.47
  race_white: 51449
  race_black: 11721
  race_asian: 697
  race_native: 121
  hispanic: 5663
  bachelors_plus: 11114
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/fl/districts/house/10"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Columbia County, FL

County jurisdiction — 26 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71789 |
| Under 18 | 17451 |
| 18–64 | 21889 |
| 65+ | 32449 |
| Median household income | 59205 |
| Poverty rate | 16.67 |
| Homeownership rate | 72.5 |
| Unemployment rate | 5.33 |
| Median home value | 194900 |
| Gini index | 0.4492 |
| Vacancy rate | 9.47 |
| White | 51449 |
| Black | 11721 |
| Asian | 697 |
| Native | 121 |
| Hispanic/Latino | 5663 |
| Bachelor's or higher | 11114 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 100% (state senate)
- [FL House District 10](/us/states/fl/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
