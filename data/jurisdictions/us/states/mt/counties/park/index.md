---
type: Jurisdiction
title: "Park County, MT"
classification: county
fips: "30067"
state: "MT"
demographics:
  population: 17710
  population_under_18: 2990
  population_18_64: 10360
  population_65_plus: 4360
  median_household_income: 70047
  poverty_rate: 12.34
  homeownership_rate: 69.45
  unemployment_rate: 2.71
  median_home_value: 467500
  gini_index: 0.4523
  vacancy_rate: 13.17
  race_white: 16159
  race_black: 36
  race_asian: 35
  race_native: 124
  hispanic: 638
  bachelors_plus: 7288
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/mt/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/house/57"
    rel: in-district
    area_weight: 0.9625
  - to: "us/states/mt/districts/house/58"
    rel: in-district
    area_weight: 0.0373
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Park County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17710 |
| Under 18 | 2990 |
| 18–64 | 10360 |
| 65+ | 4360 |
| Median household income | 70047 |
| Poverty rate | 12.34 |
| Homeownership rate | 69.45 |
| Unemployment rate | 2.71 |
| Median home value | 467500 |
| Gini index | 0.4523 |
| Vacancy rate | 13.17 |
| White | 16159 |
| Black | 36 |
| Asian | 35 |
| Native | 124 |
| Hispanic/Latino | 638 |
| Bachelor's or higher | 7288 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 29](/us/states/mt/districts/senate/29.md) — 100% (state senate)
- [MT House District 57](/us/states/mt/districts/house/57.md) — 96% (state house)
- [MT House District 58](/us/states/mt/districts/house/58.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
