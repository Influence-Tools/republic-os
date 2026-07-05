---
type: Jurisdiction
title: "Howard County, AR"
classification: county
fips: "05061"
state: "AR"
demographics:
  population: 12583
  population_under_18: 3234
  population_18_64: 6978
  population_65_plus: 2371
  median_household_income: 45603
  poverty_rate: 22.52
  homeownership_rate: 72.54
  unemployment_rate: 5.38
  median_home_value: 153900
  gini_index: 0.4583
  vacancy_rate: 17.41
  race_white: 8186
  race_black: 2623
  race_asian: 73
  race_native: 12
  hispanic: 1582
  bachelors_plus: 1807
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/86"
    rel: in-district
    area_weight: 0.6247
  - to: "us/states/ar/districts/house/88"
    rel: in-district
    area_weight: 0.3047
  - to: "us/states/ar/districts/house/87"
    rel: in-district
    area_weight: 0.0706
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Howard County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12583 |
| Under 18 | 3234 |
| 18–64 | 6978 |
| 65+ | 2371 |
| Median household income | 45603 |
| Poverty rate | 22.52 |
| Homeownership rate | 72.54 |
| Unemployment rate | 5.38 |
| Median home value | 153900 |
| Gini index | 0.4583 |
| Vacancy rate | 17.41 |
| White | 8186 |
| Black | 2623 |
| Asian | 73 |
| Native | 12 |
| Hispanic/Latino | 1582 |
| Bachelor's or higher | 1807 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 4](/us/states/ar/districts/senate/4.md) — 100% (state senate)
- [AR House District 86](/us/states/ar/districts/house/86.md) — 62% (state house)
- [AR House District 88](/us/states/ar/districts/house/88.md) — 30% (state house)
- [AR House District 87](/us/states/ar/districts/house/87.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
