---
type: Jurisdiction
title: "Sanders County, MT"
classification: county
fips: "30089"
state: "MT"
demographics:
  population: 13285
  population_under_18: 2265
  population_18_64: 6636
  population_65_plus: 4384
  median_household_income: 57476
  poverty_rate: 15.45
  homeownership_rate: 81.29
  unemployment_rate: 5.95
  median_home_value: 359000
  gini_index: 0.4448
  vacancy_rate: 19.93
  race_white: 11846
  race_black: 33
  race_asian: 60
  race_native: 384
  hispanic: 466
  bachelors_plus: 2806
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mt/districts/senate/7"
    rel: in-district
    area_weight: 0.7461
  - to: "us/states/mt/districts/senate/46"
    rel: in-district
    area_weight: 0.1891
  - to: "us/states/mt/districts/senate/45"
    rel: in-district
    area_weight: 0.0645
  - to: "us/states/mt/districts/house/14"
    rel: in-district
    area_weight: 0.7461
  - to: "us/states/mt/districts/house/91"
    rel: in-district
    area_weight: 0.1891
  - to: "us/states/mt/districts/house/90"
    rel: in-district
    area_weight: 0.0645
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Sanders County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13285 |
| Under 18 | 2265 |
| 18–64 | 6636 |
| 65+ | 4384 |
| Median household income | 57476 |
| Poverty rate | 15.45 |
| Homeownership rate | 81.29 |
| Unemployment rate | 5.95 |
| Median home value | 359000 |
| Gini index | 0.4448 |
| Vacancy rate | 19.93 |
| White | 11846 |
| Black | 33 |
| Asian | 60 |
| Native | 384 |
| Hispanic/Latino | 466 |
| Bachelor's or higher | 2806 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 7](/us/states/mt/districts/senate/7.md) — 75% (state senate)
- [MT Senate District 46](/us/states/mt/districts/senate/46.md) — 19% (state senate)
- [MT Senate District 45](/us/states/mt/districts/senate/45.md) — 6% (state senate)
- [MT House District 14](/us/states/mt/districts/house/14.md) — 75% (state house)
- [MT House District 91](/us/states/mt/districts/house/91.md) — 19% (state house)
- [MT House District 90](/us/states/mt/districts/house/90.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
