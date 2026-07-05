---
type: Jurisdiction
title: "Otsego County, NY"
classification: county
fips: "36077"
state: "NY"
demographics:
  population: 60108
  population_under_18: 8951
  population_18_64: 38246
  population_65_plus: 12911
  median_household_income: 68885
  poverty_rate: 12.54
  homeownership_rate: 73.87
  unemployment_rate: 6.37
  median_home_value: 179100
  gini_index: 0.4451
  vacancy_rate: 22.85
  race_white: 53637
  race_black: 1357
  race_asian: 922
  race_native: 140
  hispanic: 2687
  bachelors_plus: 19589
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/102"
    rel: in-district
    area_weight: 0.3904
  - to: "us/states/ny/districts/house/122"
    rel: in-district
    area_weight: 0.3142
  - to: "us/states/ny/districts/house/121"
    rel: in-district
    area_weight: 0.2633
  - to: "us/states/ny/districts/house/118"
    rel: in-district
    area_weight: 0.0321
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Otsego County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60108 |
| Under 18 | 8951 |
| 18–64 | 38246 |
| 65+ | 12911 |
| Median household income | 68885 |
| Poverty rate | 12.54 |
| Homeownership rate | 73.87 |
| Unemployment rate | 6.37 |
| Median home value | 179100 |
| Gini index | 0.4451 |
| Vacancy rate | 22.85 |
| White | 53637 |
| Black | 1357 |
| Asian | 922 |
| Native | 140 |
| Hispanic/Latino | 2687 |
| Bachelor's or higher | 19589 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 100% (state senate)
- [NY House District 102](/us/states/ny/districts/house/102.md) — 39% (state house)
- [NY House District 122](/us/states/ny/districts/house/122.md) — 31% (state house)
- [NY House District 121](/us/states/ny/districts/house/121.md) — 26% (state house)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
