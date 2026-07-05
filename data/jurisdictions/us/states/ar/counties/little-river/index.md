---
type: Jurisdiction
title: "Little River County, AR"
classification: county
fips: "05081"
state: "AR"
demographics:
  population: 11821
  population_under_18: 2589
  population_18_64: 6711
  population_65_plus: 2521
  median_household_income: 53344
  poverty_rate: 15.53
  homeownership_rate: 80.06
  unemployment_rate: 7.32
  median_home_value: 113500
  gini_index: 0.4404
  vacancy_rate: 20.45
  race_white: 8551
  race_black: 2249
  race_asian: 46
  race_native: 75
  hispanic: 474
  bachelors_plus: 1957
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9845
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.0093
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.006
  - to: "us/states/ar/districts/senate/4"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ar/districts/house/87"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Little River County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11821 |
| Under 18 | 2589 |
| 18–64 | 6711 |
| 65+ | 2521 |
| Median household income | 53344 |
| Poverty rate | 15.53 |
| Homeownership rate | 80.06 |
| Unemployment rate | 7.32 |
| Median home value | 113500 |
| Gini index | 0.4404 |
| Vacancy rate | 20.45 |
| White | 8551 |
| Black | 2249 |
| Asian | 46 |
| Native | 75 |
| Hispanic/Latino | 474 |
| Bachelor's or higher | 1957 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 98% (congressional)
- [TX-04](/us/states/tx/districts/04.md) — 1% (congressional)
- [TX-01](/us/states/tx/districts/01.md) — 1% (congressional)
- [AR Senate District 4](/us/states/ar/districts/senate/4.md) — 100% (state senate)
- [AR House District 87](/us/states/ar/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
