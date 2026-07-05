---
type: Jurisdiction
title: "Pope County, AR"
classification: county
fips: "05115"
state: "AR"
demographics:
  population: 64131
  population_under_18: 14816
  population_18_64: 38741
  population_65_plus: 10574
  median_household_income: 57344
  poverty_rate: 16.9
  homeownership_rate: 70.38
  unemployment_rate: 5.15
  median_home_value: 170100
  gini_index: 0.4691
  vacancy_rate: 10.34
  race_white: 53562
  race_black: 1472
  race_asian: 513
  race_native: 496
  hispanic: 7074
  bachelors_plus: 13535
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/senate/25"
    rel: in-district
    area_weight: 0.9898
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.0101
  - to: "us/states/ar/districts/house/45"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/ar/districts/house/53"
    rel: in-district
    area_weight: 0.0598
  - to: "us/states/ar/districts/house/54"
    rel: in-district
    area_weight: 0.0101
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Pope County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64131 |
| Under 18 | 14816 |
| 18–64 | 38741 |
| 65+ | 10574 |
| Median household income | 57344 |
| Poverty rate | 16.9 |
| Homeownership rate | 70.38 |
| Unemployment rate | 5.15 |
| Median home value | 170100 |
| Gini index | 0.4691 |
| Vacancy rate | 10.34 |
| White | 53562 |
| Black | 1472 |
| Asian | 513 |
| Native | 496 |
| Hispanic/Latino | 7074 |
| Bachelor's or higher | 13535 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 25](/us/states/ar/districts/senate/25.md) — 99% (state senate)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 1% (state senate)
- [AR House District 45](/us/states/ar/districts/house/45.md) — 15% (state house)
- [AR House District 53](/us/states/ar/districts/house/53.md) — 6% (state house)
- [AR House District 54](/us/states/ar/districts/house/54.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
