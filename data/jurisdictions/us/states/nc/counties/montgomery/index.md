---
type: Jurisdiction
title: "Montgomery County, NC"
classification: county
fips: "37123"
state: "NC"
demographics:
  population: 26007
  population_under_18: 5308
  population_18_64: 14912
  population_65_plus: 5787
  median_household_income: 57766
  poverty_rate: 15.44
  homeownership_rate: 74.99
  unemployment_rate: 2.85
  median_home_value: 161700
  gini_index: 0.4602
  vacancy_rate: 29.04
  race_white: 16765
  race_black: 4222
  race_asian: 381
  race_native: 326
  hispanic: 4115
  bachelors_plus: 4941
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/67"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Montgomery County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26007 |
| Under 18 | 5308 |
| 18–64 | 14912 |
| 65+ | 5787 |
| Median household income | 57766 |
| Poverty rate | 15.44 |
| Homeownership rate | 74.99 |
| Unemployment rate | 2.85 |
| Median home value | 161700 |
| Gini index | 0.4602 |
| Vacancy rate | 29.04 |
| White | 16765 |
| Black | 4222 |
| Asian | 381 |
| Native | 326 |
| Hispanic/Latino | 4115 |
| Bachelor's or higher | 4941 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 100% (congressional)
- [NC Senate District 29](/us/states/nc/districts/senate/29.md) — 100% (state senate)
- [NC House District 67](/us/states/nc/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
