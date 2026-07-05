---
type: Jurisdiction
title: "Washington County, NY"
classification: county
fips: "36115"
state: "NY"
demographics:
  population: 60522
  population_under_18: 11160
  population_18_64: 36254
  population_65_plus: 13108
  median_household_income: 73495
  poverty_rate: 10.73
  homeownership_rate: 76.65
  unemployment_rate: 5.02
  median_home_value: 196200
  gini_index: 0.4078
  vacancy_rate: 16.18
  race_white: 54760
  race_black: 1441
  race_asian: 437
  race_native: 37
  hispanic: 1791
  bachelors_plus: 14216
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ny/districts/senate/43"
    rel: in-district
    area_weight: 0.6436
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.3559
  - to: "us/states/ny/districts/house/114"
    rel: in-district
    area_weight: 0.739
  - to: "us/states/ny/districts/house/107"
    rel: in-district
    area_weight: 0.1737
  - to: "us/states/ny/districts/house/113"
    rel: in-district
    area_weight: 0.0868
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Washington County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60522 |
| Under 18 | 11160 |
| 18–64 | 36254 |
| 65+ | 13108 |
| Median household income | 73495 |
| Poverty rate | 10.73 |
| Homeownership rate | 76.65 |
| Unemployment rate | 5.02 |
| Median home value | 196200 |
| Gini index | 0.4078 |
| Vacancy rate | 16.18 |
| White | 54760 |
| Black | 1441 |
| Asian | 437 |
| Native | 37 |
| Hispanic/Latino | 1791 |
| Bachelor's or higher | 14216 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 43](/us/states/ny/districts/senate/43.md) — 64% (state senate)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 36% (state senate)
- [NY House District 114](/us/states/ny/districts/house/114.md) — 74% (state house)
- [NY House District 107](/us/states/ny/districts/house/107.md) — 17% (state house)
- [NY House District 113](/us/states/ny/districts/house/113.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
