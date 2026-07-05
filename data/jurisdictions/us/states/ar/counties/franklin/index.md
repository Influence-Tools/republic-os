---
type: Jurisdiction
title: "Franklin County, AR"
classification: county
fips: "05047"
state: "AR"
demographics:
  population: 17326
  population_under_18: 3871
  population_18_64: 9872
  population_65_plus: 3583
  median_household_income: 55886
  poverty_rate: 17.98
  homeownership_rate: 77.95
  unemployment_rate: 4.87
  median_home_value: 130800
  gini_index: 0.4711
  vacancy_rate: 9.14
  race_white: 15049
  race_black: 40
  race_asian: 105
  race_native: 168
  hispanic: 577
  bachelors_plus: 2364
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ar/districts/senate/26"
    rel: in-district
    area_weight: 0.52
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.48
  - to: "us/states/ar/districts/house/26"
    rel: in-district
    area_weight: 0.5006
  - to: "us/states/ar/districts/house/46"
    rel: in-district
    area_weight: 0.345
  - to: "us/states/ar/districts/house/25"
    rel: in-district
    area_weight: 0.1543
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Franklin County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17326 |
| Under 18 | 3871 |
| 18–64 | 9872 |
| 65+ | 3583 |
| Median household income | 55886 |
| Poverty rate | 17.98 |
| Homeownership rate | 77.95 |
| Unemployment rate | 4.87 |
| Median home value | 130800 |
| Gini index | 0.4711 |
| Vacancy rate | 9.14 |
| White | 15049 |
| Black | 40 |
| Asian | 105 |
| Native | 168 |
| Hispanic/Latino | 577 |
| Bachelor's or higher | 2364 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 26](/us/states/ar/districts/senate/26.md) — 52% (state senate)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 48% (state senate)
- [AR House District 26](/us/states/ar/districts/house/26.md) — 50% (state house)
- [AR House District 46](/us/states/ar/districts/house/46.md) — 34% (state house)
- [AR House District 25](/us/states/ar/districts/house/25.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
