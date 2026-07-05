---
type: Jurisdiction
title: "Cayuga County, NY"
classification: county
fips: "36011"
state: "NY"
demographics:
  population: 75102
  population_under_18: 14516
  population_18_64: 44557
  population_65_plus: 16029
  median_household_income: 67904
  poverty_rate: 13.51
  homeownership_rate: 71.43
  unemployment_rate: 3.8
  median_home_value: 171000
  gini_index: 0.4365
  vacancy_rate: 14.4
  race_white: 65756
  race_black: 2551
  race_asian: 493
  race_native: 132
  hispanic: 2731
  bachelors_plus: 19717
districts:
  - to: "us/states/ny/districts/22"
    rel: in-district
    area_weight: 0.5042
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.3459
  - to: "us/states/ny/districts/senate/48"
    rel: in-district
    area_weight: 0.8501
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.4928
  - to: "us/states/ny/districts/house/126"
    rel: in-district
    area_weight: 0.2219
  - to: "us/states/ny/districts/house/120"
    rel: in-district
    area_weight: 0.1354
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Cayuga County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 75102 |
| Under 18 | 14516 |
| 18–64 | 44557 |
| 65+ | 16029 |
| Median household income | 67904 |
| Poverty rate | 13.51 |
| Homeownership rate | 71.43 |
| Unemployment rate | 3.8 |
| Median home value | 171000 |
| Gini index | 0.4365 |
| Vacancy rate | 14.4 |
| White | 65756 |
| Black | 2551 |
| Asian | 493 |
| Native | 132 |
| Hispanic/Latino | 2731 |
| Bachelor's or higher | 19717 |

## Districts

- [NY-22](/us/states/ny/districts/22.md) — 50% (congressional)
- [NY-24](/us/states/ny/districts/24.md) — 35% (congressional)
- [NY Senate District 48](/us/states/ny/districts/senate/48.md) — 85% (state senate)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 49% (state house)
- [NY House District 126](/us/states/ny/districts/house/126.md) — 22% (state house)
- [NY House District 120](/us/states/ny/districts/house/120.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
