---
type: Jurisdiction
title: "Luzerne County, PA"
classification: county
fips: "42079"
state: "PA"
demographics:
  population: 327675
  population_under_18: 66457
  population_18_64: 195296
  population_65_plus: 65922
  median_household_income: 63691
  poverty_rate: 15.32
  homeownership_rate: 67.8
  unemployment_rate: 5.8
  median_home_value: 174100
  gini_index: 0.4639
  vacancy_rate: 10.73
  race_white: 248337
  race_black: 16461
  race_asian: 3957
  race_native: 370
  hispanic: 56836
  bachelors_plus: 82126
districts:
  - to: "us/states/pa/districts/08"
    rel: in-district
    area_weight: 0.5645
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.4345
  - to: "us/states/pa/districts/senate/20"
    rel: in-district
    area_weight: 0.3808
  - to: "us/states/pa/districts/senate/27"
    rel: in-district
    area_weight: 0.2934
  - to: "us/states/pa/districts/senate/29"
    rel: in-district
    area_weight: 0.2464
  - to: "us/states/pa/districts/senate/22"
    rel: in-district
    area_weight: 0.0793
  - to: "us/states/pa/districts/house/117"
    rel: in-district
    area_weight: 0.5574
  - to: "us/states/pa/districts/house/121"
    rel: in-district
    area_weight: 0.1287
  - to: "us/states/pa/districts/house/119"
    rel: in-district
    area_weight: 0.11
  - to: "us/states/pa/districts/house/120"
    rel: in-district
    area_weight: 0.1001
  - to: "us/states/pa/districts/house/116"
    rel: in-district
    area_weight: 0.0582
  - to: "us/states/pa/districts/house/118"
    rel: in-district
    area_weight: 0.0455
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Luzerne County, PA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 327675 |
| Under 18 | 66457 |
| 18–64 | 195296 |
| 65+ | 65922 |
| Median household income | 63691 |
| Poverty rate | 15.32 |
| Homeownership rate | 67.8 |
| Unemployment rate | 5.8 |
| Median home value | 174100 |
| Gini index | 0.4639 |
| Vacancy rate | 10.73 |
| White | 248337 |
| Black | 16461 |
| Asian | 3957 |
| Native | 370 |
| Hispanic/Latino | 56836 |
| Bachelor's or higher | 82126 |

## Districts

- [PA-08](/us/states/pa/districts/08.md) — 56% (congressional)
- [PA-09](/us/states/pa/districts/09.md) — 43% (congressional)
- [PA Senate District 20](/us/states/pa/districts/senate/20.md) — 38% (state senate)
- [PA Senate District 27](/us/states/pa/districts/senate/27.md) — 29% (state senate)
- [PA Senate District 29](/us/states/pa/districts/senate/29.md) — 25% (state senate)
- [PA Senate District 22](/us/states/pa/districts/senate/22.md) — 8% (state senate)
- [PA House District 117](/us/states/pa/districts/house/117.md) — 56% (state house)
- [PA House District 121](/us/states/pa/districts/house/121.md) — 13% (state house)
- [PA House District 119](/us/states/pa/districts/house/119.md) — 11% (state house)
- [PA House District 120](/us/states/pa/districts/house/120.md) — 10% (state house)
- [PA House District 116](/us/states/pa/districts/house/116.md) — 6% (state house)
- [PA House District 118](/us/states/pa/districts/house/118.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
