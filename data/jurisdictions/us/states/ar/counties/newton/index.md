---
type: Jurisdiction
title: "Newton County, AR"
classification: county
fips: "05101"
state: "AR"
demographics:
  population: 7112
  population_under_18: 1332
  population_18_64: 3808
  population_65_plus: 1972
  median_household_income: 48986
  poverty_rate: 15.87
  homeownership_rate: 76.53
  unemployment_rate: 4.09
  median_home_value: 169300
  gini_index: 0.4246
  vacancy_rate: 22.44
  race_white: 6621
  race_black: 11
  race_asian: 3
  race_native: 46
  hispanic: 118
  bachelors_plus: 1093
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.7701
  - to: "us/states/ar/districts/senate/24"
    rel: in-district
    area_weight: 0.2299
  - to: "us/states/ar/districts/house/27"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Newton County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7112 |
| Under 18 | 1332 |
| 18–64 | 3808 |
| 65+ | 1972 |
| Median household income | 48986 |
| Poverty rate | 15.87 |
| Homeownership rate | 76.53 |
| Unemployment rate | 4.09 |
| Median home value | 169300 |
| Gini index | 0.4246 |
| Vacancy rate | 22.44 |
| White | 6621 |
| Black | 11 |
| Asian | 3 |
| Native | 46 |
| Hispanic/Latino | 118 |
| Bachelor's or higher | 1093 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 77% (state senate)
- [AR Senate District 24](/us/states/ar/districts/senate/24.md) — 23% (state senate)
- [AR House District 27](/us/states/ar/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
