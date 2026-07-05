---
type: Jurisdiction
title: "Crawford County, AR"
classification: county
fips: "05033"
state: "AR"
demographics:
  population: 61139
  population_under_18: 14636
  population_18_64: 35549
  population_65_plus: 10954
  median_household_income: 64132
  poverty_rate: 14.66
  homeownership_rate: 75.47
  unemployment_rate: 4.06
  median_home_value: 182800
  gini_index: 0.4296
  vacancy_rate: 8.84
  race_white: 49797
  race_black: 789
  race_asian: 692
  race_native: 558
  hispanic: 5251
  bachelors_plus: 10845
districts:
  - to: "us/states/ar/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ar/districts/senate/29"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/house/24"
    rel: in-district
    area_weight: 0.573
  - to: "us/states/ar/districts/house/25"
    rel: in-district
    area_weight: 0.3284
  - to: "us/states/ar/districts/house/48"
    rel: in-district
    area_weight: 0.0983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Crawford County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61139 |
| Under 18 | 14636 |
| 18–64 | 35549 |
| 65+ | 10954 |
| Median household income | 64132 |
| Poverty rate | 14.66 |
| Homeownership rate | 75.47 |
| Unemployment rate | 4.06 |
| Median home value | 182800 |
| Gini index | 0.4296 |
| Vacancy rate | 8.84 |
| White | 49797 |
| Black | 789 |
| Asian | 692 |
| Native | 558 |
| Hispanic/Latino | 5251 |
| Bachelor's or higher | 10845 |

## Districts

- [AR-03](/us/states/ar/districts/03.md) — 100% (congressional)
- [AR Senate District 29](/us/states/ar/districts/senate/29.md) — 100% (state senate)
- [AR House District 24](/us/states/ar/districts/house/24.md) — 57% (state house)
- [AR House District 25](/us/states/ar/districts/house/25.md) — 33% (state house)
- [AR House District 48](/us/states/ar/districts/house/48.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
