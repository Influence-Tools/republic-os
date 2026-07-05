---
type: Jurisdiction
title: "Hubbard County, MN"
classification: county
fips: "27057"
state: "MN"
demographics:
  population: 21831
  population_under_18: 4528
  population_18_64: 11444
  population_65_plus: 5859
  median_household_income: 71995
  poverty_rate: 10.77
  homeownership_rate: 83.05
  unemployment_rate: 4.36
  median_home_value: 282600
  gini_index: 0.4569
  vacancy_rate: 39.29
  race_white: 19767
  race_black: 113
  race_asian: 90
  race_native: 429
  hispanic: 575
  bachelors_plus: 6531
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.6669
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.3331
  - to: "us/states/mn/districts/senate/5"
    rel: in-district
    area_weight: 0.6733
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.3267
  - to: "us/states/mn/districts/house/5a"
    rel: in-district
    area_weight: 0.6733
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.3266
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Hubbard County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21831 |
| Under 18 | 4528 |
| 18–64 | 11444 |
| 65+ | 5859 |
| Median household income | 71995 |
| Poverty rate | 10.77 |
| Homeownership rate | 83.05 |
| Unemployment rate | 4.36 |
| Median home value | 282600 |
| Gini index | 0.4569 |
| Vacancy rate | 39.29 |
| White | 19767 |
| Black | 113 |
| Asian | 90 |
| Native | 429 |
| Hispanic/Latino | 575 |
| Bachelor's or higher | 6531 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 67% (congressional)
- [MN-07](/us/states/mn/districts/07.md) — 33% (congressional)
- [MN Senate District 5](/us/states/mn/districts/senate/5.md) — 67% (state senate)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 33% (state senate)
- [MN House District 5A](/us/states/mn/districts/house/5a.md) — 67% (state house)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
