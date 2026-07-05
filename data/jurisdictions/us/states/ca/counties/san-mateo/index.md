---
type: Jurisdiction
title: "San Mateo County, CA"
classification: county
fips: "06081"
state: "CA"
demographics:
  population: 742340
  population_under_18: 145095
  population_18_64: 465003
  population_65_plus: 132242
  median_household_income: 158855
  poverty_rate: 6.71
  homeownership_rate: 58.47
  unemployment_rate: 4.78
  median_home_value: 1559600
  gini_index: 0.4968
  vacancy_rate: 7.93
  race_white: 280904
  race_black: 15785
  race_asian: 232971
  race_native: 8434
  hispanic: 184940
  bachelors_plus: 422182
districts:
  - to: "us/states/ca/districts/16"
    rel: in-district
    area_weight: 0.4605
  - to: "us/states/ca/districts/15"
    rel: in-district
    area_weight: 0.1556
  - to: "us/states/ca/districts/senate/13"
    rel: in-district
    area_weight: 0.5938
  - to: "us/states/ca/districts/senate/11"
    rel: in-district
    area_weight: 0.0238
  - to: "us/states/ca/districts/house/23"
    rel: in-district
    area_weight: 0.4623
  - to: "us/states/ca/districts/house/21"
    rel: in-district
    area_weight: 0.1315
  - to: "us/states/ca/districts/house/19"
    rel: in-district
    area_weight: 0.0238
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# San Mateo County, CA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 742340 |
| Under 18 | 145095 |
| 18–64 | 465003 |
| 65+ | 132242 |
| Median household income | 158855 |
| Poverty rate | 6.71 |
| Homeownership rate | 58.47 |
| Unemployment rate | 4.78 |
| Median home value | 1559600 |
| Gini index | 0.4968 |
| Vacancy rate | 7.93 |
| White | 280904 |
| Black | 15785 |
| Asian | 232971 |
| Native | 8434 |
| Hispanic/Latino | 184940 |
| Bachelor's or higher | 422182 |

## Districts

- [CA-16](/us/states/ca/districts/16.md) — 46% (congressional)
- [CA-15](/us/states/ca/districts/15.md) — 16% (congressional)
- [CA Senate District 13](/us/states/ca/districts/senate/13.md) — 59% (state senate)
- [CA Senate District 11](/us/states/ca/districts/senate/11.md) — 2% (state senate)
- [CA House District 23](/us/states/ca/districts/house/23.md) — 46% (state house)
- [CA House District 21](/us/states/ca/districts/house/21.md) — 13% (state house)
- [CA House District 19](/us/states/ca/districts/house/19.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
