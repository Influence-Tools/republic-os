---
type: Jurisdiction
title: "Union County, FL"
classification: county
fips: "12125"
state: "FL"
demographics:
  population: 15701
  population_under_18: 3414
  population_18_64: 9680
  population_65_plus: 2607
  median_household_income: 64146
  poverty_rate: 19.54
  homeownership_rate: 74.75
  unemployment_rate: 4.76
  median_home_value: 169500
  gini_index: 0.4789
  vacancy_rate: 10.68
  race_white: 11211
  race_black: 2337
  race_asian: 38
  race_native: 0
  hispanic: 846
  bachelors_plus: 1658
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/10"
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

# Union County, FL

County jurisdiction — 30 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15701 |
| Under 18 | 3414 |
| 18–64 | 9680 |
| 65+ | 2607 |
| Median household income | 64146 |
| Poverty rate | 19.54 |
| Homeownership rate | 74.75 |
| Unemployment rate | 4.76 |
| Median home value | 169500 |
| Gini index | 0.4789 |
| Vacancy rate | 10.68 |
| White | 11211 |
| Black | 2337 |
| Asian | 38 |
| Native | 0 |
| Hispanic/Latino | 846 |
| Bachelor's or higher | 1658 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 100% (state senate)
- [FL House District 10](/us/states/fl/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
