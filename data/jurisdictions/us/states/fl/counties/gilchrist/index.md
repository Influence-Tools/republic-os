---
type: Jurisdiction
title: "Gilchrist County, FL"
classification: county
fips: "12041"
state: "FL"
demographics:
  population: 19040
  population_under_18: 4303
  population_18_64: 5751
  population_65_plus: 8986
  median_household_income: 63523
  poverty_rate: 11.5
  homeownership_rate: 85.72
  unemployment_rate: 3.47
  median_home_value: 199900
  gini_index: 0.4927
  vacancy_rate: 9.06
  race_white: 16561
  race_black: 607
  race_asian: 36
  race_native: 96
  hispanic: 1529
  bachelors_plus: 2843
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/fl/districts/house/22"
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

# Gilchrist County, FL

County jurisdiction — 25 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19040 |
| Under 18 | 4303 |
| 18–64 | 5751 |
| 65+ | 8986 |
| Median household income | 63523 |
| Poverty rate | 11.5 |
| Homeownership rate | 85.72 |
| Unemployment rate | 3.47 |
| Median home value | 199900 |
| Gini index | 0.4927 |
| Vacancy rate | 9.06 |
| White | 16561 |
| Black | 607 |
| Asian | 36 |
| Native | 96 |
| Hispanic/Latino | 1529 |
| Bachelor's or higher | 2843 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 100% (state senate)
- [FL House District 22](/us/states/fl/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
