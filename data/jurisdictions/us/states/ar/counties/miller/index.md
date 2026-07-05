---
type: Jurisdiction
title: "Miller County, AR"
classification: county
fips: "05091"
state: "AR"
demographics:
  population: 42360
  population_under_18: 9899
  population_18_64: 25215
  population_65_plus: 7246
  median_household_income: 48836
  poverty_rate: 24.57
  homeownership_rate: 64.37
  unemployment_rate: 7.1
  median_home_value: 153900
  gini_index: 0.4931
  vacancy_rate: 17.56
  race_white: 28325
  race_black: 10806
  race_asian: 337
  race_native: 258
  hispanic: 1754
  bachelors_plus: 6211
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/senate/4"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/house/99"
    rel: in-district
    area_weight: 0.7354
  - to: "us/states/ar/districts/house/88"
    rel: in-district
    area_weight: 0.1815
  - to: "us/states/ar/districts/house/100"
    rel: in-district
    area_weight: 0.0828
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Miller County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42360 |
| Under 18 | 9899 |
| 18–64 | 25215 |
| 65+ | 7246 |
| Median household income | 48836 |
| Poverty rate | 24.57 |
| Homeownership rate | 64.37 |
| Unemployment rate | 7.1 |
| Median home value | 153900 |
| Gini index | 0.4931 |
| Vacancy rate | 17.56 |
| White | 28325 |
| Black | 10806 |
| Asian | 337 |
| Native | 258 |
| Hispanic/Latino | 1754 |
| Bachelor's or higher | 6211 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 4](/us/states/ar/districts/senate/4.md) — 100% (state senate)
- [AR House District 99](/us/states/ar/districts/house/99.md) — 74% (state house)
- [AR House District 88](/us/states/ar/districts/house/88.md) — 18% (state house)
- [AR House District 100](/us/states/ar/districts/house/100.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
