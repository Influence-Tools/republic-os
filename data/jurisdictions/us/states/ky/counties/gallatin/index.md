---
type: Jurisdiction
title: "Gallatin County, KY"
classification: county
fips: "21077"
state: "KY"
demographics:
  population: 8769
  population_under_18: 2013
  population_18_64: 5366
  population_65_plus: 1390
  median_household_income: 63346
  poverty_rate: 13.81
  homeownership_rate: 75.07
  unemployment_rate: 4.61
  median_home_value: 178200
  gini_index: 0.4397
  vacancy_rate: 14.44
  race_white: 7880
  race_black: 237
  race_asian: 41
  race_native: 1
  hispanic: 478
  bachelors_plus: 1220
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/senate/20"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/61"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Gallatin County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8769 |
| Under 18 | 2013 |
| 18–64 | 5366 |
| 65+ | 1390 |
| Median household income | 63346 |
| Poverty rate | 13.81 |
| Homeownership rate | 75.07 |
| Unemployment rate | 4.61 |
| Median home value | 178200 |
| Gini index | 0.4397 |
| Vacancy rate | 14.44 |
| White | 7880 |
| Black | 237 |
| Asian | 41 |
| Native | 1 |
| Hispanic/Latino | 478 |
| Bachelor's or higher | 1220 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 20](/us/states/ky/districts/senate/20.md) — 100% (state senate)
- [KY House District 61](/us/states/ky/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
