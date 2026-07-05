---
type: Jurisdiction
title: "Wilkes County, NC"
classification: county
fips: "37193"
state: "NC"
demographics:
  population: 65935
  population_under_18: 13159
  population_18_64: 37666
  population_65_plus: 15110
  median_household_income: 51721
  poverty_rate: 16.73
  homeownership_rate: 73.52
  unemployment_rate: 5.02
  median_home_value: 168800
  gini_index: 0.4182
  vacancy_rate: 14.85
  race_white: 57339
  race_black: 2403
  race_asian: 396
  race_native: 128
  hispanic: 4915
  bachelors_plus: 10996
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/senate/36"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/94"
    rel: in-district
    area_weight: 0.7226
  - to: "us/states/nc/districts/house/90"
    rel: in-district
    area_weight: 0.2771
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Wilkes County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65935 |
| Under 18 | 13159 |
| 18–64 | 37666 |
| 65+ | 15110 |
| Median household income | 51721 |
| Poverty rate | 16.73 |
| Homeownership rate | 73.52 |
| Unemployment rate | 5.02 |
| Median home value | 168800 |
| Gini index | 0.4182 |
| Vacancy rate | 14.85 |
| White | 57339 |
| Black | 2403 |
| Asian | 396 |
| Native | 128 |
| Hispanic/Latino | 4915 |
| Bachelor's or higher | 10996 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 36](/us/states/nc/districts/senate/36.md) — 100% (state senate)
- [NC House District 94](/us/states/nc/districts/house/94.md) — 72% (state house)
- [NC House District 90](/us/states/nc/districts/house/90.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
