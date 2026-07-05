---
type: Jurisdiction
title: "Hill County, MT"
classification: county
fips: "30041"
state: "MT"
demographics:
  population: 16155
  population_under_18: 4563
  population_18_64: 8960
  population_65_plus: 2632
  median_household_income: 52798
  poverty_rate: 20.7
  homeownership_rate: 66.08
  unemployment_rate: 4.24
  median_home_value: 202600
  gini_index: 0.4612
  vacancy_rate: 14.21
  race_white: 10970
  race_black: 41
  race_asian: 27
  race_native: 3675
  hispanic: 566
  bachelors_plus: 3147
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/14"
    rel: in-district
    area_weight: 0.8433
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.1565
  - to: "us/states/mt/districts/house/28"
    rel: in-district
    area_weight: 0.8359
  - to: "us/states/mt/districts/house/32"
    rel: in-district
    area_weight: 0.1565
  - to: "us/states/mt/districts/house/27"
    rel: in-district
    area_weight: 0.0074
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Hill County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16155 |
| Under 18 | 4563 |
| 18–64 | 8960 |
| 65+ | 2632 |
| Median household income | 52798 |
| Poverty rate | 20.7 |
| Homeownership rate | 66.08 |
| Unemployment rate | 4.24 |
| Median home value | 202600 |
| Gini index | 0.4612 |
| Vacancy rate | 14.21 |
| White | 10970 |
| Black | 41 |
| Asian | 27 |
| Native | 3675 |
| Hispanic/Latino | 566 |
| Bachelor's or higher | 3147 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 14](/us/states/mt/districts/senate/14.md) — 84% (state senate)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 16% (state senate)
- [MT House District 28](/us/states/mt/districts/house/28.md) — 84% (state house)
- [MT House District 32](/us/states/mt/districts/house/32.md) — 16% (state house)
- [MT House District 27](/us/states/mt/districts/house/27.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
