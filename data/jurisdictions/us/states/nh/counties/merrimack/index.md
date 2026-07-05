---
type: Jurisdiction
title: "Merrimack County, NH"
classification: county
fips: "33013"
state: "NH"
demographics:
  population: 155967
  population_under_18: 28657
  population_18_64: 96249
  population_65_plus: 31061
  median_household_income: 97004
  poverty_rate: 7.64
  homeownership_rate: 73.49
  unemployment_rate: 3.12
  median_home_value: 367600
  gini_index: 0.44
  vacancy_rate: 8.42
  race_white: 141669
  race_black: 2533
  race_asian: 2362
  race_native: 259
  hispanic: 4277
  bachelors_plus: 62436
districts:
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.96
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.04
  - to: "us/states/nh/districts/senate/7"
    rel: in-district
    area_weight: 0.4992
  - to: "us/states/nh/districts/senate/17"
    rel: in-district
    area_weight: 0.2553
  - to: "us/states/nh/districts/senate/15"
    rel: in-district
    area_weight: 0.1472
  - to: "us/states/nh/districts/senate/16"
    rel: in-district
    area_weight: 0.0387
  - to: "us/states/nh/districts/senate/8"
    rel: in-district
    area_weight: 0.0327
  - to: "us/states/nh/districts/senate/5"
    rel: in-district
    area_weight: 0.0268
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Merrimack County, NH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 155967 |
| Under 18 | 28657 |
| 18–64 | 96249 |
| 65+ | 31061 |
| Median household income | 97004 |
| Poverty rate | 7.64 |
| Homeownership rate | 73.49 |
| Unemployment rate | 3.12 |
| Median home value | 367600 |
| Gini index | 0.44 |
| Vacancy rate | 8.42 |
| White | 141669 |
| Black | 2533 |
| Asian | 2362 |
| Native | 259 |
| Hispanic/Latino | 4277 |
| Bachelor's or higher | 62436 |

## Districts

- [NH-02](/us/states/nh/districts/02.md) — 96% (congressional)
- [NH-01](/us/states/nh/districts/01.md) — 4% (congressional)
- [NH Senate District 7](/us/states/nh/districts/senate/7.md) — 50% (state senate)
- [NH Senate District 17](/us/states/nh/districts/senate/17.md) — 26% (state senate)
- [NH Senate District 15](/us/states/nh/districts/senate/15.md) — 15% (state senate)
- [NH Senate District 16](/us/states/nh/districts/senate/16.md) — 4% (state senate)
- [NH Senate District 8](/us/states/nh/districts/senate/8.md) — 3% (state senate)
- [NH Senate District 5](/us/states/nh/districts/senate/5.md) — 3% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
