---
type: Jurisdiction
title: "Haywood County, NC"
classification: county
fips: "37087"
state: "NC"
demographics:
  population: 62662
  population_under_18: 11025
  population_18_64: 35531
  population_65_plus: 16106
  median_household_income: 61912
  poverty_rate: 13.13
  homeownership_rate: 74.9
  unemployment_rate: 3.09
  median_home_value: 279200
  gini_index: 0.4358
  vacancy_rate: 23.73
  race_white: 57171
  race_black: 567
  race_asian: 229
  race_native: 414
  hispanic: 3103
  bachelors_plus: 19499
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.7374
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.2621
  - to: "us/states/nc/districts/house/118"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Haywood County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62662 |
| Under 18 | 11025 |
| 18–64 | 35531 |
| 65+ | 16106 |
| Median household income | 61912 |
| Poverty rate | 13.13 |
| Homeownership rate | 74.9 |
| Unemployment rate | 3.09 |
| Median home value | 279200 |
| Gini index | 0.4358 |
| Vacancy rate | 23.73 |
| White | 57171 |
| Black | 567 |
| Asian | 229 |
| Native | 414 |
| Hispanic/Latino | 3103 |
| Bachelor's or higher | 19499 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 74% (state senate)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 26% (state senate)
- [NC House District 118](/us/states/nc/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
