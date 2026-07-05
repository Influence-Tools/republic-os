---
type: Jurisdiction
title: "Oneida County, NY"
classification: county
fips: "36065"
state: "NY"
demographics:
  population: 229124
  population_under_18: 49023
  population_18_64: 134671
  population_65_plus: 45430
  median_household_income: 70154
  poverty_rate: 15.47
  homeownership_rate: 67.67
  unemployment_rate: 4.65
  median_home_value: 182600
  gini_index: 0.4511
  vacancy_rate: 9.7
  race_white: 183822
  race_black: 14093
  race_asian: 9862
  race_native: 436
  hispanic: 16197
  bachelors_plus: 63581
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.7246
  - to: "us/states/ny/districts/22"
    rel: in-district
    area_weight: 0.2752
  - to: "us/states/ny/districts/senate/53"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/117"
    rel: in-district
    area_weight: 0.398
  - to: "us/states/ny/districts/house/122"
    rel: in-district
    area_weight: 0.2846
  - to: "us/states/ny/districts/house/119"
    rel: in-district
    area_weight: 0.1757
  - to: "us/states/ny/districts/house/118"
    rel: in-district
    area_weight: 0.1417
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Oneida County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 229124 |
| Under 18 | 49023 |
| 18–64 | 134671 |
| 65+ | 45430 |
| Median household income | 70154 |
| Poverty rate | 15.47 |
| Homeownership rate | 67.67 |
| Unemployment rate | 4.65 |
| Median home value | 182600 |
| Gini index | 0.4511 |
| Vacancy rate | 9.7 |
| White | 183822 |
| Black | 14093 |
| Asian | 9862 |
| Native | 436 |
| Hispanic/Latino | 16197 |
| Bachelor's or higher | 63581 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 72% (congressional)
- [NY-22](/us/states/ny/districts/22.md) — 28% (congressional)
- [NY Senate District 53](/us/states/ny/districts/senate/53.md) — 100% (state senate)
- [NY House District 117](/us/states/ny/districts/house/117.md) — 40% (state house)
- [NY House District 122](/us/states/ny/districts/house/122.md) — 28% (state house)
- [NY House District 119](/us/states/ny/districts/house/119.md) — 18% (state house)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
