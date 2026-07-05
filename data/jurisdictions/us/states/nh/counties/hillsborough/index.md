---
type: Jurisdiction
title: "Hillsborough County, NH"
classification: county
fips: "33011"
state: "NH"
demographics:
  population: 426378
  population_under_18: 83696
  population_18_64: 268864
  population_65_plus: 73818
  median_household_income: 103545
  poverty_rate: 6.74
  homeownership_rate: 67.39
  unemployment_rate: 3.08
  median_home_value: 421100
  gini_index: 0.4299
  vacancy_rate: 5.06
  race_white: 347760
  race_black: 10520
  race_asian: 18375
  race_native: 598
  hispanic: 36414
  bachelors_plus: 177449
districts:
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.8441
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.1556
  - to: "us/states/nh/districts/senate/9"
    rel: in-district
    area_weight: 0.2113
  - to: "us/states/nh/districts/senate/8"
    rel: in-district
    area_weight: 0.2002
  - to: "us/states/nh/districts/senate/12"
    rel: in-district
    area_weight: 0.1483
  - to: "us/states/nh/districts/senate/11"
    rel: in-district
    area_weight: 0.1333
  - to: "us/states/nh/districts/senate/10"
    rel: in-district
    area_weight: 0.0781
  - to: "us/states/nh/districts/senate/7"
    rel: in-district
    area_weight: 0.0504
  - to: "us/states/nh/districts/senate/16"
    rel: in-district
    area_weight: 0.0458
  - to: "us/states/nh/districts/senate/18"
    rel: in-district
    area_weight: 0.0377
  - to: "us/states/nh/districts/senate/14"
    rel: in-district
    area_weight: 0.0327
  - to: "us/states/nh/districts/senate/22"
    rel: in-district
    area_weight: 0.03
  - to: "us/states/nh/districts/senate/13"
    rel: in-district
    area_weight: 0.017
  - to: "us/states/nh/districts/senate/20"
    rel: in-district
    area_weight: 0.015
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Hillsborough County, NH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 426378 |
| Under 18 | 83696 |
| 18–64 | 268864 |
| 65+ | 73818 |
| Median household income | 103545 |
| Poverty rate | 6.74 |
| Homeownership rate | 67.39 |
| Unemployment rate | 3.08 |
| Median home value | 421100 |
| Gini index | 0.4299 |
| Vacancy rate | 5.06 |
| White | 347760 |
| Black | 10520 |
| Asian | 18375 |
| Native | 598 |
| Hispanic/Latino | 36414 |
| Bachelor's or higher | 177449 |

## Districts

- [NH-02](/us/states/nh/districts/02.md) — 84% (congressional)
- [NH-01](/us/states/nh/districts/01.md) — 16% (congressional)
- [NH Senate District 9](/us/states/nh/districts/senate/9.md) — 21% (state senate)
- [NH Senate District 8](/us/states/nh/districts/senate/8.md) — 20% (state senate)
- [NH Senate District 12](/us/states/nh/districts/senate/12.md) — 15% (state senate)
- [NH Senate District 11](/us/states/nh/districts/senate/11.md) — 13% (state senate)
- [NH Senate District 10](/us/states/nh/districts/senate/10.md) — 8% (state senate)
- [NH Senate District 7](/us/states/nh/districts/senate/7.md) — 5% (state senate)
- [NH Senate District 16](/us/states/nh/districts/senate/16.md) — 5% (state senate)
- [NH Senate District 18](/us/states/nh/districts/senate/18.md) — 4% (state senate)
- [NH Senate District 14](/us/states/nh/districts/senate/14.md) — 3% (state senate)
- [NH Senate District 22](/us/states/nh/districts/senate/22.md) — 3% (state senate)
- [NH Senate District 13](/us/states/nh/districts/senate/13.md) — 2% (state senate)
- [NH Senate District 20](/us/states/nh/districts/senate/20.md) — 2% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
