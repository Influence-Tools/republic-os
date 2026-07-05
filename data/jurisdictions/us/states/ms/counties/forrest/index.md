---
type: Jurisdiction
title: "Forrest County, MS"
classification: county
fips: "28035"
state: "MS"
demographics:
  population: 78272
  population_under_18: 17773
  population_18_64: 49748
  population_65_plus: 10751
  median_household_income: 53640
  poverty_rate: 20.97
  homeownership_rate: 57.17
  unemployment_rate: 6.69
  median_home_value: 168000
  gini_index: 0.505
  vacancy_rate: 10.74
  race_white: 44272
  race_black: 27807
  race_asian: 760
  race_native: 156
  hispanic: 3428
  bachelors_plus: 20815
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/45"
    rel: in-district
    area_weight: 0.8114
  - to: "us/states/ms/districts/senate/42"
    rel: in-district
    area_weight: 0.1028
  - to: "us/states/ms/districts/senate/34"
    rel: in-district
    area_weight: 0.0857
  - to: "us/states/ms/districts/house/104"
    rel: in-district
    area_weight: 0.724
  - to: "us/states/ms/districts/house/103"
    rel: in-district
    area_weight: 0.1115
  - to: "us/states/ms/districts/house/87"
    rel: in-district
    area_weight: 0.0597
  - to: "us/states/ms/districts/house/90"
    rel: in-district
    area_weight: 0.0592
  - to: "us/states/ms/districts/house/102"
    rel: in-district
    area_weight: 0.0451
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Forrest County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 78272 |
| Under 18 | 17773 |
| 18–64 | 49748 |
| 65+ | 10751 |
| Median household income | 53640 |
| Poverty rate | 20.97 |
| Homeownership rate | 57.17 |
| Unemployment rate | 6.69 |
| Median home value | 168000 |
| Gini index | 0.505 |
| Vacancy rate | 10.74 |
| White | 44272 |
| Black | 27807 |
| Asian | 760 |
| Native | 156 |
| Hispanic/Latino | 3428 |
| Bachelor's or higher | 20815 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 45](/us/states/ms/districts/senate/45.md) — 81% (state senate)
- [MS Senate District 42](/us/states/ms/districts/senate/42.md) — 10% (state senate)
- [MS Senate District 34](/us/states/ms/districts/senate/34.md) — 9% (state senate)
- [MS House District 104](/us/states/ms/districts/house/104.md) — 72% (state house)
- [MS House District 103](/us/states/ms/districts/house/103.md) — 11% (state house)
- [MS House District 87](/us/states/ms/districts/house/87.md) — 6% (state house)
- [MS House District 90](/us/states/ms/districts/house/90.md) — 6% (state house)
- [MS House District 102](/us/states/ms/districts/house/102.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
