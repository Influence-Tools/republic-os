---
type: Jurisdiction
title: "Logan County, AR"
classification: county
fips: "05083"
state: "AR"
demographics:
  population: 21277
  population_under_18: 4590
  population_18_64: 12445
  population_65_plus: 4242
  median_household_income: 58555
  poverty_rate: 13.93
  homeownership_rate: 78.39
  unemployment_rate: 5.64
  median_home_value: 139900
  gini_index: 0.4618
  vacancy_rate: 12.69
  race_white: 19015
  race_black: 312
  race_asian: 322
  race_native: 23
  hispanic: 744
  bachelors_plus: 3288
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/26"
    rel: in-district
    area_weight: 0.7968
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.2032
  - to: "us/states/ar/districts/house/46"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Logan County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21277 |
| Under 18 | 4590 |
| 18–64 | 12445 |
| 65+ | 4242 |
| Median household income | 58555 |
| Poverty rate | 13.93 |
| Homeownership rate | 78.39 |
| Unemployment rate | 5.64 |
| Median home value | 139900 |
| Gini index | 0.4618 |
| Vacancy rate | 12.69 |
| White | 19015 |
| Black | 312 |
| Asian | 322 |
| Native | 23 |
| Hispanic/Latino | 744 |
| Bachelor's or higher | 3288 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 26](/us/states/ar/districts/senate/26.md) — 80% (state senate)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 20% (state senate)
- [AR House District 46](/us/states/ar/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
