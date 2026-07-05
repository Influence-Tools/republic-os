---
type: Jurisdiction
title: "Merced County, CA"
classification: county
fips: "06047"
state: "CA"
demographics:
  population: 290201
  population_under_18: 83330
  population_18_64: 172870
  population_65_plus: 34001
  median_household_income: 65510
  poverty_rate: 19.09
  homeownership_rate: 54.0
  unemployment_rate: 10.56
  median_home_value: 391800
  gini_index: 0.4651
  vacancy_rate: 5.3
  race_white: 91462
  race_black: 8082
  race_asian: 20971
  race_native: 4316
  hispanic: 183933
  bachelors_plus: 34910
districts:
  - to: "us/states/ca/districts/13"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ca/districts/senate/14"
    rel: in-district
    area_weight: 0.8347
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.1653
  - to: "us/states/ca/districts/house/27"
    rel: in-district
    area_weight: 0.816
  - to: "us/states/ca/districts/house/22"
    rel: in-district
    area_weight: 0.1839
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Merced County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 290201 |
| Under 18 | 83330 |
| 18–64 | 172870 |
| 65+ | 34001 |
| Median household income | 65510 |
| Poverty rate | 19.09 |
| Homeownership rate | 54.0 |
| Unemployment rate | 10.56 |
| Median home value | 391800 |
| Gini index | 0.4651 |
| Vacancy rate | 5.3 |
| White | 91462 |
| Black | 8082 |
| Asian | 20971 |
| Native | 4316 |
| Hispanic/Latino | 183933 |
| Bachelor's or higher | 34910 |

## Districts

- [CA-13](/us/states/ca/districts/13.md) — 100% (congressional)
- [CA Senate District 14](/us/states/ca/districts/senate/14.md) — 83% (state senate)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 17% (state senate)
- [CA House District 27](/us/states/ca/districts/house/27.md) — 82% (state house)
- [CA House District 22](/us/states/ca/districts/house/22.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
