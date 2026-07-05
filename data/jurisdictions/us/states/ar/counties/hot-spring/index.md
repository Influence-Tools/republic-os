---
type: Jurisdiction
title: "Hot Spring County, AR"
classification: county
fips: "05059"
state: "AR"
demographics:
  population: 33180
  population_under_18: 6539
  population_18_64: 19988
  population_65_plus: 6653
  median_household_income: 55405
  poverty_rate: 15.1
  homeownership_rate: 76.47
  unemployment_rate: 3.72
  median_home_value: 151100
  gini_index: 0.4297
  vacancy_rate: 13.93
  race_white: 27282
  race_black: 3692
  race_asian: 12
  race_native: 175
  hispanic: 1362
  bachelors_plus: 5817
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/7"
    rel: in-district
    area_weight: 0.8186
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.1813
  - to: "us/states/ar/districts/house/90"
    rel: in-district
    area_weight: 0.4889
  - to: "us/states/ar/districts/house/29"
    rel: in-district
    area_weight: 0.4129
  - to: "us/states/ar/districts/house/89"
    rel: in-district
    area_weight: 0.0981
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Hot Spring County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33180 |
| Under 18 | 6539 |
| 18–64 | 19988 |
| 65+ | 6653 |
| Median household income | 55405 |
| Poverty rate | 15.1 |
| Homeownership rate | 76.47 |
| Unemployment rate | 3.72 |
| Median home value | 151100 |
| Gini index | 0.4297 |
| Vacancy rate | 13.93 |
| White | 27282 |
| Black | 3692 |
| Asian | 12 |
| Native | 175 |
| Hispanic/Latino | 1362 |
| Bachelor's or higher | 5817 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 7](/us/states/ar/districts/senate/7.md) — 82% (state senate)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 18% (state senate)
- [AR House District 90](/us/states/ar/districts/house/90.md) — 49% (state house)
- [AR House District 29](/us/states/ar/districts/house/29.md) — 41% (state house)
- [AR House District 89](/us/states/ar/districts/house/89.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
